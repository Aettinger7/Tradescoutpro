from flask import Flask, render_template_string, jsonify, request
import requests
import datetime
import json

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

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

        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update

    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], "Error"

def fetch_trending_data():
    try:
        trending_url = "https://api.coingecko.com/api/v3/search/trending"
        headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
        trending_res = requests.get(trending_url, headers=headers, timeout=15)
        trending_res.raise_for_status()
        trending_json = trending_res.json()
        trending_items = trending_json.get('coins', [])
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

            # Preserve trending order
            order_map = {item['item']['id']: idx for idx, item in enumerate(trending_items)}
            full_data.sort(key=lambda c: order_map.get(c['id'], 999))

            formatted_data = []
            for rank, coin in enumerate(full_data, 1):
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
            last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
            return formatted_data, last_update
    except Exception as e:
        print(f"Trending error: {e}")

    return fetch_crypto_data()

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=crypto_data, last_update=last_update, title="Top 100 Cryptocurrencies", page="top")

@app.route('/trending')
def trending():
    trending_data, last_update = fetch_trending_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=trending_data, last_update=last_update, title="Trending Coins", page="trending")

@app.route('/api/data')
def api_data():
    crypto_data, last_update = fetch_crypto_data()
    return jsonify({"data": crypto_data, "last_update": last_update})

@app.route('/api/trending')
def api_trending():
    trending_data, last_update = fetch_trending_data()
    return jsonify({"data": trending_data, "last_update": last_update})

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({"results": []})
    url = "https://api.coingecko.com/api/v3/search"
    params = {"query": query}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        search_data = response.json().get('coins', [])[:20]
        results = []
        for item in search_data:
            results.append({
                "id": item['id'],
                "name": item['name'],
                "symbol": item['symbol'].upper(),
                "logo": item.get('large') or item.get('thumb') or '',
            })
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"results": [], "error": str(e)})

