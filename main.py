from flask import Flask, render_template_string, jsonify, request
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

# Global metrics (Market Cap, BTC Dominance)
def get_global_metrics():
    url = "https://api.coingecko.com/api/v3/global"
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        data = res.json()['data']
        total_cap = data['total_market_cap']['usd']
        btc_dom = round(data['market_cap_percentage']['btc'], 1)
        return {
            "total_market_cap": total_cap,
            "btc_dominance": btc_dom,
            "fear_greed": 40,  # Current value (you can update manually or use another API)
            "alt_season": 24,  # Current value
        }
    except Exception as e:
        print("Metrics error:", e)
        return {
            "total_market_cap": 3120000000000,
            "btc_dominance": 58.4,
            "fear_greed": 40,
            "alt_season": 24,
        }

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "price_change_percentage": "1h,24h,7d",
        "sparkline": True,
    }
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        formatted = []
        for rank, coin in enumerate(data, 1):
            formatted.append({
                "rank": rank,
                "id": coin["id"],
                "name": coin["name"],
                "symbol": coin["symbol"].upper(),
                "logo": coin["image"],
                "price": coin["current_price"] or 0,
                "change_1h": round(coin.get("price_change_percentage_1h_in_currency") or 0, 2),
                "change_24h": round(coin.get("price_change_percentage_24h_in_currency") or 0, 2),
                "change_7d": round(coin.get("price_change_percentage_7d_in_currency") or 0, 2),
                "market_cap": coin["market_cap"] or 0,
                "volume_24h": coin["total_volume"] or 0,
                "sparkline_prices": coin.get("sparkline_in_7d", {}).get("price", []),
            })
        return formatted
    except Exception as e:
        print("Data error:", e)
        return []

def fetch_trending_data():
    try:
        trending_url = "https://api.coingecko.com/api/v3/search/trending"
        headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
        trending_res = requests.get(trending_url, headers=headers, timeout=15)
        trending_res.raise_for_status()
        trending_items = trending_res.json().get('coins', [])
        ids = [item['item']['id'] for item in trending_items]

        if ids:
            markets_url = "https://api.coingecko.com/api/v3/coins/markets"
            markets_params = {
                "vs_currency": "usd",
                "ids": ','.join(ids),
                "order": "market_cap_desc",
                "per_page": 50,
                "page": 1,
                "sparkline": True,
                "price_change_percentage": "1h,24h,7d",
            }
            markets_res = requests.get(markets_url, params=markets_params, headers=headers, timeout=15)
            markets_res.raise_for_status()
            full_data = markets_res.json()

            order_map = {item['item']['id']: idx for idx, item in enumerate(trending_items)}
            full_data.sort(key=lambda c: order_map.get(c['id'], 999))

            formatted = []
            for rank, coin in enumerate(full_data, 1):
                formatted.append({
                    "rank": rank,
                    "id": coin["id"],
                    "name": coin["name"],
                    "symbol": coin["symbol"].upper(),
                    "logo": coin["image"],
                    "price": coin["current_price"] or 0,
                    "change_1h": round(coin.get("price_change_percentage_1h_in_currency") or 0, 2),
                    "change_24h": round(coin.get("price_change_percentage_24h_in_currency") or 0, 2),
                    "change_7d": round(coin.get("price_change_percentage_7d_in_currency") or 0, 2),
                    "market_cap": coin["market_cap"] or 0,
                    "volume_24h": coin["total_volume"] or 0,
                    "sparkline_prices": coin.get("sparkline_in_7d", {}).get("price", []),
                })
            return formatted
    except Exception as e:
        print("Trending error:", e)
    return fetch_crypto_data()

@app.route('/')
def index():
    metrics = get_global_metrics()
    data = fetch_crypto_data()
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, data=data, last_update=last_update, metrics=metrics, page="top")

@app.route('/trending')
def trending():
    metrics = get_global_metrics()
    data = fetch_trending_data()
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, data=data, last_update=last_update, metrics=metrics, page="trending")

@app.route('/api/coin_ohlc/<id>')
def coin_ohlc(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}/ohlc"
    params = {"vs_currency": "usd", "days": "30"}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        return jsonify(response.json())
    except:
        return jsonify([]), 500

application = app  # Gunicorn fallback

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-chart-financial"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
        [data-theme="dark"] {
            --bg: #000;
            --card-bg: #111;
            --text: #fff;
            --green: #00ff99;
            --red: #ff4444;
            --header: #0066ff;
        }
        [data-theme="light"] {
            --bg: #fff;
            --card-bg: #f0f0f0;
            --text: #000;
            --green: #00aa66;
            --red: #cc3333;
            --header: #005edc;
        }
        body { background: var(--bg); color: var(--text); transition: background 0.3s; }
        .card { background: var(--card-bg); }
        .text-green { color: var(--green); }
        .text-red { color: var(--red); }
        .header { background: var(--header); }
    </style>
