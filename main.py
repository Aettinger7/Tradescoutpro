from flask import Flask, render_template_string, jsonify
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu" # Keep your Pro key

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

 last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
 return formatted_data, last_update

 except Exception as e:
 print(f"Error fetching data: {e}")
 return [], "Error"

def fetch_trending_data():
 # We'll keep it simple and reuse top 100 for trending until we improve it
 return fetch_crypto_data() # Temporary - replace later if needed

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
 <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
 <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
 <script>
 tailwind.config = {
 darkMode: 'class',
 theme: { extend: { fontFamily : { sans: ['Inter', 'sans-serif'] } }}
 }
 </script>
 <style>
 body { font-family: 'Inter', sans-serif; transition: background-color 0.3s, color 0.3s; }
 .theme-dark { background-color: #121212; color: #e0e0e0; }
 .theme-dark .table { --bs-table-bg: #1e1e1e; }
 .theme-dark .table-hover tbody tr:hover { background-color: #2d2d2d !important; }
 .coin-logo { width: 32px; height: 32px; margin-right: 10px; }
 .sparkline { width: 120px; height: 50px; }
 .change-positive { color: #00c853; }
 .change-negative { color: #ff1744; }
 .navbar { background-color: #1976d2; }
 .search-input { max-width: 300px; }
 .table-hover tbody tr:hover { background-color: #f3f4f6; }
 .theme-dark .table-hover tbody tr:hover { background-color: #2d2d2d; }
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
 <tbody id="tableBody"></tbody> <!-- Added ID here -->
 </table>
 </div>
 <p class="text-center text-muted mt-3">Last update: <span id="lastUpdate">{{ last_update }}</span> • Data refreshes every 60 seconds • Powered by CoinGecko API</p>
 </div>

 <!-- Modal -->
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
 let detailChart = null;

 function formatNumber(num) {
 if (!num) return '$0';
 if (num >= 1e9) return '$' + (num / 1e9).toFixed(2) + 'B';
 if (num >= 1e6) return '$' + (num / 1e6).toFixed(2) + 'M';
 return '$' + num.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 6});
 }

 function formatPercent(pct) {
 if (pct === null || pct === undefined || pct === 0) return '-';
 const cls = pct >= 0 ? 'change-positive' : 'change-negative';
 return `<span class="${cls}">${pct > 0 ? '+' : ''}${pct.toFixed(2)}%</span>`;
 }

 async function loadCoins() {
 try {
 const endpoint = {{ '"/api/trending"' if is_trending else '"/api/data"' }};
 const res = await fetch(endpoint);
 if (!res.ok) throw new Error('Fetch failed');
 const json = await res.json();
 const data = json.data || [];

 const tbody = document.querySelector('#tableBody');
 tbody.innerHTML = '';

 data.forEach(coin => {
 const row = document.createElement('tr');
 row.style.cursor = 'pointer';
 row.onclick = () => openModal(coin.id, coin.name, coin.symbol);

 row.innerHTML = `
 <td>${coin.rank}</td>
 <td><img src="${coin.logo}" class="coin-logo rounded-circle" alt="${coin.name}"> ${coin.name} <small class="text-muted">${coin.symbol}</small></td>
 <td>${formatNumber(coin.price)}</td>
 <td>${formatPercent(coin.change_1h)}</td>
 <td>${formatPercent(coin.change_24h)}</td>
 <td>${formatPercent(coin.change_7d)}</td>
 <td>${formatNumber(coin.volume_24h)}</td>
 <td>${formatNumber(coin.market_cap)}</td>
 <td><canvas class="sparkline" data-prices='${JSON.stringify(coin.sparkline_prices)}'></canvas></td>
 `;
 tbody.appendChild(row);
 });

 // Render sparklines
 document.querySelectorAll('.sparkline').forEach(canvas => {
 let prices = [];
 try { prices = JSON.parse(canvas.dataset.prices); } catch(e) {}
 if (prices.length < 2) {
 canvas.parentElement.innerHTML = '<small>No data</small>';
 return;
 }
 const isUp = prices[prices.length - 1] >= prices[0];
 new Chart(canvas, {
 type: 'line',
 data: { datasets: [{ data: prices, borderColor: isUp ? '#00c853' : '#ff1744', tension: 0.4, pointRadius: 0, fill: false, borderWidth: 2 }] },
 options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } }, responsive: true, maintainAspectRatio: false }
 });
 });

 document.getElementById('lastUpdate').textContent = json.last_update || new Date().toUTCString();
 } catch (err) {
 console.error(err);
 document.querySelector('#tableBody').innerHTML = '<tr><td colspan="9" class="text-center text-danger">Error loading data. Check console.</td></tr>';
 }
 }

 async function openModal(id, name, symbol) {
 document.getElementById('modalTitle').textContent = `${name} (${symbol}) Price Chart (30d)`;
 try {
 const res = await fetch(`/api/coin_chart/${id}`);
 const hist = await res.json();
 const labels = hist.prices.map(p => new Date(p[0]).toLocaleDateString());
 const prices = hist.prices.map(p => p[1]);

 if (detailChart) detailChart.destroy();
 detailChart = new Chart(document.getElementById('detailChart'), {
 type: 'line',
 data: { labels, datasets: [{ label: 'Price (USD)', data: prices, borderColor: '#1976d2', backgroundColor: 'rgba(25,118,210,0.1)', tension: 0.3, fill: true }] },
 options: { responsive: true, scales: { x: { ticks: { maxTicksLimit: 8 } } } }
 });

 new bootstrap.Modal(document.getElementById('chartModal')).show();
 } catch (err) {
 alert('Error loading chart');
 }
 }

 // Search
 const searchInput = document.getElementById('searchInput');
 const tableRows = document.querySelectorAll('#coinsTable tbody tr');
 searchInput.addEventListener('input', () => {
 const term = searchInput.value .toLowerCase();
 document.querySelectorAll('#coinsTable tbody tr').forEach(row => {
 const text = row.textContent.toLowerCase();
 row.style.display = text.includes(term) ? '' : 'none';
 });
 });

 // Theme toggle
 document.getElementById('themeToggle').addEventListener('click', () => {
 document.body.classList.toggle('theme-dark');
 const icon = document.body.classList.contains('theme-dark') ? 'fa-moon' : 'fa-sun';
 document.querySelector('#themeToggle i').classList.replace('fa-moon', 'fa-sun');
 document.querySelector('#themeToggle i').classList.replace('fa-sun', 'fa-moon');
 document.querySelector('#themeToggle i').classList.toggle(icon);
 });

 // Load on start + refresh
 loadCoins();
 setInterval(loadCoins, 60000);
 </script>
</body>
</html>
'''