@app.route('/api/coin_detail/<id>')
def coin_detail(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}"
    params = {"localization": False, "tickers": False, "market_data": True, "community_data": False, "developer_data": False, "sparkline": False}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        return jsonify(response.json())
    except:
        return jsonify({}), 500

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
        [data-theme="dark"] {
            --bg: #000000;
            --text: #ffffff;
            --table-bg: #111111;
            --table-header: #1e1e1e;
            --hover: #222222;
            --border: #333333;
            --green: #00ff99;
            --red: #ff4444;
        }
        [data-theme="light"] {
            --bg: #ffffff;
            --text: #000000;
            --table-bg: #f8f9fa;
            --table-header: #e9ecef;
            --hover: #e9ecef;
            --border: #dee2e6;
            --green: #00aa66;
            --red: #cc3333;
        }
        body { background-color: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; transition: background 0.3s, color 0.3s; }
        .logo-font { font-family: 'Orbitron', sans-serif; }
        .text-green { color: var(--green); }
        .text-red { color: var(--red); }
        .hover-row:hover { background-color: var(--hover) !important; }
        .sparkline { height: 60px; width: 140px; }
        .navbar-blue { background-color: #0066ff; }
        .active-link { color: #00ff99; border-bottom: 3px solid #00ff99; padding-bottom: 4px; }
        table { background-color: var(--table-bg); }
        thead { background-color: var(--table-header); color: var(--text); }
        .divide-y > tr { border-bottom: 1px solid var(--border); }
    </style>
</head>
<body class="min-h-screen">
    <nav class="navbar-blue text-white py-5 px-8 flex justify-between items-center sticky top-0 z-50 shadow-xl">
        <a href="/" class="text-4xl font-bold logo-font flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="TradeScout Pro Logo" class="w-12 h-12 rounded-lg">
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
        <h1 class="text-4xl font-bold text-center mb-10 logo-font">{{ title }}</h1>
        
        <div class="overflow-x-auto rounded-2xl shadow-2xl">
            <table class="w-full text-left">
                <thead class="text-gray-300 uppercase text-sm">
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
                <tbody id="tableBody" class="divide-y"></tbody>
            </table>
        </div>
        
        <p class="text-center text-gray-500 mt-8 text-sm">Last update: <span id="lastUpdate">{{ last_update }}</span> • Auto-refreshes every 60s • Powered by CoinGecko</p>
    </div>

    <!-- Modal -->
    <div class="fixed inset-0 hidden flex items-center justify-center bg-black/90 z-50" id="modal">
        <div class="bg-current rounded-2xl p-8 max-w-4xl w-full max-h-[90vh] overflow-y-auto shadow-2xl mx-4" style="background-color: var(--table-bg);">
            <div class="flex justify-between items-start mb-6">
                <div class="flex items-center gap-4">
                    <img id="modalLogo" src="" class="w-16 h-16 rounded-full">
                    <div>
                        <h2 id="modalName" class="text-3xl font-bold logo-font"></h2>
                        <p id="modalSymbol" class="text-xl text-gray-400"></p>
                    </div>
                </div>
                <button onclick="document.getElementById('modal').classList.add('hidden')" class="text-4xl text-gray-400 hover:text-white">&times;</button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8 text-lg">
                <div><strong>Current Price:</strong> <span id="modalPrice" class="font-bold text-2xl"></span></div>
                <div><strong>Market Cap:</strong> <span id="modalMarketCap"></span></div>
                <div><strong>24h Volume:</strong> <span id="modalVolume"></span></div>
                <div><strong>24h Change:</strong> <span id="modalChange24h"></span></div>
            </div>
            <h3 class="text-2xl font-bold mb-4">30 Day Candlestick Chart</h3>
            <div class="bg-gray-800 rounded-lg p-4">
                <canvas id="detailChart"></canvas>
            </div>
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
            const color = pct >= 0 ? 'text-green' : 'text-red';
            return `<span class="${color}">${pct > 0 ? '+' : ''}${pct.toFixed(2)}%</span>`;
        }

        async function loadCoins() {
            try {
                const endpoint = "{{ '/api/trending' if page == 'trending' else '/api/data' }}";
                const res = await fetch(endpoint);
                if (!res.ok) throw new Error("Failed");
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
                        <td class="px-6 py-5 text-center"><canvas class="sparkline" data-prices="${pricesJson}"></canvas></td>
                    `;
                    tbody.appendChild(tr);
                });

                // Render sparklines
                document.querySelectorAll('.sparkline').forEach(canvas => {
                    let prices = [];
                    try { prices = JSON.parse(canvas.dataset.prices); } catch(e) {}
                    if (prices.length < 2) return;
                    const up = prices[prices.length - 1] >= prices[0];
                    new Chart(canvas, {
                        type: 'line',
                        data: { datasets: [{ data: prices, borderColor: up ? 'var(--green)' : 'var(--red)', tension: 0.4, pointRadius: 0, borderWidth: 2.5 }] },
                        options: { responsive: true, scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
                    });
                });

                document.getElementById('lastUpdate').textContent = json.last_update;
            } catch (e) {
                console.error(e);
            }
        }

        async function openModal(id) {
            // Same as before...
            try {
                const detailRes = await fetch(`/api/coin_detail/${id}`);
                const detail = await detailRes.json();
                const md = detail.market_data || {};

                document.getElementById('modalLogo').src = detail.image?.large || '';
                document.getElementById('modalName').textContent = detail.name || '';
                document.getElementById('modalSymbol').textContent = detail.symbol?.toUpperCase() || '';
                document.getElementById('modalPrice').textContent = formatNumber(md.current_price?.usd);
                document.getElementById('modalMarketCap').textContent = formatNumber(md.market_cap?.usd);
                document.getElementById('modalVolume').textContent = formatNumber(md.total_volume?.usd);
                document.getElementById('modalChange24h').innerHTML = formatPercent(md.price_change_percentage_24h);
            } catch(e) {}

            try {
                const ohlcRes = await fetch(`/api/coin_ohlc/${id}`);
                const raw = await ohlcRes.json();
                const candles = raw.map(d => ({ x: d[0], o: d[1], h: d[2], l: d[3], c: d[4] }));

                if (detailChart) detailChart.destroy();
                detailChart = new Chart(document.getElementById('detailChart'), {
                    type: 'candlestick',
                    data: { datasets: [{ label: detail.symbol?.toUpperCase() + '/USD', data: candles }] },
                    options: { responsive: true }
                });
            } catch (e) { console.error(e); }

            document.getElementById('modal').classList.remove('hidden');
        }

        // Search fixed with debug
        let searchTimeout;
        const searchInput = document.getElementById('searchInput');
        const dropdown = document.getElementById('searchDropdown');
        const resultsDiv = document.getElementById('searchResults');

        searchInput.addEventListener('input', () => {
            clearTimeout(searchTimeout);
            const q = searchInput.value.trim();
            dropdown.classList.add('hidden');
            if (q.length < 2) return;

            searchTimeout = setTimeout(async () => {
                try {
                    const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
                    console.log("Search response status:", res.status);
                    const json = await res.json();
                    console.log("Search results:", json);
                    const results = json.results || [];

                    resultsDiv.innerHTML = '';
                    if (results.length === 0) {
                        resultsDiv.innerHTML = '<div class="p-4 text-gray-500">No results</div>';
                    } else {
                        results.forEach(coin => {
                            const div = document.createElement('div');
                            div.className = 'p-4 hover:bg-gray-700 cursor-pointer flex items-center gap-4';
                            div.onclick = () => {
                                openModal(coin.id);
                                searchInput.value = '';
                                dropdown.classList.add('hidden');
                            };
                            div.innerHTML = `
                                <img src="${coin.logo || ''}" class="w-10 h-10 rounded-full">
                                <div>
                                    <div class="font-semibold">${coin.name}</div>
                                    <div class="text-sm text-gray-500">${coin.symbol}</div>
                                </div>
                            `;
                            resultsDiv.appendChild(div);
                        });
                    }
                    dropdown.classList.remove('hidden');
                } catch (e) {
                    console.error("Search error:", e);
                }
            }, 300);
        });

        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
                dropdown.classList.add('hidden');
            }
        });

        document.getElementById('themeToggle').addEventListener('click', () => {
            const html = document.documentElement;
            const current = html.getAttribute('data-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
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
