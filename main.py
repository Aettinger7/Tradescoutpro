from flask import Flask, render_template_string, jsonify
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

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

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=crypto_data, last_update=last_update)

@app.route('/api/data')
def api_data():
    crypto_data, last_update = fetch_crypto_data()
    return jsonify({"data": crypto_data, "last_update": last_update})

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
    <title>TradeScout Pro — Top 100 Cryptocurrencies</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #000000 0%, #001f3f 100%);
            color: #e6f1ff;
            min-height: 100vh;
        }
        .navbar {
            background: rgba(0, 31, 63, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #0057ff;
        }
        .table-container {
            max-height: 70vh; /* Limits height so table body scrolls independently */
            overflow-y: auto;
            overflow-x: auto;
        }
        .table thead th {
            position: sticky;
            top: 0;
            background: #001f3f;
            color: #93c5fd;
            border-bottom: 2px solid #0057ff;
            z-index: 10;
        }
        .table tbody tr:hover {
            background: rgba(0, 87, 255, 0.1);
        }
        .sparkline-canvas { height: 48px; width: 160px; }
        .modal-content {
            background: #001f3f;
            color: #e6f1ff;
            border: 1px solid #0057ff;
        }
        .btn-close-white { filter: invert(1); }
        .search-input {
            background: #0f172a;
            border: 1px solid #0057ff;
            color: #e6f1ff;
        }
        .search-input:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(0, 87, 255, 0.5);
        }
        ::-webkit-scrollbar { height: 8px; width: 8px; }
        ::-webkit-scrollbar-track { background: #001f3f; }
        ::-webkit-scrollbar-thumb { background: #0057ff; border-radius: 4px; }
    </style>
</head>
<body>
    <nav class="navbar sticky-top">
        <div class="max-w-7xl mx-auto px-6 flex justify-between items-center h-16">
            <a href="/" class="flex items-center space-x-3">
                <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="Logo" class="h-9 w-9 rounded-lg">
                <h1 class="text-2xl font-bold text-blue-400">TradeScout Pro</h1>
            </a>
            <div class="flex items-center space-x-6">
                <input type="text" id="searchInput" placeholder="Search cryptos..." class="px-5 py-2.5 rounded-lg search-input w-72 text-sm">
                <button id="themeToggle" class="p-3 rounded-lg bg-blue-900 hover:bg-blue-800 transition text-xl">
                    🌙
                </button>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-6 py-8">
        <div class="text-center mb-8 text-blue-200">
            <p>Live cryptocurrency prices • Last updated: <span id="lastUpdate">{{ last_update }}</span> • Auto-refreshes every minute</p>
        </div>

        <div class="rounded-2xl shadow-2xl overflow-hidden border border-blue-800">
            <div class="table-container">
                <table class="w-full min-w-[1200px]">
                    <thead>
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
                            <td class="py-4 px-6 text-right {% if coin.change_1h > 0 %}text-green-400{% else %}text-red-400{% endif %}">
                                {% if coin.change_1h > 0 %}+{% endif %}{{ coin.change_1h }}%
                            </td>
                            <td class="py-4 px-6 text-right {% if coin.change_24h > 0 %}text-green-400{% else %}text-red-400{% endif %}">
                                {% if coin.change_24h > 0 %}+{% endif %}{{ coin.change_24h }}%
                            </td>
                            <td class="py-4 px-6 text-right {% if coin.change_7d > 0 %}text-green-400{% else %}text-red-400{% endif %}">
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

    <!-- Modal and script same as previous version -->
    <!-- (Full script from last message - modal + sparkline render + refresh + detail) -->

    <script>
        // Same script as last full version (theme disabled, search, sparklines, refresh, modal)
        // Omitted for brevity - copy from previous full code
    </script>
</body>
</html>
'''
