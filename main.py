from flask import Flask, render_template_string, jsonify, request
import requests
import datetime
import json

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"  # Your Pro key

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': True,
        'price_change_percentage': '24h,7d'
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except:
        return []

def fetch_trending_top_25():
    try:
        response = requests.get(COINGECKO_TRENDING, timeout=10)
        response.raise_for_status()
        data = response.json()
        trending_coins = data.get('coins', [])[:25]
        ids = [coin['item']['id'] for coin in trending_coins]
        if not ids:
            return []
        
        params = {
            'vs_currency': 'usd',
            'ids': ','.join(ids),
            'order': 'market_cap_desc',
            'per_page': 50,
            'page': 1,
            'sparkline': True,
            'price_change_percentage': '24h,7d'
        }
        response = requests.get(COINGECKO_MARKETS, params=params, timeout=10)
        response.raise_for_status()
        full_data = response.json()
        
        order_map = {coin['id']: idx for idx, coin in enumerate(full_data)}
        full_data.sort(key=lambda x: order_map.get(x['id'], 999))
        return full_data[:25]
    except:
        return []

def get_coin_detail(coin_id):
    url = COINGECKO_COIN_DETAIL.format(id=coin_id)
    params = {'localization': False, 'tickers': False, 'market_data': True,
              'community_data': False, 'developer_data': False, 'sparkline': False}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except:
        return {}

def get_chart_data(coin_id):
    url = COINGECKO_CHART.format(id=coin_id)
    params = {'vs_currency': 'usd', 'days': 30, 'interval': 'daily'}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()['prices']
    except:
        return []

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/trending')
def trending():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/top100')
def api_top100():
    data = fetch_crypto_data()
    return jsonify({'data': data, 'timestamp': datetime.datetime.utcnow().timestamp()})

@app.route('/api/trending')
def api_trending():
    data = fetch_trending_top_25()
    return jsonify({'data': data, 'timestamp': datetime.datetime.utcnow().timestamp()})

@app.route('/api/coin/<coin_id>')
def api_coin(coin_id):
    detail = get_coin_detail(coin_id)
    chart = get_chart_data(coin_id)
    return jsonify({'detail': detail, 'chart': chart})

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="icon" href="https://www.tradescoutpro.com/favicon.ico">
</head>
<body>
    <header>
        <div class="container header-content">
            <a href="/" class="logo">TradeScout Pro</a>
            <nav>
                <a href="/" class="{% if request.path == '/' %}active{% endif %}">Top 100</a>
                <a href="/trending" class="{% if request.path == '/trending' %}active{% endif %}">Trending</a>
                <button id="theme-toggle" aria-label="Toggle dark/light mode">🌙</button>
            </nav>
        </div>
    </header>

    <main class="container">
        <h1>{{ title }}</h1>
        
        <div class="controls">
            <input type="text" id="search" placeholder="Search coin..." aria-label="Search">
            <div id="last-update">Loading...</div>
        </div>

        <div class="table-wrapper">
            <table id="coins-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Coin</th>
                        <th>Price</th>
                        <th>24h %</th>
                        <th>7d %</th>
                        <th>Market Cap</th>
                        <th>Volume(24h)</th>
                        <th>Last 7d</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </div>
    </main>

    <!-- Modal -->
    <div id="modal" class="modal hidden">
        <div class="modal-content">
            <span class="close">&times;</span>
            <div id="modal-body"></div>
        </div>
    </div>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
    <script>
        const API_ENDPOINT = '{% block api_endpoint %}/api/top100{% endblock %}';
        const PAGE_TITLE = '{% block page_title %}Top 100{% endblock %}';
    </script>
</body>
</html>
'''
</parameter>
</xai:function_call>
