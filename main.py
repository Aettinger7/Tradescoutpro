from flask import Flask, render_template_string, jsonify
import requests
import datetime

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
    return fetch_crypto_data()

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=crypto_data, last_update=last_update, title="Top 100 Cryptocurrencies", is_trending=False)

@app.route('/trending')
def trending():
    trending_data, last_update = fetch_trending_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=trending_data, last_update=last_update, title="Top 25 Trending Coins", is_trending=True)

@app.route('/api/data')
def api_data():
    crypto_data, last_update = fetch_crypto_data()
    return jsonify({"data": crypto_data, "last_update": last_update})

@app.route('/api/trending')
def api_trending():
    trending_data, last_update = fetch_trending_data()
    return jsonify({"data": trending_data, "last_update": last_update})

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

application = app  # For Render/Gunicorn

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
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
    <style>
        body { background-color: #000; color: #fff; font-family: 'Inter', system-ui, sans-serif; }
        .bg-dark { background-color: #000; }
        .text-green { color: #00ff99; }
        .text-red { color: #ff4444; }
        .hover-row:hover { background-color: #111 !important; }
        .sparkline { height: 60px; width: 140px; }
        .navbar-blue { background-color: #0066ff; }
    </style>
</head>
<body class="bg-dark min-h-screen">
    <nav class="navbar-blue text-white py-4 px-6 flex justify-between items-center sticky top-0 z-50 shadow-lg">
        <a href="/" class="text-2xl font-bold">TradeScout Pro</a>
        <div class="flex items-center gap-6">
            <input type="text" id="searchInput" class="px-4 py-2 rounded-lg bg-black/50 text-white placeholder-gray-400 border border-gray-700 focus:outline-none focus:border-blue-400" placeholder="Search coin...">
            <button id="themeToggle" class="text-2xl">🌙</button>
        </div>
    </nav>

    <div class="container mx-auto px-4 py-8 max-w-7xl">
        <h1 class="text-3xl font-bold text-center mb-8">{{ title }}</h1>
        
        <div class="overflow-x-auto rounded-xl shadow-2xl">
            <table class="w-full text-left">
                <thead class="bg-gray-900 text-gray-400 uppercase text-xs">
                    <tr>
                        <th class="px-6 py-4">#</th>
                        <th class="px-6 py-4">Name</th>
                        <th class="px-6 py-4 text-right">Price</th>
                        <th class="px-6 py-4 text-right">1h %</th>
                        <th class="px-6 py-4 text-right">24h %</th>
                        <th class="px-6 py-4 text-right">7d %</th>
                        <th class="px-6 py-4 text-right">24h Volume</th>
                        <th class="px-6 py-4 text-right">Market Cap</th>
                        <th class="px-6 py-4 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody id="tableBody" class="divide-y divide-gray-800"></tbody>
            </table>
        </div>
        
        <p class="text-center text-gray-500 mt-6 text-sm">Last update: <span id="lastUpdate">{{ last_update }}</span> • Auto-refreshes every 60s • Powered by CoinGecko</p>
    </div>

    <div class="fixed inset-0 hidden items-center justify-center bg-black/80 z-50" id="modal">
        <div class="bg-gray-900 rounded-2xl p-8 max-w-4xl w-full mx-4 shadow-2xl">
            <div class="flex justify-between items-center mb-6">
                <h2 id="modalTitle" class="text-2xl font-bold"></h2>
                <button onclick="document.getElementById('modal').classList.add('hidden')" class="text-3xl text-gray-400 hover:text-white">&times;</button>
            </div>
            <canvas id="detailChart" height="400"></canvas>
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
                const endpoint = "{{ '/api/trending' if is_trending else '/api/data' }}";
                const res = await fetch(endpoint);
                if (!res.ok) throw new Error("Failed");
                const json = await res.json();
                const data = json.data || [];

                const tbody = document.getElementById('tableBody');
                tbody.innerHTML = '';

                data.forEach(coin => {
                    const tr = document.createElement('tr');
                    tr.className = 'hover-row cursor-pointer';
                    tr.onclick = () => openModal(coin.id, coin.name, coin.symbol);

                    tr.innerHTML = `
                        <td class="px-6 py-4 text-gray-400">${coin.rank}</td>
                        <td class="px-6 py-4">
                            <div class="flex items-center gap-3">
                                <img src="${coin.logo}" class="w-8 h-8 rounded-full">
                                <div>
                                    <div class="font-semibold">${coin.name}</div>
                                    <div class="text-gray-500 text-sm">${coin.symbol}</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-4 text-right font-medium">${formatNumber(coin.price)}</td>
                        <td class="px-6 py-4 text-right">${formatPercent(coin.change_1h)}</td>
                        <td class="px-6 py-4 text-right">${formatPercent(coin.change_24h)}</td>
                        <td class="px-6 py-4 text-right">${formatPercent(coin.change_7d)}</td>
                        <td class="px-6 py-4 text-right text-gray-400">${formatNumber(coin.volume_24h)}</td>
                        <td class="px-6 py-4 text-right text-gray-400">${formatNumber(coin.market_cap)}</td>
                        <td class="px-6 py-4"><canvas class="sparkline" data-prices='${JSON.stringify(coin.sparkline_prices)}'></canvas></td>
                    `;
                    tbody.appendChild(tr);
                });

                // Render sparklines
                document.querySelectorAll('.sparkline').forEach(canvas => {
                    let prices = JSON.parse(canvas.dataset.prices || '[]');
                    if (prices.length < 2) return;
                    const up = prices[prices.length - 1] >= prices[0];
                    new Chart(canvas, {
                        type: 'line',
                        data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
                        options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
                    });
                });

                document.getElementById('lastUpdate').textContent = json.last_update;
            } catch (e) {
                console.error(e);
            }
        }

        async function openModal(id, name, symbol) {
            document.getElementById('modalTitle').textContent = `${name} (${symbol}) — 30 Day Candlesticks`;
            document.getElementById('modal').classList.remove('hidden');
            try {
                const res = await fetch(`/api/coin_ohlc/${id}`);
                const raw = await res.json();
                const candles = raw.map(d => ({ x: d[0], o: d[1], h: d[2], l: d[3], c: d[4] }));

                if (detailChart) detailChart.destroy();
                detailChart = new Chart(document.getElementById('detailChart'), {
                    type: 'candlestick',
                    data: { datasets: [{ label: `${symbol}/USD`, data: candles }] },
                    options: { responsive: true }
                });
            } catch (e) { console.error(e); }
        }

        document.getElementById('searchInput').addEventListener('input', e => {
            const term = e.target.value.toLowerCase();
            document.querySelectorAll('#tableBody tr').forEach(row => {
                row.style.display = row.textContent.toLowerCase().includes(term) ? '' : 'none';
            });
        });

        // Simple theme toggle (dark/light)
        document.getElementById('themeToggle').addEventListener('click', () => {
            document.body.classList.toggle('bg-dark');
            const isDark = document.body.classList.contains('bg-dark');
            document.getElementById('themeToggle').textContent = isDark ? '🌙' : '☀️';
            // Add light mode classes if needed later
        });

        loadCoins();
        setInterval(loadCoins, 60000);
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
