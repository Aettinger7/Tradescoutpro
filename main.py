from flask import Flask, render_template_string, jsonify
from datetime import datetime
from time import sleep
import threading
from polygon import RESTClient

app = Flask(__name__)

# Your Polygon API key
client = RESTClient("2lm_5uIh9NF6hQkcOxJN85RL9Ta0xHjF")

# Assets
STOCKS = ["AAPL", "MSFT", "TSLA", "NVDA", "AMZN"]
CRYPTO = ["X:BTCUSD", "X:ETHUSD", "X:SOLUSD", "X:ADAUSD", "X:DOGEUSD"]

# Global data
live_data = {"stocks": {}, "crypto": {}}
last_update = "Loading..."

def update_prices():
    global live_data, last_update
    while True:
        stocks = {}
        crypto = {}
        for symbol in STOCKS:
            try:
                trade = client.get_last_trade(symbol)
                stocks[symbol] = round(trade.price, 2)
            except:
                stocks[symbol] = "—"
        for symbol in CRYPTO:
            try:
                trade = client.get_last_trade(symbol)
                sym = symbol.replace("X:", "").replace("USD", "")
                crypto[sym] = round(trade.price, 2 if sym in ["BTC", "ETH"] else 4)
            except:
                sym = symbol.replace("X:", "").replace("USD", "")
                crypto[sym] = "—"
        live_data = {"stocks": stocks, "crypto": crypto}
        last_update = datetime.now().strftime("%b %d, %Y - %H:%M:%S")
        sleep(60)  # Update every minute

threading.Thread(target=update_prices, daemon=True).start()

@app.route('/')
def dashboard():
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/stocks')
def api_stocks():
    return jsonify(live_data["stocks"])

@app.route('/api/crypto')
def api_crypto():
    return jsonify(live_data["crypto"])

@app.route('/markets/<category>')
def markets(category):
    if category == "crypto":
        return render_template_string(MARKETS_PAGE, category="Cryptocurrency", assets=CRYPTO)
    elif category == "stocks":
        return render_template_string(MARKETS_PAGE, category="Stocks", assets=STOCKS)
    return "Page not found", 404

