from flask import Flask, render_template_string
import requests
import datetime
import time
import json  # for safe JSON in JS

app = Flask(__name__)

HEADERS = {
    "accept": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Caching globals
CACHE_SECONDS = 60
last_fetch_time = 0
cached_coins = []
cached_metrics = {}

def get_global_metrics():
    global cached_metrics, last_fetch_time
    if time.time() - last_fetch_time < CACHE_SECONDS and cached_metrics:
        return cached_metrics
    try:
        res = requests.get("https://api.coingecko.com/api/v3/global", headers=HEADERS, timeout=15)
        res.raise_for_status()
        data = res.json()['data']
        total_cap = data['total_market_cap']['usd']
        btc_dom = round(data['market_cap_percentage']['btc'], 1)

        # Fear & Greed
        fg_res = requests.get("https://api.alternative.me/fng/?limit=1", headers=HEADERS, timeout=10)
        fg_res.raise_for_status()
        fg_data = fg_res.json()['data'][0]
        fear_greed = int(fg_data['value'])

        # Altcoin Season Index
        alt_res = requests.get("https://api.blockchaincenter.net/v1/altcoin-season-index", headers=HEADERS, timeout=10)
        alt_res.raise_for_status()
        alt_season = alt_res.json()['index']

        metrics = {
            "total_market_cap": total_cap,
            "btc_dominance": btc_dom,
            "fear_greed": fear_greed,
            "alt_season": alt_season,
        }
        cached_metrics = metrics
        last_fetch_time = time.time()
        return metrics
    except Exception as e:
        print("Global metrics error:", e)
        return {
            "total_market_cap": 3270220197008,
            "btc_dominance": 57.2,
            "fear_greed": 26,
            "alt_season": 39,
        }

def fetch_crypto_data():
    global cached_coins, last_fetch_time
    if time.time() - last_fetch_time < CACHE_SECONDS and cached_coins:
        return cached_coins
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,  # Load more for search/trending
        "page": 1,
        "price_change_percentage": "1h,24h,7d",
        "sparkline": True,
    }
    for attempt in range(5):
        try:
            response = requests.get(url, params=params, headers=HEADERS, timeout=15)
            if response.status_code == 429:
                time.sleep(2 ** attempt + 1)  # Exponential backoff
                continue
            response.raise_for_status()
            data = response.json()
            formatted = []
            for rank, coin in enumerate(data, 1):
                sparkline = coin.get("sparkline_in_7d", {}).get("price", [])
                if not sparkline: continue  # Skip if no sparkline
                formatted.append({
                    "rank": rank,
                    "name": coin["name"],
                    "symbol": coin["symbol"].upper(),
                    "logo": coin["image"],
                    "price": float(coin["current_price"] or 0),
                    "change_1h": round(float(coin.get("price_change_percentage_1h_in_currency") or 0), 2),
                    "change_24h": round(float(coin.get("price_change_percentage_24h_in_currency") or 0), 2),
                    "change_7d": round(float(coin.get("price_change_percentage_7d_in_currency") or 0), 2),
                    "market_cap": int(coin["market_cap"] or 0),
                    "volume_24h": int(coin["total_volume"] or 0),
                    "sparkline_prices": sparkline,
                })
            cached_coins = formatted
            last_fetch_time = time.time()
            return formatted
        except Exception as e:
            print("Data fetch error (attempt {}): {}".format(attempt + 1, e))
            if attempt < 4:
                time.sleep(5)
    return []  # Final fallback

@app.route('/')
def index():
    metrics = get_global_metrics()
    data = fetch_crypto_data()[:100]  # Top 100 for main
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, data=data, last_update=last_update, metrics=metrics)

