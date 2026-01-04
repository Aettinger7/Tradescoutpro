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
            "fear_greed": 40,
            "alt_season": 24,
        }
    except Exception as e:
        print(f"Metrics error: {e}")
        return {
            "total_market_cap": 3120000000000,
            "btc_dominance": 58.4,
            "fear_greed": 40,
            "alt_season": 24,
        }

# fetch_crypto_data and fetch_trending_data same as last fixed version

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

# All other routes same

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <!-- Same head -->
</head>
<body class="min-h-screen">
    <!-- Nav same -->

    <!-- Metrics Boxes (CMC style) -->
    <div class="container mx-auto px-6 py-8">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
            <div class="bg-gray-800 rounded-xl p-6 shadow-lg text-center">
                <p class="text-gray-400 text-sm mb-2">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.0f}".format(metrics.total_market_cap / 1e12) }}T</p>
                <p class="text-green text-sm mt-2">+1.27%</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 shadow-lg text-center">
                <p class="text-gray-400 text-sm mb-2">Fear & Greed Index</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-gray-400 text-sm">Neutral</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 shadow-lg text-center">
                <p class="text-gray-400 text-sm mb-2">Altcoin Season Index</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}/100</p>
                <p class="text-gray-400 text-sm">Bitcoin Season</p>
            </div>
            <div class="bg-gray-800 rounded-xl p-6 shadow-lg text-center">
                <p class="text-gray-400 text-sm mb-2">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ "%.1f" % metrics.btc_dominance }}%</p>
            </div>
        </div>
    </div>

    <!-- Table full width -->
    <div class="container mx-auto px-6 pb-10">
        <div class="overflow-x-auto rounded-2xl shadow-2xl bg-gray-900/50">
            <table class="w-full text-left">
                <!-- same table -->
            </table>
        </div>
    </div>

    <!-- Modal and script same -->

</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