@app.route('/settings')
def settings():
    return render_template_string(SETTINGS_PAGE)

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0f172a;
            --sidebar: #1e293b;
            --card: #1e293b;
            --text: #e2e8f0;
            --accent: #3b82f6;
            --green: #10b981;
            --gray: #64748b;
        }
        [data-theme="light"] {
            --bg: #f8fafc;
            --sidebar: #ffffff;
            --card: #ffffff;
            --text: #1e293b;
            --accent: #2563eb;
            --green: #059669;
        }
        body { margin: 0; font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); display: flex; min-height: 100vh; }
        .sidebar {
            width: 260px;
            background: var(--sidebar);
            padding: 30px 20px;
            box-shadow: 4px 0 20px rgba(0,0,0,0.1);
            position: fixed;
            height: 100vh;
        }
        .logo {
            font-size: 2em;
            font-weight: 700;
            color: var(--accent);
            text-align: center;
            margin-bottom: 60px;
        }
        .menu-item {
            padding: 16px 20px;
            border-radius: 12px;
            margin-bottom: 12px;
            cursor: pointer;
            font-weight: 500;
            transition: 0.3s;
        }
        .menu-item:hover { background: var(--accent); color: white; }
        .submenu {
            margin-left: 20px;
            display: none;
        }
        .menu-item.active > .submenu { display: block; }
        .submenu .menu-item { padding-left: 40px; font-size: 0.95em; }
        .main { margin-left: 260px; padding: 40px; width: calc(100% - 260px); }
        .header { text-align: center; margin-bottom: 40px; }
        h1 { font-size: 3em; margin: 0; }
        .last-update { font-size: 1.2em; color: var(--gray); margin: 30px 0; }
        .welcome { text-align: center; font-size: 1.6em; color: var(--gray); margin: 100px 0; }
        .theme-toggle {
            position: absolute;
            top: 30px;
            right: 30px;
            background: var(--card);
            border: none;
            border-radius: 50px;
            padding: 12px 24px;
            cursor: pointer;
            font-size: 1.1em;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        footer { text-align: center; margin-top: 100px; color: var(--gray); font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="logo">TradeScout Pro</div>
        <div class="menu-item active">Dashboard</div>
        <div class="menu-item" onclick="toggleSubmenu(this)">
            Markets
            <div class="submenu">
                <div class="menu-item" onclick="window.location='/markets/crypto'">Cryptocurrency</div>
                <div class="menu-item" onclick="window.location='/markets/stocks'">Stocks</div>
            </div>
        </div>
        <div class="menu-item" onclick="window.location='/settings'">Settings</div>
    </div>
    <div class="main">
        <button class="theme-toggle" onclick="toggleTheme()">🌙 Dark Mode</button>
        <div class="header">
            <h1>TradeScout Pro</h1>
            <p class="last-update">Last updated: {{ time }}</p>
        </div>
        <p class="welcome">Welcome to your real-time market dashboard.<br>
        Select "Markets" to view live prices for stocks and crypto.</p>
    </div>
    <footer>Powered by Polygon • Updates every minute</footer>
    <script>
        function toggleTheme() {
            const body = document.body;
            if (body.getAttribute('data-theme') === 'dark') {
                body.setAttribute('data-theme', 'light');
            } else {
                body.setAttribute('data-theme', 'dark');
            }
        }
        function toggleSubmenu(el) {
            const submenu = el.querySelector('.submenu');
            submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
        }
    </script>
</body>
</html>
"""

MARKETS_PAGE = """
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ category }} - TradeScout Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <style>
        :root { --bg: #0f172a; --sidebar: #1e293b; --card: #1e293b; --text: #e2e8f0; --accent: #3b82f6; --green: #10b981; --gray: #64748b; }
        [data-theme="light"] { --bg: #f8fafc; --sidebar: #ffffff; --card: #ffffff; --text: #1e293b; --accent: #2563eb; --green: #059669; }
        body { margin: 0; font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); display: flex; min-height: 100vh; }
        .sidebar { width: 260px; background: var(--sidebar); padding: 30px 20px; box-shadow: 4px 0 20px rgba(0,0,0,0.1); position: fixed; height: 100vh; }
        .logo { font-size: 2em; font-weight: 700; color: var(--accent); text-align: center; margin-bottom: 60px; }
        .menu-item { padding: 16px 20px; border-radius: 12px; margin-bottom: 12px; cursor: pointer; font-weight: 500; transition: 0.3s; }
        .menu-item:hover { background: var(--accent); color: white; }
        .main { margin-left: 260px; padding: 40px; width: calc(100% - 260px); }
        h1 { font-size: 2.8em; text-align: center; margin-bottom: 40px; }
        .market-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; }
        .market-card {
            background: var(--card);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            text-align: center;
        }
        .symbol { font-size: 2em; font-weight: 700; color: var(--green); margin-bottom: 10px; }
        .price { font-size: 2.2em; font-weight: 600; margin: 20px 0; }
        .sentiment { font-size: 1.1em; color: var(--gray); }
        .loading { text-align: center; font-size: 1.6em; color: var(--gray); margin: 100px; }
        .theme-toggle { position: absolute; top: 30px; right: 30px; background: var(--card); border: none; border-radius: 50px; padding: 12px 24px; cursor: pointer; font-size: 1.1em; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="logo">TradeScout Pro</div>
        <div class="menu-item" onclick="window.location='/'">Dashboard</div>
        <div class="menu-item active">{{ category }}</div>
        <div class="menu-item" onclick="window.location='/settings'">Settings</div>
    </div>
    <div class="main">
        <button class="theme-toggle" onclick="toggleTheme()">🌙 Dark Mode</button>
        <h1>{{ category }}</h1>
        <div class="market-grid" id="market-list">
            <p class="loading">Loading live prices...</p>
        </div>
    </div>
    <script>
        function toggleTheme() {
            const body = document.body;
            if (body.getAttribute('data-theme') === 'dark') {
                body.setAttribute('data-theme', 'light');
            } else {
                body.setAttribute('data-theme', 'dark');
            }
        }
        async function loadPrices() {
            try {
                const res = await axios.get('/api/{{ "crypto" if category == "Cryptocurrency" else "stocks" }}');
                const data = res.data;
                let html = '';
                for (const [sym, price] of Object.entries(data)) {
                    html += `
                        <div class="market-card">
                            <div class="symbol">${sym}</div>
                            <div class="price">$${price}</div>
                            <div class="sentiment">Live • Updated now</div>
                        </div>
                    `;
                }
                document.getElementById('market-list').innerHTML = html || '<p class="loading">No data available</p>';
            } catch (e) {
                document.getElementById('market-list').innerHTML = '<p class="loading">Error loading prices</p>';
            }
        }
        loadPrices();
        setInterval(loadPrices, 60000);
    </script>
</body>
</html>
"""

SETTINGS_PAGE = """
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Settings - TradeScout Pro</title>
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: #e2e8f0; padding: 40px; }
        h1 { text-align: center; }
        .container { max-width: 800px; margin: 0 auto; }
    </style>
</head>
<body>
    <h1>Settings</h1>
    <div class="container">
        <p>Theme, notifications, API keys, and more coming soon!</p>
        <p><a href="/">← Back to Dashboard</a></p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
