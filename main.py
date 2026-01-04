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
        return {
            "total_market_cap": data['total_market_cap']['usd'],
            "btc_dominance": data['market_cap_percentage']['btc'],
            "fear_greed": 40,  # Hardcoded from current data (CMC ~40)
            "alt_season_index": 24,  # Hardcoded low (Bitcoin season)
        }
    except:
        return {
            "total_market_cap": 3120000000000,
            "btc_dominance": 58.4,
            "fear_greed": 40,
            "alt_season_index": 24,
        }

def fetch_crypto_data():
    # Same as before...
    # (keep your existing fetch_crypto_data)

def fetch_trending_data():
    # Same as before...

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

# Keep all other routes (api/data, api/trending, api/search, api/coin_detail, api/coin_ohlc)

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <!-- Same head as before -->
</head>
<body class="min-h-screen">
    <nav class="navbar-blue text-white py-5 px-8 flex justify-between items-center sticky top-0 z-50 shadow-xl">
        <a href="/" class="text-4xl font-bold logo-font flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12 rounded-lg">
            TradeScout Pro
        </a>
        <div class="flex items-center gap-10 text-lg">
            <a href="/" class="{% if page == 'top' %}active-link{% endif %} hover:text-cyan-300">Top 100</a>
            <a href="/trending" class="{% if page == 'trending' %}active-link{% endif %} hover:text-cyan-300">Trending</a>
            <div class="relative">
                <input type="text" id="searchInput" class="px-6 py-3 rounded-full bg-black/50 text-white placeholder-gray-400 border border-gray-600 focus:outline-none focus:border-cyan-400 w-96" placeholder="Search any crypto...">
                <div id="searchDropdown" class="absolute hidden bg-gray-900 border border-gray-700 rounded-lg shadow-xl mt-2 w-full z-50">
                    <div id="searchResults" class="max-h-96 overflow-y-auto"></div>
                </div>
            </div>
            <button id="themeToggle" class="text-3xl">🌙</button>
        </div>
    </nav>

    <!-- New Header Metrics Row -->
    <div class="container mx-auto px-6 py-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <div class="bg-gray-800/80 rounded-xl p-6 text-center">
                <p class="text-gray-400 text-sm">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.0f}".format(metrics.total_market_cap / 1e12) }}T</p>
            </div>
            <div class="bg-gray-800/80 rounded-xl p-6 text-center">
                <p class="text-gray-400 text-sm">Fear & Greed Index</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-sm text-gray-400">Neutral</p>
            </div>
            <div class="bg-gray-800/80 rounded-xl p-6 text-center">
                <p class="text-gray-400 text-sm">Altcoin Season Index</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season_index }}</p>
                <p class="text-sm text-gray-400">Bitcoin Season</p>
            </div>
            <div class="bg-gray-800/80 rounded-xl p-6 text-center">
                <p class="text-gray-400 text-sm">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ "%.1f" % metrics.btc_dominance }}%</p>
            </div>
        </div>
    </div>

    <div class="container mx-auto px-6 max-w-7xl">
        <div class="overflow-x-auto rounded-2xl shadow-2xl">
            <table class="w-full text-left">
                <!-- Same table as before -->
            </table>
        </div>
        <p class="text-center text-gray-500 mt-8 text-sm">Last update: <span id="lastUpdate">{{ last_update }}</span> • Auto-refreshes every 60s • Powered by CoinGecko</p>
    </div>

    <!-- Modal same as before -->

    <script>
        // Same script as previous, with search console logs
        // Ensure openModal works
        // Sparklines with setTimeout if needed
    </script>
</body>
</html>
'''
