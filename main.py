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
        "sparkline": True,  # This gets the 7-day price array
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
                "sparkline_prices": sparkline_prices,  # List of ~168 prices
            })

        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update

    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=crypto_data, last_update=last_update, format_number=format_number, format_supply=format_supply)

@app.route('/api/data')
def api_data():
    crypto_data, last_update = fetch_crypto_data()
    return jsonify({"data": crypto_data, "last_update": last_update})

@app.route('/api/coin/<id>')
def coin_detail(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}"
    params = {"localization": "false", "tickers": "false", "market_data": "true", "community_data": "false", "developer_data": "false", "sparkline": "false"}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print(f"Error fetching coin detail: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/coin_chart/<id>')
def coin_chart(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
    params = {"vs_currency": "usd", "days": "30", "interval": "daily"}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print(f"Error fetching coin chart: {e}")
        return jsonify({"error": str(e)}), 500

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro — Top 100 Cryptocurrencies</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> <!-- For sparklines and detail chart -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: { extend: { colors: { coinbase: '#0057ff', coinbase-dark: '#001f3f' }, fontFamily: { sans: ['Inter', 'sans-serif'] } } }
        }
    </script>
    <style>
        body { font-family: 'Inter', sans-serif; transition: background 0.3s, color 0.3s; }
        .dark body { background: linear-gradient(to bottom, #000000, #001f3f); color: #e6f1ff; }
        .navbar { transition: background 0.3s; }
        .dark .navbar { background: rgba(0, 31, 63, 0.95); border-bottom: 1px solid #0057ff; backdrop-filter: blur(10px); }
        .table-container { overflow-x: auto; -webkit-overflow-scrolling: touch; }
        .dark .table { background: rgba(0, 31, 63, 0.8); color: #e6f1ff; }
        .dark .table thead th { background: #001f3f; color: #93c5fd; border-bottom: 2px solid #0057ff; }
        .dark .table tbody tr:hover { background: rgba(0, 87, 255, 0.1); }
        .sparkline-canvas { height: 48px; width: 160px; }
        .modal-content { transition: background 0.3s, color 0.3s; }
        .dark .modal-content { background: #001f3f; color: #e6f1ff; border: 1px solid #0057ff; }
        .btn-close-white { filter: invert(1); }
        .change-positive { color: #00c853; }
        .change-negative { color: #ff1744; }
        .search-input { transition: background 0.3s, border 0.3s, color 0.3s; }
        .dark .search-input { background: #0f172a; border: 1px solid #0057ff; color: #e6f1ff; }
        .dark .search-input:focus { box-shadow: 0 0 0 3px rgba(0, 87, 255, 0.5); }
        ::-webkit-scrollbar { height: 8px; }
        ::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb { background: #c0c0c0; border-radius: 4px; }
        .dark ::-webkit-scrollbar-track { background: #001f3f; }
        .dark ::-webkit-scrollbar-thumb { background: #0057ff; }
    </style>
</head>
<body class="theme-dark">
    <nav class="navbar sticky-top">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <a href="/" class="flex items-center space-x-4">
                    <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="Logo" class="h-10 w-10 rounded-lg">
                    <h1 class="text-2xl font-bold text-coinbase">TradeScout Pro</h1>
                </a>
                <div class="flex items-center space-x-4">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." class="px-4 py-2 rounded-lg search-input w-64">
                    <button id="themeToggle" class="p-3 rounded-lg bg-blue-900 hover:bg-blue-800 transition">
                        <span class="text-xl">🌙</span>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="text-center mb-8 text-blue-300">
            <p>Live cryptocurrency prices • Last updated: <span id="lastUpdate">{{ last_update }}</span> • Auto-refreshes every minute</p>
        </div>

        <div class="rounded-2xl shadow-xl overflow-hidden border border-coinbase">
            <div class="table-container">
                <table class="w-full min-w-[1200px]">
                    <thead class="sticky top-0 z-10">
                        <tr>
                            <th class="px-6 py-4 text-left text-xs font-medium uppercase tracking-wider text-center">#</th>
                            <th class="px-6 py-4 text-left text-xs font-medium uppercase tracking-wider">Coin</th>
                            <th class="px-6 py-4 text-right text-xs font-medium uppercase tracking-wider">Price</th>
                            <th class="px-6 py-4 text-right text-xs font-medium uppercase tracking-wider">1h</th>
                            <th class="px-6 py-4 text-right text-xs font-medium uppercase tracking-wider">24h</th>
                            <th class="px-6 py-4 text-right text-xs font-medium uppercase tracking-wider">7d</th>
                            <th class="px-6 py-4 text-right text-xs font-medium uppercase tracking-wider">Market Cap</th>
                            <th class="px-6 py-4 text-right text-xs font-medium uppercase tracking-wider">Volume (24h)</th>
                            <th class="px-6 py-4 text-right text-xs font-medium uppercase tracking-wider">Circulating Supply</th>
                            <th class="px-6 py-4 text-center text-xs font-medium uppercase tracking-wider">Last 7 Days</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody" class="divide-y divide-blue-900/50">
                        {% for coin in crypto_data %}
                        <tr class="hover:bg-blue-900/20 transition-colors cursor-pointer" onclick="showCoinDetail('{{ coin.id }}', '{{ coin.name }}', '{{ coin.symbol }}')">
                            <td class="py-4 px-6 text-center text-gray-400">{{ coin.rank }}</td>
                            <td class="py-4 px-6">
                                <div class="flex items-center space-x-3">
                                    <img src="{{ coin.logo }}" alt="{{ coin.name }}" class="w-8 h-8 rounded-full">
                                    <div>
                                        <div class="font-medium">{{ coin.name }}</div>
                                        <div class="text-sm text-gray-400 uppercase">{{ coin.symbol }}</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-4 px-6 text-right font-medium">${{ '%.2f' % coin.price if coin.price else '0.00' }}</td>
                            <td class="py-4 px-6 text-right change-{{ 'positive' if coin.change_1h > 0 else 'negative' }}">
                                {% if coin.change_1h > 0 %}+{% endif %}{{ coin.change_1h }}%
                            </td>
                            <td class="py-4 px-6 text-right change-{{ 'positive' if coin.change_24h > 0 else 'negative' }}">
                                {% if coin.change_24h > 0 %}+{% endif %}{{ coin.change_24h }}%
                            </td>
                            <td class="py-4 px-6 text-right change-{{ 'positive' if coin.change_7d > 0 else 'negative' }}">
                                {% if coin.change_7d > 0 %}+{% endif %}{{ coin.change_7d }}%
                            </td>
                            <td class="py-4 px-6 text-right">{{ format_number(coin.market_cap) }}</td>
                            <td class="py-4 px-6 text-right">{{ format_number(coin.volume_24h) }}</td>
                            <td class="py-4 px-6 text-right text-sm">{{ format_supply(coin.circulating_supply, coin.symbol) }}</td>
                            <td class="py-4 px-6 text-center">
                                <canvas class="sparkline-canvas mx-auto" data-prices='{{ coin.sparkline_prices | tojson }}'></canvas>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <!-- Coin Detail Modal -->
    <div class="modal fade" id="coinModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="coinModalLabel"></h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <div id="coinDetailContent"></div>
                    <canvas id="coinChart" height="200"></canvas>
                </div>
            </div>
        </div>
    </div>

    <footer class="text-center py-8 text-gray-400 text-sm">
        Powered by CoinGecko API • TradeScout Pro © 2026
    </footer>

    <script>
        // Theme toggle with persistence
        const themeToggle = document.getElementById('themeToggle');
        const html = document.documentElement;
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            html.classList.add('dark');
            themeToggle.innerHTML = '☀️';
        } else {
            html.classList.remove('dark');
            themeToggle.innerHTML = '🌙';
        }
        themeToggle.addEventListener('click', () => {
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                localStorage.theme = 'light';
                themeToggle.innerHTML = '🌙';
            } else {
                html.classList.add('dark');
                localStorage.theme = 'dark';
                themeToggle.innerHTML = '☀️';
            }
        });

        // Search filter
        const searchInput = document.getElementById('searchInput');
        const rows = document.querySelectorAll('#tableBody tr');
        searchInput.addEventListener('input', () => {
            const term = searchInput.value.toLowerCase();
            rows.forEach(row => {
                row.style.display = row.textContent.toLowerCase().includes(term) ? '' : 'none';
            });
        });

        // Render initial sparklines
        function renderSparklines() {
            document.querySelectorAll('.sparkline-canvas').forEach(canvas => {
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
        renderSparklines();

        // Auto-refresh data every 60s
        async function refreshData() {
            try {
                const res = await fetch('/api/data');
                const { data, last_update } = await res.json();
                document.getElementById('lastUpdate').textContent = last_update;
                const tbody = document.getElementById('tableBody');
                tbody.innerHTML = '';
                data.forEach(coin => {
                    const row = document.createElement('tr');
                    row.className = 'hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors cursor-pointer';
                    row.onclick = () => showCoinDetail(coin.id, coin.name, coin.symbol);
                    row.innerHTML = `
                        <td class="py-4 px-6 text-center text-gray-500 dark:text-gray-400">${coin.rank}</td>
                        <td class="py-4 px-6">
                            <div class="flex items-center space-x-3">
                                <img src="${coin.logo}" class="w-8 h-8 rounded-full">
                                <div>
                                    <div class="font-medium">${coin.name}</div>
                                    <div class="text-sm text-gray-500 dark:text-gray-400 uppercase">${coin.symbol}</div>
                                </div>
                            </div>
                        </td>
                        <td class="py-4 px-6 text-right font-medium">$${parseFloat(coin.price).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 8})}</td>
                        <td class="py-4 px-6 text-right ${coin.change_1h > 0 ? 'text-green-500' : coin.change_1h < 0 ? 'text-red-500' : ''}">${coin.change_1h > 0 ? '+' : ''}${coin.change_1h}%</td>
                        <td class="py-4 px-6 text-right ${coin.change_24h > 0 ? 'text-green-500' : coin.change_24h < 0 ? 'text-red-500' : ''}">${coin.change_24h > 0 ? '+' : ''}${coin.change_24h}%</td>
                        <td class="py-4 px-6 text-right ${coin.change_7d > 0 ? 'text-green-500' : coin.change_7d < 0 ? 'text-red-500' : ''}">${coin.change_7d > 0 ? '+' : ''}${coin.change_7d}%</td>
                        <td class="py-4 px-6 text-right">${formatNumber(coin.market_cap)}</td>
                        <td class="py-4 px-6 text-right">${formatNumber(coin.volume_24h)}</td>
                        <td class="py-4 px-6 text-right text-sm">${formatSupply(coin.circulating_supply, coin.symbol)}</td>
                        <td class="py-4 px-6 text-center">
                            <canvas class="sparkline-canvas mx-auto" data-prices='${JSON.stringify(coin.sparkline_prices)}'></canvas>
                        </td>
                    `;
                    tbody.appendChild(row);
                });
                renderSparklines();
            } catch (e) {
                console.error('Refresh failed:', e);
            }
        }

        function formatNumber(num) {
            if (!num) return "N/A";
            if (num >= 1e12) return `$${(num/1e12).toFixed(2)}T`;
            if (num >= 1e9) return `$${(num/1e9).toFixed(2)}B`;
            if (num >= 1e6) return `$${(num/1e6).toFixed(2)}M`;
            return `$${(num).toFixed(2)}`;
        }

        function formatSupply(num, symbol) {
            if (!num) return "N/A";
            return `${num.toLocaleString()} ${symbol}`;
        }

        setInterval(refreshData, 60000);

        // Show coin detail modal
        let detailChart;
        async function showCoinDetail(id, name, symbol) {
            const modal = new bootstrap.Modal(document.getElementById('coinModal'));
            document.getElementById('coinModalLabel').textContent = `${name} (${symbol.toUpperCase()})`;
            const content = document.getElementById('coinDetailContent');
            content.innerHTML = 'Loading...';
            try {
                const [detailRes, chartRes] = await Promise.all([fetch(`/api/coin/${id}`), fetch(`/api/coin_chart/${id}`)]);
                const detail = await detailRes.json();
                const chartData = await chartRes.json();

                content.innerHTML = `
                    <p><strong>Price:</strong> $${detail.market_data.current_price.usd.toLocaleString()}</p>
                    <p><strong>Market Cap:</strong> $${detail.market_data.market_cap.usd.toLocaleString()}</p>
                    <p><strong>24h Volume:</strong> $${detail.market_data.total_volume.usd.toLocaleString()}</p>
                    <p><strong>24h Change:</strong> ${detail.market_data.price_change_percentage_24h.toFixed(2)}%</p>
                    <p><strong>All Time High:</strong> $${detail.market_data.ath.usd.toLocaleString()}</p>
                `;

                const labels = chartData.prices.map(p => new Date(p[0]).toLocaleDateString());
                const prices = chartData.prices.map(p => p[1]);
                if (detailChart) detailChart.destroy();
                detailChart = new Chart(document.getElementById('coinChart'), {
                    type: 'line',
                    data: { labels, datasets: [{ label: 'Price (USD)', data: prices, borderColor: '#1976d2', tension: 0.3 }] },
                    options: { responsive: true, scales: { x: { ticks: { maxTicksLimit: 10 } } } }
                });

                modal.show();
            } catch (e) {
                content.innerHTML = 'Error loading detail: ' + e;
            }
        }
    </script>
</body>
</html>
'''