@app.route('/trending')
def trending():
    metrics = get_global_metrics()
    all_data = fetch_crypto_data()
    # Sort by 24h change desc, positive only, top 25
    trending_data = sorted([coin for coin in all_data if coin['change_24h'] > 0], key=lambda x: x['change_24h'], reverse=True)[:25]
    # Re-rank them
    for i, coin in enumerate(trending_data, 1):
        coin['rank'] = i
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(TRENDING_TEMPLATE, data=trending_data, last_update=last_update, metrics=metrics)

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
      tailwind.config = {
        darkMode: 'class',
      }
    </script>
    <style>
        .hover-row:hover { background-color: #333; cursor: pointer; } /* dark */
        .light .hover-row:hover { background-color: #eee; }
        .sparkline { height: 60px; width: 140px; }
        .modal { display: none; position: fixed; z-index: 50; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.8); }
        .modal-content { background-color: #222; margin: 15% auto; padding: 20px; border: 1px solid #888; width: 80%; max-width: 600px; border-radius: 1rem; color: #fff; }
        .light .modal-content { background-color: #fff; color: #000; }
        .close { color: #aaa; float: right; font-size: 28px; font-weight: bold; }
        .close:hover { color: #fff; text-decoration: none; cursor: pointer; }
        .light .close:hover { color: #000; }
    </style>
</head>
<body class="bg-black text-white dark:bg-black dark:text-white light:bg-white light:text-black transition-colors duration-300">
    <header class="bg-blue-600 text-white py-6 px-8 flex justify-between items-center light:bg-blue-500 light:text-black">
        <a href="/" class="flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12">
            <div class="text-4xl font-bold">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <a href="/trending" class="px-4 py-2 rounded hover:bg-blue-700 light:hover:bg-blue-400">Trending</a>
            <input id="search-input" type="text" class="px-6 py-3 rounded-full bg-gray-800 text-white light:bg-gray-200 light:text-black" placeholder="Search crypto...">
            <button id="toggle-theme" class="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600 light:bg-gray-300 light:hover:bg-gray-200 light:text-black">Toggle Theme</button>
        </div>
    </header>

    <div class="container mx-auto px-6 py-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.2f}".format(metrics.total_market_cap / 1e12) }}T</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: {{ (metrics.total_market_cap / 5e12 * 100) | min(100) }}%"></div>
                </div>
            </div>
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Fear & Greed</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-gray-400 light:text-gray-600">Fear</p>
                {% set fg_color = 'bg-red-500' if metrics.fear_greed < 25 else 'bg-orange-500' if metrics.fear_greed < 50 else 'bg-yellow-500' if metrics.fear_greed < 51 else 'bg-green-500' if metrics.fear_greed < 76 else 'bg-lime-500' %}
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="{{ fg_color }} h-1.5 rounded-full" style="width: {{ metrics.fear_greed }}%"></div>
                </div>
            </div>
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Altcoin Season</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}/100</p>
                <p class="text-gray-400 light:text-gray-600">Bitcoin Season</p>
                {% set alt_color = 'bg-red-500' if metrics.alt_season < 25 else 'bg-orange-500' if metrics.alt_season < 50 else 'bg-yellow-500' if metrics.alt_season == 50 else 'bg-green-500' if metrics.alt_season < 76 else 'bg-lime-500' %}
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="{{ alt_color }} h-1.5 rounded-full" style="width: {{ metrics.alt_season }}%"></div>
                </div>
            </div>
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ metrics.btc_dominance }}%</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: {{ metrics.btc_dominance }}%"></div>
                </div>
            </div>
        </div>

        <div class="overflow-x-auto rounded-2xl bg-gray-800 light:bg-gray-200">
            <table class="w-full text-left">
                <thead class="bg-gray-700 text-gray-300 text-sm uppercase light:bg-gray-300 light:text-gray-700">
                    <tr>
                        <th class="px-6 py-4">#</th>
                        <th class="px-6 py-4">Name</th>
                        <th class="px-6 py-4 text-right">Price</th>
                        <th class="px-6 py-4 text-right">1h %</th>
                        <th class="px-6 py-4 text-right">24h %</th>
                        <th class="px-6 py-4 text-right">7d %</th>
                        <th class="px-6 py-4 text-right">Market Cap</th>
                        <th class="px-6 py-4 text-right">Volume(24h)</th>
                        <th class="px-6 py-4 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody id="crypto-table">
                    {% if data %}
                    {% for coin in data %}
                    <tr class="hover-row border-b border-gray-700 light:border-gray-300" data-coin='{{ coin | tojson }}'>
                        <td class="px-6 py-4 text-gray-400 light:text-gray-600">{{ coin.rank }}</td>
                        <td class="px-6 py-4">
                            <div class="flex items-center gap-4">
                                <img src="{{ coin.logo }}" class="w-10 h-10 rounded-full">
                                <div>
                                    <div class="font-bold">{{ coin.name }}</div>
                                    <div class="text-gray-500 light:text-gray-400">{{ coin.symbol }}</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-4 text-right font-bold">${{ "{:.2f}".format(coin.price) }}</td>
                        <td class="px-6 py-4 text-right {% if coin.change_1h > 0 %}text-green-500{% elif coin.change_1h < 0 %}text-red-500{% endif %}">
                            {% if coin.change_1h > 0 %}+{{ coin.change_1h }}%{% elif coin.change_1h < 0 %}{{ coin.change_1h }}%{% else %}-{% endif %}
                        </td>
                        <td class="px-6 py-4 text-right {% if coin.change_24h > 0 %}text-green-500{% elif coin.change_24h < 0 %}text-red-500{% endif %}">
                            {% if coin.change_24h > 0 %}+{{ coin.change_24h }}%{% elif coin.change_24h < 0 %}{{ coin.change_24h }}%{% else %}-{% endif %}
                        </td>
                        <td class="px-6 py-4 text-right {% if coin.change_7d > 0 %}text-green-500{% elif coin.change_7d < 0 %}text-red-500{% endif %}">
                            {% if coin.change_7d > 0 %}+{{ coin.change_7d }}%{% elif coin.change_7d < 0 %}{{ coin.change_7d }}%{% else %}-{% endif %}
                        </td>
                        <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">${{ "{:,.0f}".format(coin.market_cap) }}</td>
                        <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">${{ "{:,.0f}".format(coin.volume_24h) }}</td>
                        <td class="px-6 py-4 text-center">
                            <canvas class="sparkline" data-prices='{{ coin.sparkline_prices | tojson }}'></canvas>
                        </td>
                    </tr>
                    {% endfor %}
                    {% else %}
                    <tr>
                        <td colspan="9" class="px-6 py-4 text-center text-red-500">Failed to load data. Try refreshing.</td>
                    </tr>
                    {% endif %}
                </tbody>
            </table>
        </div>

        <p class="text-center text-gray-500 mt-8 light:text-gray-400">Last update: {{ last_update }} • Powered by CoinGecko</p>
    </div>

    <!-- Modal -->
    <div id="coin-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2 id="modal-name" class="text-2xl font-bold"></h2>
            <p id="modal-symbol"></p>
            <p id="modal-price"></p>
            <p id="modal-change-24h"></p>
            <p id="modal-market-cap"></p>
            <!-- Add more details as needed -->
        </div>
    </div>

    <script>
        // Theme toggle
        const html = document.documentElement;
        const toggleBtn = document.getElementById('toggle-theme');
        if (localStorage.theme === 'light') {
            html.classList.remove('dark');
            html.classList.add('light');
            toggleBtn.textContent = 'Dark Mode';
        } else {
            html.classList.add('dark');
            html.classList.remove('light');
            toggleBtn.textContent = 'Light Mode';
        }
        toggleBtn.addEventListener('click', () => {
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                html.classList.add('light');
                localStorage.theme = 'light';
                toggleBtn.textContent = 'Dark Mode';
            } else {
                html.classList.add('dark');
                html.classList.remove('light');
                localStorage.theme = 'dark';
                toggleBtn.textContent = 'Light Mode';
            }
        });

        // Sparklines
        document.querySelectorAll('.sparkline').forEach(canvas => {
            const prices = JSON.parse(canvas.dataset.prices || '[]');
            if (prices.length < 2) return;
            const up = prices[prices.length - 1] >= prices[0];
            new Chart(canvas, {
                type: 'line',
                data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
                options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
            });
        });

        // Search filter
        const searchInput = document.getElementById('search-input');
        const tableBody = document.getElementById('crypto-table');
        const originalRows = Array.from(tableBody.querySelectorAll('tr:not(.no-results)'));
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.toLowerCase();
            tableBody.innerHTML = '';
            const matches = originalRows.filter(row => {
                const name = row.querySelector('.font-bold')?.textContent.toLowerCase() || '';
                const symbol = row.querySelector('.text-gray-500, .text-gray-400')?.textContent.toLowerCase() || '';
                return name.includes(query) || symbol.includes(query);
            });
            if (matches.length) {
                matches.forEach(row => tableBody.appendChild(row));
            } else {
                tableBody.innerHTML = '<tr><td colspan="9" class="px-6 py-4 text-center text-red-500">No results found.</td></tr>';
            }
        });

        // Modal on row click
        const modal = document.getElementById('coin-modal');
        const closeBtn = document.querySelector('.close');
        tableBody.addEventListener('click', (e) => {
            const row = e.target.closest('tr');
            if (!row || !row.dataset.coin) return;
            const coin = JSON.parse(row.dataset.coin);
            document.getElementById('modal-name').textContent = coin.name;
            document.getElementById('modal-symbol').textContent = coin.symbol;
            document.getElementById('modal-price').textContent = `Price: $${coin.price.toFixed(2)}`;
            document.getElementById('modal-change-24h').textContent = `24h Change: ${coin.change_24h}%`;
            document.getElementById('modal-market-cap').textContent = `Market Cap: $${coin.market_cap.toLocaleString()}`;
            modal.style.display = 'block';
        });
        closeBtn.addEventListener('click', () => modal.style.display = 'none');
        window.addEventListener('click', (e) => { if (e.target === modal) modal.style.display = 'none'; });
    </script>
