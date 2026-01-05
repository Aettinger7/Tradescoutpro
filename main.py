from flask import Flask, render_template_string, jsonify, request
import requests
import datetime
import json

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

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
            "fear_greed": 26,  # Current from feargreedmeter.com
            "alt_season": 22,  # Current from CoinNess
        }
    except Exception as e:
        print(f"Metrics error: {e}")
        return {
            "total_market_cap": 3120000000000,
            "btc_dominance": 58.4,
            "fear_greed": 26,
            "alt_season": 22,
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
        formatted_data = []
        for rank, coin in enumerate(data, 1):
            sparkline_prices = coin.get("sparkline_in_7d", {}).get("price", [])
            formatted_data.append({
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
                "sparkline_prices": sparkline_prices,
            })
        return formatted_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def fetch_trending_data():
    try:
        trending_url = "https://api.coingecko.com/api/v3/search/trending"
        headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
        trending_res = requests.get(trending_url, headers=headers, timeout=15)
        trending_res.raise_for_status()
        trending_json = trending_res.json()
        trending_items = trending_json.get('coins', [])
        ids = [item['item']['id'] for item in trending_items]

        if len(ids) < 25:
            top_gainers_url = "https://api.coingecko.com/api/v3/coins/markets"
            top_gainers_params = {
                "vs_currency": "usd",
                "order": "price_change_percentage_24h_desc",
                "per_page": 25 - len(ids),
                "page": 1,
                "sparkline": True,
                "price_change_percentage": "1h,24h,7d",
            }
            top_gainers_res = requests.get(top_gainers_url, params=top_gainers_params, headers=headers, timeout=15)
            top_gainers_res.raise_for_status()
            top_gainers = top_gainers_res.json()
            ids.extend([coin['id'] for coin in top_gainers if coin['id'] not in ids])

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

            formatted_data = []
            for rank, coin in enumerate(full_data[:25], 1):
                sparkline_prices = coin.get("sparkline_in_7d", {}).get("price", [])
                formatted_data.append({
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
                    "sparkline_prices": sparkline_prices,
                })
            return formatted_data
    except Exception as e:
        print(f"Trending error: {e}")
        return fetch_crypto_data()

@app.route('/')
def index():
    metrics = get_global_metrics()
    data = fetch_crypto_data()
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, data=data, last_update=last_update, metrics=metrics, title="Top 100 Cryptocurrencies", page="top")

@app.route('/trending')
def trending():
    metrics = get_global_metrics()
    data = fetch_trending_data()
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, data=data, last_update=last_update, metrics=metrics, title="Top 25 Trending Coins", page="trending")

