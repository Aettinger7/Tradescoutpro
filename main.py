from flask import Flask, render_template_string, jsonify
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"  # Your Pro key for higher limits

def format_number(num):
    if not num or num == 0:
        return "N/A"
    if num >= 1e12:
        return f"${num / 1e12:.2f}T"
    if num >= 1e9:
        return f"${num / 1e9:.2f}B"
    if num >= 1e6:
        return f"${num / 1e6:.2f}M"
    return f"${num:,.2f}"

def format_supply(num, symbol):
    if not num:
        return "N/A"
    return f"{num:,.0f} {symbol}"

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
                "circulating_supply": coin.get("circulating_supply") or 0,
                "sparkline_prices": sparkline_prices,
            })

        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update

    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def fetch_trending_data():
    url = "https://api.coingecko.com/api/v3/search/trending"
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()

        formatted_data = []
        for rank, item in enumerate(data.get("coins", [])[:25], 1):
            coin = item["item"]
            formatted_data.append({
                "rank": rank,
                "id": coin["id"],
                "name": coin["name"],
                "symbol": coin["symbol"].upper(),
                "logo": coin["thumb"],
                "price": coin["data"]["price"] or 0,
                "change_24h": round(coin["data"]["price_change_percentage_24h"]["usd"] or 0, 2),
                "market_cap": coin["market_cap_rank"] or "N/A",  # Trending doesn't have full data, use rank as proxy
                "volume_24h": "N/A",  # Not available in trending
                "circulating_supply": "N/A",
                "sparkline_prices": [],  # No sparkline in trending, can fetch separately if needed
            })

        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update

    except Exception as e:
        print(f"Error fetching trending data: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

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

@app.route('/api/coin/<id>')
def coin_detail(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}"
    params = {"localization": "false", "tickers": "false", "market_data": "true", "community_data": "false", "developer_data": "false"}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/coin_chart/<id>')
def coin_chart(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
    params = {"vs_currency": "usd", "days": "30", "interval": "daily"}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro — {{ title }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> <!-- For sparklines and detail chart -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: { extend: { fontFamily: { sans: ['Inter', 'sans-serif'] } }}
        }
    </script>
    <style>
        body { font-family: 'Inter', sans-serif; transition: background-color 0.3s, color 0.3s; }
        .theme-dark { background-color: #121212; color: #e0e0e0; }
        .theme-dark .table { background-color: #1e1e1e; }
        .theme-dark .table-hover tbody tr:hover { background-color: #2d2d2d; }
        .coin-logo { width: 32px; height: 32px; margin-right: 10px; }
        .sparkline { width: 120px; height: 50px; }
        .change-positive { color: #00c853; }
        .change-negative { color: #ff1744; }
        .navbar { background-color: #1976d2; } /* Coinbase blue */
        .search-input { max-width: 300px; }
        .table-hover tbody tr:hover { background-color: #f3f4f6; } /* Light hover for light mode */
        .theme-dark .table-hover tbody tr:hover { background-color: #2d2d2d; } /* Dark hover for dark mode */
    </style>
</head>
<body class="theme-dark">
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand fw-bold" href="/">TradeScout Pro</a>
            <div class="d-flex align-items-center">
                <input type="text" id="searchInput" class="form-control me-3 search-input" placeholder="Search coin...">
                <button id="themeToggle" class="btn btn-outline-light"><i class="fas fa-moon"></i></button>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        <h2 class="text-center mb-4">{{ title }}</h2>
        <div class="table-responsive">
            <table id="coinsTable" class="table table-hover align-middle">
                <thead class="table-light">
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Price</th>
                        <th>1h %</th>
                        <th>24h %</th>
                        <th>7d %</th>
                        <th>24h Volume</th>
                        <th>Market Cap</th>
                        <th>Last 7 Days</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </div>
        <p class="text-center text-muted mt-3">Data refreshes every 60 seconds • Powered by CoinGecko API</p>
    </div>

    <!-- Modal for detailed chart -->
    <div class="modal fade" id="chartModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content theme-dark">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalTitle"></h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <canvas id="detailChart"></canvas>
                </div>
            </div>
        </div>
    </div>

    <script>
        let table;
        let detailChart;

        function formatNumber(num) {
            if (num >= 1e9) return '$' + (num / 1e9).toFixed(2) + 'B';
            if (num >= 1e6) return '$' + (num / 1e6).toFixed(2) + 'M';
            return '$' + num.toFixed(2);
        }

        function formatPercent(pct) {
            if (pct === null || pct === undefined) return '-';
            const cls = pct >= 0 ? 'change-positive' : 'change-negative';
            return `<span class="${cls}">${pct.toFixed(2)}%</span>`;
        }

        async function loadCoins() {
            const endpoint = '{{ ' /api/trending ' if is_trending else ' /api/data ' }}';
            const res = await fetch(endpoint);
            const { data } = await res.json();

            const tbody = document.querySelector('#tableBody');
            tbody.innerHTML = '';

            data.forEach(coin => {
                const row = `
                    <tr style="cursor: pointer;" onclick="openModal('${coin.id}', '${coin.name}', '${coin.symbol}')">
                        <td>${coin.rank}</td>
                        <td><img src="${coin.logo}" class="coin-logo rounded-circle"> ${coin.name} <small class="text-muted">${coin.symbol}</small></td>
                        <td>$${coin.price.toLocaleString()}</td>
                        <td>${formatPercent(coin.change_1h)}</td>
                        <td>${formatPercent(coin.change_24h)}</td>
                        <td>${formatPercent(coin.change_7d)}</td>
                        <td>${formatNumber(coin.volume_24h)}</td>
                        <td>${formatNumber(coin.market_cap)}</td>
                        <td><canvas class="sparkline" data-prices="${coin.sparkline_prices}"></canvas></td>
                    </tr>`;
                tbody.insertAdjacentHTML('beforeend', row);
            });

            // Render sparklines
            document.querySelectorAll('.sparkline').forEach(canvas => {
                const prices = JSON.parse(canvas.dataset.prices || '[]');
                if (prices.length === 0) return;
                const isUp = prices[prices.length - 1] >= prices[0];
                new Chart(canvas, {
                    type: 'line',
                    data: { datasets: [{ data: prices, borderColor: isUp ? '#00c853' : '#ff1744', tension: 0.4, pointRadius: 0, fill: false }] },
                    options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } }, maintainAspectRatio: false }
                });
            });
        }

        async function openModal(id, name, symbol) {
            document.getElementById('modalTitle').textContent = `${name} (${symbol.toUpperCase()}) Price Chart`;
            const hist = await fetch(`/api/coin_chart/${id}`).then(r => r.json());
            const labels = hist.prices.map(p => new Date(p[0]).toLocaleDateString());
            const data = hist.prices.map(p => p[1]);

            if (detailChart) detailChart.destroy();
            detailChart = new Chart(document.getElementById('detailChart'), {
                type: 'line',
                data: { labels: labels, datasets: [{ label: 'Price (USD)', data: data, borderColor: '#1976d2', tension: 0.3 }] },
                options: { responsive: true, scales: { x: { ticks: { maxTicksLimit: 10 } } } }
            });

            new bootstrap.Modal(document.getElementById('chartModal')).show();
        }

        // Search filter
        document.getElementById('searchInput').addEventListener('input', () => {
            const term = searchInput.value.toLowerCase();
            rows.forEach(row => {
                row.style.display = row.textContent.toLowerCase().includes(term) ? '' : 'none';
            });
        });

        // Theme toggle
        document.getElementById('themeToggle').addEventListener('click', () => {
            document.body.classList.toggle('theme-dark');
            this.innerHTML = document.body.classList.contains('theme-dark') ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
        });

        // Initial load & auto-refresh
        loadCoins();
        setInterval(loadCoins, 60000);
    </script>
</body>
</html>
'''