</head>
<body class="min-h-screen">
    <header class="header text-white py-6 px-8 flex justify-between items-center sticky top-0 z-50 shadow-xl">
        <a href="/" class="text-4xl font-bold flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12 rounded">
            TradeScout Pro
        </a>
        <div class="flex items-center gap-8 text-lg">
            <a href="/" class="{% if page == 'top' %}underline{% endif %} hover:underline">Top 100</a>
            <a href="/trending" class="{% if page == 'trending' %}underline{% endif %} hover:underline">Trending</a>
            <button id="themeToggle" class="text-3xl">🌙</button>
        </div>
    </header>

    <!-- Metrics Cards -->
    <div class="container mx-auto px-6 py-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <div class="card rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.0f}".format(metrics.total_market_cap / 1e12) }}T</p>
            </div>
            <div class="card rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">Fear & Greed Index</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-sm text-gray-400">Neutral</p>
            </div>
            <div class="card rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">Altcoin Season Index</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}/100</p>
                <p class="text-sm text-gray-400">Bitcoin Season</p>
            </div>
            <div class="card rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ metrics.btc_dominance }}%</p>
            </div>
        </div>
    </div>

    <!-- Table -->
    <div class="container mx-auto px-6 pb-10">
        <div class="overflow-x-auto rounded-2xl shadow-2xl bg-gray-900/50">
            <table class="w-full">
                <thead class="bg-gray-800 text-gray-300 text-sm uppercase">
                    <tr>
                        <th class="px-6 py-4 text-left">#</th>
                        <th class="px-6 py-4 text-left">Name</th>
                        <th class="px-6 py-4 text-right">Price</th>
                        <th class="px-6 py-4 text-right">1h %</th>
                        <th class="px-6 py-4 text-right">24h %</th>
                        <th class="px-6 py-4 text-right">7d %</th>
                        <th class="px-6 py-4 text-right">Market Cap</th>
                        <th class="px-6 py-4 text-right">Volume(24h)</th>
                        <th class="px-6 py-4 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody id="tableBody" class="divide-y divide-gray-800"></tbody>
            </table>
        </div>
    </div>

    <!-- Modal -->
    <div class="fixed inset-0 hidden flex items-center justify-center bg-black/80 z-50" id="modal">
        <div class="bg-gray-900 rounded-2xl p-8 max-w-4xl w-full max-h-[90vh] overflow-y-auto shadow-2xl">
            <div class="flex justify-between items-center mb-6">
                <h2 id="modalTitle" class="text-3xl font-bold"></h2>
                <button class="text-4xl" onclick="document.getElementById('modal').classList.add('hidden')">&times;</button>
            </div>
            <canvas id="detailChart"></canvas>
        </div>
    </div>

    <script>
        let detailChart = null;

        function formatNumber(num) {
            if (!num) return '$0';
            if (num >= 1e9) return '$' + (num / 1e9).toFixed(2) + 'B';
            if (num >= 1e6) return '$' + (num / 1e6).toFixed(2) + 'M';
            return '$' + num.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 8});
        }

        function formatPercent(pct) {
            if (!pct) return '-';
            const cls = pct >= 0 ? 'text-green' : 'text-red';
            return `<span class="${cls}">${pct > 0 ? '+' : ''}${pct.toFixed(2)}%</span>`;
        }

        async function loadCoins() {
            const isTrending = window.location.pathname === '/trending';
            const endpoint = isTrending ? '/api/trending' : '/api/data';
            try {
                const res = await fetch(endpoint);
                const json = await res.json();
                const data = json.data || [];

                const tbody = document.getElementById('tableBody');
                tbody.innerHTML = '';

                data.forEach(coin => {
                    const tr = document.createElement('tr');
                    tr.className = 'cursor-pointer hover:bg-gray-800';
                    tr.onclick = () => openModal(coin.id);

                    const pricesJson = JSON.stringify(coin.sparkline_prices || []);

                    tr.innerHTML = `
                        <td class="px-6 py-4 text-gray-400">${coin.rank}</td>
                        <td class="px-6 py-4">
                            <div class="flex items-center gap-4">
                                <img src="${coin.logo}" class="w-10 h-10 rounded-full">
                                <div>
                                    <div class="font-bold">${coin.name}</div>
                                    <div class="text-gray-500">${coin.symbol}</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-4 text-right font-bold">${formatNumber(coin.price)}</td>
                        <td class="px-6 py-4 text-right">${formatPercent(coin.change_1h)}</td>
                        <td class="px-6 py-4 text-right">${formatPercent(coin.change_24h)}</td>
                        <td class="px-6 py-4 text-right">${formatPercent(coin.change_7d)}</td>
                        <td class="px-6 py-4 text-right text-gray-400">${formatNumber(coin.market_cap)}</td>
                        <td class="px-6 py-4 text-right text-gray-400">${formatNumber(coin.volume_24h)}</td>
                        <td class="px-6 py-4 text-center"><canvas class="sparkline" data-prices="${pricesJson}"></canvas></td>
                    `;
                    tbody.appendChild(tr);
                });

                document.querySelectorAll('.sparkline').forEach(canvas => {
                    let prices = [];
                    try { prices = JSON.parse(canvas.dataset.prices); } catch(e) {}
                    if (prices.length < 2) return;
                    const up = prices[prices.length - 1] >= prices[0];
                    new Chart(canvas, {
                        type: 'line',
                        data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
                        options: { responsive: true, scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
                    });
                });
            } catch (e) { console.error(e); }
        }

        async function openModal(id) {
            document.getElementById('modalTitle').textContent = 'Loading...';
            document.getElementById('modal').classList.remove('hidden');
            try {
                const res = await fetch(`/api/coin_ohlc/${id}`);
                const raw = await res.json();
                const candles = raw.map(d => ({ x: d[0], o: d[1], h: d[2], l: d[3], c: d[4] }));

                if (detailChart) detailChart.destroy();
                detailChart = new Chart(document.getElementById('detailChart'), {
                    type: 'candlestick',
                    data: { datasets: [{ data: candles }] },
                    options: { responsive: true }
                });
            } catch (e) { console.error(e); }
        }

        document.getElementById('themeToggle').addEventListener('click', () => {
            const root = document.documentElement;
            const current = root.getAttribute('data-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            root.setAttribute('data-theme', newTheme);
            document.getElementById('themeToggle').textContent = newTheme === 'dark' ? '🌙' : '☀️';
        });

        loadCoins();
        setInterval(loadCoins, 60000);
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
