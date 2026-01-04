from flask import Flask, render_template_string, jsonify
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"  # Your Pro key

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
    }
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()

        formatted_data = []
        for rank, coin in enumerate(data, 1):
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
            })

        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update

    except Exception as e:
        print(f"Error: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=crypto_data, last_update=last_update)

@app.route('/api/data')
def api_data():
    crypto_data, last_update = fetch_crypto_data()
    return jsonify({"data": crypto_data, "last_update": last_update})

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro — Top 100 Cryptocurrencies</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: { extend: { fontFamily: { sans: ['Inter', 'sans-serif'] } }}
        }
    </script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        .table-container { overflow-x: auto; -webkit-overflow-scrolling: touch; }
        .sparkline-img { height: 48px; width: 160px; }
        ::-webkit-scrollbar { height: 8px; }
        ::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb { background: #c0c0c0; border-radius: 4px; }
        .dark ::-webkit-scrollbar-track { background: #1f2937; }
        .dark ::-webkit-scrollbar-thumb { background: #4b5563; }
    </style>
</head>
<body class="bg-gray-50 dark:bg-gray-950 text-gray-900 dark:text-gray-100 transition-colors duration-300">
    <!-- Navigation -->
    <nav class="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 sticky top-0 z-10 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center space-x-8">
                    <div class="flex items-center space-x-4">
                        <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="Logo" class="h-10 w-10 rounded-lg">
                        <h1 class="text-2xl font-bold text-blue-600 dark:text-blue-500">TradeScout Pro</h1>
                    </div>
                    <div class="hidden md:flex items-center space-x-8">
                        <a href="#" class="font-medium hover:text-blue-600 dark:hover:text-blue-400">Markets</a>
                        <a href="#" class="font-medium hover:text-blue-600 dark:hover:text-blue-400">Watchlist</a>
                        <a href="#" class="font-medium hover:text-blue-600 dark:hover:text-blue-400">Trending</a>
                    </div>
                </div>
                <div class="flex items-center space-x-4">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." class="px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 focus:outline-none focus:border-blue-500 w-64">
                    <button id="themeToggle" class="p-3 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition">
                        <span class="text-xl">🌙</span>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="text-center mb-8">
            <p class="text-gray-600 dark:text-gray-400">Live cryptocurrency prices • Last updated: <span id="lastUpdate">{{ last_update }}</span> • Auto-refreshes every minute</p>
        </div>

        <div class="bg-white dark:bg-gray-900 rounded-2xl shadow-xl overflow-hidden">
            <div class="table-container">
                <table class="w-full min-w-[1200px]">
                    <thead class="bg-gray-50 dark:bg-gray-800 sticky top-0 z-10">
                        <tr>
                            <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider text-center">#</th>
                            <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Coin</th>
                            <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Price</th>
                            <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">1h</th>
                            <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">24h</th>
                            <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">7d</th>
                            <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Market Cap</th>
                            <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Volume (24h)</th>
                            <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Circulating Supply</th>
                            <th class="px-6 py-4 text-center text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Last 7 Days</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody" class="divide-y divide-gray-200 dark:divide-gray-800">
                        {% for coin in crypto_data %}
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
                            <td class="py-4 px-6 text-center text-gray-500 dark:text-gray-400">{{ coin.rank }}</td>
                            <td class="py-4 px-6">
                                <div class="flex items-center space-x-3">
                                    <img src="{{ coin.logo }}" alt="{{ coin.name }}" class="w-8 h-8 rounded-full">
                                    <div>
                                        <div class="font-medium">{{ coin.name }}</div>
                                        <div class="text-sm text-gray-500 dark:text-gray-400 uppercase">{{ coin.symbol }}</div>
                                    </div>
                                </div>
                            </td>
                            <td class="py-4 px-6 text-right font-medium">${{ coin.price|float|format("%.2f") if coin.price else "0.00" }}</td>
                            <td class="py-4 px-6 text-right {% if coin.change_1h > 0 %}text-green-500{% elif coin.change_1h < 0 %}text-red-500{% endif %}">
                                {% if coin.change_1h > 0 %}+{% endif %}{{ coin.change_1h }}%
                            </td>
                            <td class="py-4 px-6 text-right {% if coin.change_24h > 0 %}text-green-500{% elif coin.change_24h < 0 %}text-red-500{% endif %}">
                                {% if coin.change_24h > 0 %}+{% endif %}{{ coin.change_24h }}%
                            </td>
                            <td class="py-4 px-6 text-right {% if coin.change_7d > 0 %}text-green-500{% elif coin.change_7d < 0 %}text-red-500{% endif %}">
                                {% if coin.change_7d > 0 %}+{% endif %}{{ coin.change_7d }}%
                            </td>
                            <td class="py-4 px-6 text-right">{{ format_number(coin.market_cap) }}</td>
                            <td class="py-4 px-6 text-right">{{ format_number(coin.volume_24h) }}</td>
                            <td class="py-4 px-6 text-right text-sm">{{ format_supply(coin.circulating_supply, coin.symbol) }}</td>
                            <td class="py-4 px-6 text-center">
                                <img src="https://www.coingecko.com/coins/{{ coin.id }}/sparkline" alt="{{ coin.name }} sparkline" class="sparkline-img mx-auto">
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <footer class="text-center py-8 text-gray-500 dark:text-gray-500 text-sm">
        Powered by CoinGecko API • TradeScout Pro © 2026
    </footer>

    <script>
        // Dark mode toggle
        const themeToggle = document.getElementById('themeToggle');
        const html = document.documentElement;
        
        // Load saved theme
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

        // Search
        const searchInput = document.getElementById('searchInput');
        const rows = document.querySelectorAll('#tableBody tr');

        searchInput.addEventListener('input', () => {
            const term = searchInput.value.toLowerCase();
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(term) ? '' : 'none';
            });
        });

        // Auto-refresh data
        async function refreshData() {
            try {
                const res = await fetch('/api/data');
                const { data, last_update } = await res.json();
                document.getElementById('lastUpdate').textContent = last_update;

                const tbody = document.getElementById('tableBody');
                tbody.innerHTML = '';

                data.forEach(coin => {
                    const change1hClass = coin.change_1h > 0 ? 'text-green-500' : coin.change_1h < 0 ? 'text-red-500' : '';
                    const change24hClass = coin.change_24h > 0 ? 'text-green-500' : coin.change_24h < 0 ? 'text-red-500' : '';
                    const change7dClass = coin.change_7d > 0 ? 'text-green-500' : coin.change_7d < 0 ? 'text-red-500' : '';

                    const row = document.createElement('tr');
                    row.className = 'hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors';
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
                        <td class="py-4 px-6 text-right ${change1hClass}">${coin.change_1h > 0 ? '+' : ''}${coin.change_1h}%</td>
                        <td class="py-4 px-6 text-right ${change24hClass}">${coin.change_24h > 0 ? '+' : ''}${coin.change_24h}%</td>
                        <td class="py-4 px-6 text-right ${change7dClass}">${coin.change_7d > 0 ? '+' : ''}${coin.change_7d}%</td>
                        <td class="py-4 px-6 text-right">${formatNumber(coin.market_cap)}</td>
                        <td class="py-4 px-6 text-right">${formatNumber(coin.volume_24h)}</td>
                        <td class="py-4 px-6 text-right text-sm">${formatSupply(coin.circulating_supply, coin.symbol)}</td>
                        <td class="py-4 px-6 text-center">
                            <img src="https://www.coingecko.com/coins/${coin.id}/sparkline" class="sparkline-img mx-auto">
                        </td>
                    `;
                    tbody.appendChild(row);
                });
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
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