@app.route('/api/coin_ohlc/<id>')
def coin_ohlc(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}/ohlc"
    params = {"vs_currency": "usd", "days": "30"}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro — {{ title }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-chart-financial"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body { background-color: #000; color: #fff; font-family: 'Inter', sans-serif; transition: background 0.3s, color 0.3s; }
        .logo-font { font-family: 'Orbitron', sans-serif; }
        .text-green { color: #00ff99; }
        .text-red { color: #ff4444; }
        .hover-row:hover { background-color: #111 !important; }
        .sparkline { height: 60px; width: 140px; }
        .navbar-blue { background-color: #0066ff; transition: background 0.3s; }
        .active-link { color: #00ff99; border-bottom: 3px solid #00ff99; padding-bottom: 4px; }
        [data-theme="light"] { background-color: #f8f9fa; color: #000; }
        [data-theme="light"] .navbar-blue { background-color: #005edc; }
        [data-theme="light"] .hover-row:hover { background-color: #e9ecef !important; }
        [data-theme="light"] .text-green { color: #00aa66; }
        [data-theme="light"] .text-red { color: #cc3333; }
        [data-theme="light"] .bg-gray-900 { background-color: #fff; }
        [data-theme="light"] .bg-gray-800 { background-color: #e5e7eb; }
    </style>
</head>
<body class="min-h-screen">
    <nav class="navbar-blue text-white py-5 px-8 flex justify-between items-center sticky top-0 z-50 shadow-xl">
        <a href="/" class="text-4xl font-bold logo-font flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12 rounded-lg">
            TradeScout Pro
        </a>
        <div class="flex items-center gap-10 text-lg">
            <a href="/" class="hover:text-cyan-300 {% if page == 'top' %}active-link{% endif %}">Top 100</a>
            <a href="/trending" class="hover:text-cyan-300 {% if page == 'trending' %}active-link{% endif %}">Trending</a>
            <div class="relative">
                <input type="text" id="searchInput" class="px-6 py-3 rounded-full bg-black/50 text-white placeholder-gray-400 border border-gray-600 focus:outline-none focus:border-cyan-400 w-96" placeholder="Search any crypto...">
                <div id="searchDropdown" class="absolute hidden bg-gray-900 border border-gray-700 rounded-lg shadow-xl mt-2 w-full z-50">
                    <div id="searchResults" class="max-h-96 overflow-y-auto"></div>
                </div>
            </div>
            <button id="themeToggle" class="text-3xl">🌙</button>
        </div>
    </nav>

    <div class="container mx-auto px-6 py-10 max-w-7xl">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm mb-2">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.0f}".format(metrics.total_market_cap / 1e12) }}T</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm mb-2">Fear & Greed Index</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-sm text-gray-400">Fear</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm mb-2">Altcoin Season Index</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}/100</p>
                <p class="text-sm text-gray-400">Bitcoin Season</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm mb-2">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ metrics.btc_dominance }}%</p>
            </div>
        </div>

        <div class="overflow-x-auto rounded-2xl shadow-2xl bg-gray-900/50">
            <table class="w-full text-left">
                <thead class="bg-gray-800/80 text-gray-300 uppercase text-sm">
                    <tr>
                        <th class="px-6 py-5">#</th>
                        <th class="px-6 py-5">Name</th>
                        <th class="px-6 py-5 text-right">Price</th>
                        <th class="px-6 py-5 text-right">1h %</th>
                        <th class="px-6 py-5 text-right">24h %</th>
                        <th class="px-6 py-5 text-right">7d %</th>
                        <th class="px-6 py-5 text-right">24h Volume</th>
                        <th class="px-6 py-5 text-right">Market Cap</th>
                        <th class="px-6 py-5 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody id="tableBody" class="divide-y divide-gray-800"></tbody>
            </table>
        </div>
        
        <p class="text-center text-gray-500 mt-8 text-sm">Last update: <span id="lastUpdate">{{ last_update }}</span> • Auto-refreshes every 60s • Powered by CoinGecko</p>
    </div>

    <!-- Modal -->
    <div class="fixed inset-0 hidden items-center justify-center bg-black/80 z-50" id="modal">
        <div class="bg-gray-900 rounded-2xl p-8 max-w-4xl w-full max-h-[90vh] overflow-y-auto shadow-2xl">
            <span class="close" onclick="document.getElementById('modal').classList.add('hidden')">&times;</span>
            <div id="modal-body"></div>
        </div>
    </div>

    <script>
        let detailChart = null;

        async function loadCoins() {
            try {
                const endpoint = window.location.pathname === '/trending' ? '/api/trending' : '/api/data';
                const res = await fetch(endpoint);
                const json = await res.json();
                const data = json.data || [];

                const tbody = document.getElementById('tableBody');
                tbody.innerHTML = '';

                data.forEach(coin => {
                    const tr = document.createElement('tr');
                    tr.className = 'hover-row cursor-pointer';
                    tr.onclick = () => openModal(coin.id);

                    const pricesJson = JSON.stringify(coin.sparkline_prices || []);

                    tr.innerHTML = `
                        <td class="px-6 py-5 text-gray-400">${coin.rank}</td>
                        <td class="px-6 py-5">
                            <div class="flex items-center gap-4">
                                <img src="${coin.logo}" class="w-10 h-10 rounded-full">
                                <div>
                                    <div class="font-bold text-lg">${coin.name}</div>
                                    <div class="text-gray-500">${coin.symbol}</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-5 text-right font-bold text-xl">${formatNumber(coin.price)}</td>
                        <td class="px-6 py-5 text-right">${formatPercent(coin.change_1h)}</td>
                        <td class="px-6 py-5 text-right">${formatPercent(coin.change_24h)}</td>
                        <td class="px-6 py-5 text-right">${formatPercent(coin.change_7d)}</td>
                        <td class="px-6 py-5 text-right text-gray-400">${formatNumber(coin.volume_24h)}</td>
                        <td class="px-6 py-5 text-right text-gray-400">${formatNumber(coin.market_cap)}</td>
                        <td class="px-6 py-5 text-center"><canvas class="sparkline" data-prices='${pricesJson}'></canvas></td>
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
                        data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, fill: false, borderWidth: 2.5 }] },
                        options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
                    });
                });

                document.getElementById('lastUpdate').textContent = json.last_update;
            } catch (e) {
                console.error(e);
                document.getElementById('tableBody').innerHTML = '<tr><td colspan="9" class="text-center text-red-500">Failed to load data. Try refreshing.</td></tr>';
            }
        }

        function openModal(id) {
            document.getElementById('modal').classList.remove('hidden');
            const modalBody = document.getElementById('modal-body');
            modalBody.innerHTML = '<p>Loading...</p>';
            fetch(`/api/coin/${id}`)
                .then(res => res.json())
                .then(json => {
                    const detail = json.detail;
                    const chart = json.chart;
                    modalBody.innerHTML = `
                        <h2>${detail.name} (${detail.symbol.toUpperCase()})</h2>
                        <p>Price: $${detail.market_data.current_price.usd.toLocaleString()}</p>
                        <p>Market Cap: $${detail.market_data.market_cap.usd.toLocaleString()}</p>
                        <p>24h Volume: $${detail.market_data.total_volume.usd.toLocaleString()}</p>
                        <canvas id="modal-chart"></canvas>
                    `;
                    const labels = chart.map(p => new Date(p[0]).toLocaleDateString());
                    const prices = chart.map(p => p[1]);
                    new Chart(document.getElementById('modal-chart'), {
                        type: 'line',
                        data: { labels, datasets: [{ label: 'Price (USD)', data: prices, borderColor: '#0066ff', tension: 0.3 }] },
                        options: { responsive: true }
                    });
                });
        }

        function formatNumber(num) {
            if (!num) return '$0';
            if (num >= 1e9) return '$' + (num / 1e9).toFixed(2) + 'B';
            if (num >= 1e6) return '$' + (num / 1e6).toFixed(2) + 'M';
            return '$' + num.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 6});
        }

        function formatPercent(pct) {
            if (pct === null || pct === undefined || pct === 0) return '-';
            const cls = pct >= 0 ? 'text-green' : 'text-red';
            return `<span class="${cls}">${pct > 0 ? '+' : ''}${pct.toFixed(2)}%</span>`;
        }

        document.getElementById('themeToggle').addEventListener('click', () => {
            document.documentElement.setAttribute('data-theme', document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
            document.getElementById('themeToggle').textContent = document.documentElement.getAttribute('data-theme') === 'dark' ? '🌙' : '☀️';
        });

        loadCoins();
        setInterval(loadCoins, 60000);
    </script>
</body>
</html>
''' 

application = app

if __name__ == '__main__':
    app.run(debug=True)
