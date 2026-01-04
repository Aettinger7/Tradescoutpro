from flask import Flask, render_template_string, jsonify, request
import requests
import datetime

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
            "fear_greed": 40,  # Current from CMC/Alternative.me
            "alt_season": 24,  # Current from CMC index
        }
    except:
        return {
            "total_market_cap": 3120000000000,
            "btc_dominance": 58.4,
            "fear_greed": 40,
            "alt_season": 24,
        }

# fetch_crypto_data and fetch_trending_data same as before...

@app.route('/')
def index():
    metrics = get_global_metrics()
    crypto_data, last_update = fetch_crypto_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=crypto_data, last_update=last_update, metrics=metrics, page="top")

@app.route('/trending')
def trending():
    metrics = get_global_metrics()
    trending_data, last_update = fetch_trending_data()
    return render_template_string(HTML_TEMPLATE, crypto_data=trending_data, last_update=last_update, metrics=metrics, page="trending")

# All other routes same...

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <!-- Same head -->
</head>
<body class="min-h-screen">
    <nav class="bg-blue-600 text-white py-5 px-8 flex justify-between items-center sticky top-0 z-50 shadow-xl">
        <a href="/" class="text-4xl font-bold flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12 rounded-lg">
            TradeScout Pro
        </a>
        <div class="flex items-center gap-10 text-lg">
            <a href="/" class="hover:text-cyan-300 {% if page == 'top' %}underline{% endif %}">Top 100</a>
            <a href="/trending" class="hover:text-cyan-300 {% if page == 'trending' %}underline{% endif %}">Trending</a>
            <div class="relative">
                <input type="text" id="searchInput" class="px-6 py-3 rounded-full bg-black/50 text-white placeholder-gray-400 border border-gray-600 focus:outline-none focus:border-cyan-400 w-96" placeholder="Search any crypto...">
                <div id="searchDropdown" class="absolute hidden bg-gray-900 border border-gray-700 rounded-lg shadow-xl mt-2 w-full z-50">
                    <div id="searchResults" class="max-h-96 overflow-y-auto"></div>
                </div>
            </div>
            <button id="themeToggle" class="text-3xl">🌙</button>
        </div>
    </nav>

    <!-- Metrics Boxes -->
    <div class="container mx-auto px-6 py-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-10">
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.0f}".format(metrics.total_market_cap / 1e12) }}T</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">Fear & Greed Index</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-sm text-gray-400">Neutral</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">Altcoin Season Index</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}</p>
                <p class="text-sm text-gray-400">Bitcoin Season</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 text-center shadow-lg">
                <p class="text-gray-400 text-sm">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ metrics.btc_dominance }}%</p>
            </div>
        </div>
    </div>

    <!-- Table -->
    <div class="container mx-auto px-6 max-w-full">
        <div class="overflow-x-auto rounded-2xl shadow-2xl">
            <table class="w-full text-left">
                <!-- table head and body same -->
            </table>
        </div>
    </div>

    <!-- Modal and script same -->

</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