</body>
</html>
'''

TRENDING_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trending - TradeScout Pro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
      tailwind.config = {
        darkMode: 'class',
      }
    </script>
    <style>
        .hover-row:hover { background-color: #333; cursor: pointer; } /* dark */
        .light .hover-row:hover { background-color: #eee; }
        .sparkline { height: 60px; width: 140px; }
        .modal { display: none; position: fixed; z-index: 50; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.8); }
        .modal-content { background-color: #222; margin: 15% auto; padding: 20px; border: 1px solid #888; width: 80%; max-width: 600px; border-radius: 1rem; color: #fff; }
        .light .modal-content { background-color: #fff; color: #000; }
        .close { color: #aaa; float: right; font-size: 28px; font-weight: bold; }
        .close:hover { color: #fff; text-decoration: none; cursor: pointer; }
        .light .close:hover { color: #000; }
    </style>
</head>
<body class="bg-black text-white dark:bg-black dark:text-white light:bg-white light:text-black transition-colors duration-300">
    <header class="bg-blue-600 text-white py-6 px-8 flex justify-between items-center light:bg-blue-500 light:text-black">
        <a href="/" class="flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12">
            <div class="text-4xl font-bold">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <a href="/" class="px-4 py-2 rounded hover:bg-blue-700 light:hover:bg-blue-400">Home</a>
            <input id="search-input" type="text" class="px-6 py-3 rounded-full bg-gray-800 text-white light:bg-gray-200 light:text-black" placeholder="Search crypto...">
            <button id="toggle-theme" class="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600 light:bg-gray-300 light:hover:bg-gray-200 light:text-black">Toggle Theme</button>
        </div>
    </header>

    <div class="container mx-auto px-6 py-8">
        <h1 class="text-3xl font-bold mb-6">Top 25 Trending Coins (24h Uptrends)</h1>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <!-- Same metrics cards as index -->
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.2f}".format(metrics.total_market_cap / 1e12) }}T</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: {{ (metrics.total_market_cap / 5e12 * 100) | min(100) }}%"></div>
                </div>
            </div>
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Fear & Greed</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-gray-400 light:text-gray-600">Fear</p>
                {% set fg_color = 'bg-red-500' if metrics.fear_greed < 25 else 'bg-orange-500' if metrics.fear_greed < 50 else 'bg-yellow-500' if metrics.fear_greed < 51 else 'bg-green-500' if metrics.fear_greed < 76 else 'bg-lime-500' %}
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="{{ fg_color }} h-1.5 rounded-full" style="width: {{ metrics.fear_greed }}%"></div>
                </div>
            </div>
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Altcoin Season</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}/100</p>
                <p class="text-gray-400 light:text-gray-600">Bitcoin Season</p>
                {% set alt_color = 'bg-red-500' if metrics.alt_season < 25 else 'bg-orange-500' if metrics.alt_season < 50 else 'bg-yellow-500' if metrics.alt_season == 50 else 'bg-green-500' if metrics.alt_season < 76 else 'bg-lime-500' %}
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="{{ alt_color }} h-1.5 rounded-full" style="width: {{ metrics.alt_season }}%"></div>
                </div>
            </div>
            <div class="card bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ metrics.btc_dominance }}%</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-1.5 light:bg-gray-300">
                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: {{ metrics.btc_dominance }}%"></div>
                </div>
            </div>
        </div>

        <div class="overflow-x-auto rounded-2xl bg-gray-800 light:bg-gray-200">
            <table class="w-full text-left">
                <thead class="bg-gray-700 text-gray-300 text-sm uppercase light:bg-gray-300 light:text-gray-700">
                    <tr>
                        <th class="px-6 py-4">#</th>
                        <th class="px-6 py-4">Name</th>
                        <th class="px-6 py-4 text-right">Price</th>
                        <th class="px-6 py-4 text-right">1h %</th>
                        <th class="px-6 py-4 text-right">24h %</th>
                        <th class="px-6 py-4 text-right">7d %</th>
                        <th class="px-6 py-4 text-right">Market Cap</th>
                        <th class="px-6 py-4 text-right">Volume(24h)</th>
                        <th class="px-6 py-4 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody id="crypto-table">
                    {% if data %}
                    {% for coin in data %}
                    <tr class="hover-row border-b border-gray-700 light:border-gray-300" data-coin='{{ coin | tojson }}'>
                        <td class="px-6 py-4 text-gray-400 light:text-gray-600">{{ coin.rank }}</td>
                        <td class="px-6 py-4">
                            <div class="flex items-center gap-4">
                                <img src="{{ coin.logo }}" class="w-10 h-10 rounded-full">
                                <div>
                                    <div class="font-bold">{{ coin.name }}</div>
                                    <div class="text-gray-500 light:text-gray-400">{{ coin.symbol }}</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-4 text-right font-bold">${{ "{:.2f}".format(coin.price) }}</td>
                        <td class="px-6 py-4 text-right {% if coin.change_1h > 0 %}text-green-500{% elif coin.change_1h < 0 %}text-red-500{% endif %}">
                            {% if coin.change_1h > 0 %}+{{ coin.change_1h }}%{% elif coin.change_1h < 0 %}{{ coin.change_1h }}%{% else %}-{% endif %}
                        </td>
                        <td class="px-6 py-4 text-right {% if coin.change_24h > 0 %}text-green-500{% elif coin.change_24h < 0 %}text-red-500{% endif %}">
                            {% if coin.change_24h > 0 %}+{{ coin.change_24h }}%{% elif coin.change_24h < 0 %}{{ coin.change_24h }}%{% else %}-{% endif %}
                        </td>
                        <td class="px-6 py-4 text-right {% if coin.change_7d > 0 %}text-green-500{% elif coin.change_7d < 0 %}text-red-500{% endif %}">
                            {% if coin.change_7d > 0 %}+{{ coin.change_7d }}%{% elif coin.change_7d < 0 %}{{ coin.change_7d }}%{% else %}-{% endif %}
                        </td>
                        <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">${{ "{:,.0f}".format(coin.market_cap) }}</td>
                        <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">${{ "{:,.0f}".format(coin.volume_24h) }}</td>
                        <td class="px-6 py-4 text-center">
                            <canvas class="sparkline" data-prices='{{ coin.sparkline_prices | tojson }}'></canvas>
                        </td>
                    </tr>
                    {% endfor %}
                    {% else %}
                    <tr>
                        <td colspan="9" class="px-6 py-4 text-center text-red-500">Failed to load data. Try refreshing.</td>
                    </tr>
                    {% endif %}
                </tbody>
            </table>
        </div>

        <p class="text-center text-gray-500 mt-8 light:text-gray-400">Last update: {{ last_update }} • Powered by CoinGecko</p>
    </div>

    <!-- Modal (same as index) -->
    <div id="coin-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2 id="modal-name" class="text-2xl font-bold"></h2>
            <p id="modal-symbol"></p>
            <p id="modal-price"></p>
            <p id="modal-change-24h"></p>
            <p id="modal-market-cap"></p>
        </div>
    </div>

    <script>
        // Theme toggle (same as index)
        const html = document.documentElement;
        const toggleBtn = document.getElementById('toggle-theme');
        if (localStorage.theme === 'light') {
            html.classList.remove('dark');
            html.classList.add('light');
            toggleBtn.textContent = 'Dark Mode';
        } else {
            html.classList.add('dark');
            html.classList.remove('light');
            toggleBtn.textContent = 'Light Mode';
        }
        toggleBtn.addEventListener('click', () => {
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                html.classList.add('light');
                localStorage.theme = 'light';
                toggleBtn.textContent = 'Dark Mode';
            } else {
                html.classList.add('dark');
                html.classList.remove('light');
                localStorage.theme = 'dark';
                toggleBtn.textContent = 'Light Mode';
            }
        });

        // Sparklines (same as index)
        document.querySelectorAll('.sparkline').forEach(canvas => {
            const prices = JSON.parse(canvas.dataset.prices || '[]');
            if (prices.length < 2) return;
            const up = prices[prices.length - 1] >= prices[0];
            new Chart(canvas, {
                type: 'line',
                data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
                options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
            });
        });

        // Search filter (same as index)
        const searchInput = document.getElementById('search-input');
        const tableBody = document.getElementById('crypto-table');
        const originalRows = Array.from(tableBody.querySelectorAll('tr:not(.no-results)'));
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.toLowerCase();
            tableBody.innerHTML = '';
            const matches = originalRows.filter(row => {
                const name = row.querySelector('.font-bold')?.textContent.toLowerCase() || '';
                const symbol = row.querySelector('.text-gray-500, .text-gray-400')?.textContent.toLowerCase() || '';
                return name.includes(query) || symbol.includes(query);
            });
            if (matches.length) {
                matches.forEach(row => tableBody.appendChild(row));
            } else {
                tableBody.innerHTML = '<tr><td colspan="9" class="px-6 py-4 text-center text-red-500">No results found.</td></tr>';
            }
        });

        // Modal on row click (same as index)
        const modal = document.getElementById('coin-modal');
        const closeBtn = document.querySelector('.close');
        tableBody.addEventListener('click', (e) => {
            const row = e.target.closest('tr');
            if (!row || !row.dataset.coin) return;
            const coin = JSON.parse(row.dataset.coin);
            document.getElementById('modal-name').textContent = coin.name;
            document.getElementById('modal-symbol').textContent = coin.symbol;
            document.getElementById('modal-price').textContent = `Price: $${coin.price.toFixed(2)}`;
            document.getElementById('modal-change-24h').textContent = `24h Change: ${coin.change_24h}%`;
            document.getElementById('modal-market-cap').textContent = `Market Cap: $${coin.market_cap.toLocaleString()}`;
            modal.style.display = 'block';
        });
        closeBtn.addEventListener('click', () => modal.style.display = 'none');
        window.addEventListener('click', (e) => { if (e.target === modal) modal.style.display = 'none'; });
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
