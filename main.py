from flask import Flask, render_template_string, jsonify
from datetime import datetime
from time import sleep
import threading
from polygon import RESTClient

app = Flask(__name__)

client = RESTClient("2lm_5uIh9NF6hQkcOxJN85RL9Ta0xHjF")

ASSETS = ["AAPL", "MSFT", "TSLA", "X:BTCUSD", "X:ETHUSD"]

results = {"time": "Loading...", "signals": []}
live_prices = {"AAPL": "—", "MSFT": "—", "TSLA": "—", "BTC": "—", "ETH": "—"}

def scanner_loop():
    global results, live_prices
    while True:
        signals = []
        prices = {}
        for symbol in ASSETS:
            try:
                # Live price
                last = client.get_last_trade(symbol)
                price = round(last.price, 2 if "USD" in symbol else 2)
                sym = symbol.replace("X:", "").replace("USD", "")
                prices[sym] = f"${price}"
                
                # Simple signal check (dummy for now — real logic later)
                # For demo, random signal
                if datetime.now().second % 30 == 0:  # occasional signal
                    signals.append({
                        "symbol": sym,
                        "score": 85,
                        "reasons": "RSI reclaim, MACD expansion, EMA stack"
                    })
            except:
                prices[sym] = "—"
        results = {"time": datetime.now().strftime("%H:%M:%S"), "signals": signals}
        live_prices.update(prices)
        sleep(60)  # Update every minute

threading.Thread(target=scanner_loop, daemon=True).start()

@app.route('/')
def home():
    return render_template_string(HTML, **results)

@app.route('/prices')
def prices():
    return jsonify(live_prices)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <meta http-equiv="refresh" content="60">
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <style>
        :root { --bg: #0f172a; --sidebar: #1e293b; --card: #1e293b; --text: #e2e8f0; --accent: #3b82f6; --green: #10b981; --gray: #64748b; }
        [data-theme="light"] { --bg: #f1f5f9; --sidebar: #e2e8f0; --card: #ffffff; --text: #1e293b; --accent: #2563eb; --green: #059669; }
        body { margin: 0; font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); display: flex; min-height: 100vh; }
        .sidebar { width: 280px; background: var(--sidebar); padding: 20px; box-shadow: 4px 0 20px rgba(0,0,0,0.2); position: fixed; height: 100vh; }
        .logo { font-size: 2em; font-weight: 700; color: var(--accent); margin-bottom: 40px; }
        .menu-item { padding: 15px; border-radius: 12px; margin-bottom: 10px; cursor: pointer; transition: 0.3s; }
        .menu-item:hover, .menu-item.active { background: var(--accent); color: white; }
        .main { margin-left: 280px; padding: 30px; width: calc(100% - 280px); }
        .ticker { background: var(--card); padding: 15px; border-radius: 12px; font-size: 1.4em; font-weight: 600; display: flex; gap: 30px; flex-wrap: wrap; justify-content: center; }
        .price { color: var(--green); }
        .time { font-size: 1.4em; color: var(--accent); margin: 40px 0; text-align: center; }
        .signals-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 24px; }
        .signal-card { background: var(--card); border-radius: 16px; padding: 24px; box-shadow: 0 8px 25px rgba(0,0,0,0.2); border-left: 6px solid var(--green); }
        .symbol { font-size: 2em; font-weight: 700; color: var(--green); }
        .score { font-size: 1.8em; color: var(--accent); margin: 16px 0; }
        .reasons { margin: 16px 0; line-height: 1.6; }
        .action-buttons { display: flex; gap: 16px; margin-top: 20px; }
        .btn-buy { background: var(--green); color: white; padding: 12px 24px; border-radius: 12px; font-weight: bold; cursor: pointer; }
        .btn-sell { background: #ef4444; color: white; padding: 12px 24px; border-radius: 12px; font-weight: bold; cursor: pointer; }
        .no-signal { text-align: center; font-size: 2em; color: var(--gray); margin: 100px; }
        .theme-toggle { position: absolute; top: 20px; right: 20px; background: var(--card); border: none; border-radius: 50px; padding: 12px 20px; cursor: pointer; font-size: 1.2em; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
    </style>
</head>
<body data-theme="dark">
    <div class="sidebar">
        <div class="logo">TradeScout Pro</div>
        <div class="menu-item active">Dashboard</div>
        <div class="menu-item">Markets</div>
        <div class="menu-item">Trading</div>
        <div class="menu-item">Portfolio</div>
        <div class="menu-item">Signals</div>
        <div class="menu-item">Settings</div>
    </div>
    <div class="main">
        <div class="theme-toggle" onclick="toggleTheme()">🌙 Dark Mode</div>
        <h1>Advanced Trading Dashboard</h1>
        <div class="ticker" id="ticker">Loading prices...</div>
        <div class="time">Last scan: {{ time }}</div>
        <div class="signals-grid">
            {% if signals %}
                {% for s in signals %}
                    <div class="signal-card">
                        <div class="symbol">{{ s.symbol }}</div>
                        <div class="score">Confidence: {{ s.score }}/100</div>
                        <div class="reasons">{{ s.reasons }}</div>
                        <div class="action-buttons">
                            <div class="btn-buy">BUY</div>
                            <div class="btn-sell">SELL</div>
                        </div>
                    </div>
                {% endfor %}
            {% else %}
                <p class="no-signal">No active signals<br>Waiting for high-probability setups...</p>
            {% endif %}
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
        async function updatePrices() {
            try {
                const res = await axios.get('/prices');
                const p = res.data;
                document.getElementById('ticker').innerHTML = `
                    AAPL <span class="price">${p.AAPL}</span> • 
                    MSFT <span class="price">${p.MSFT}</span> • 
                    TSLA <span class="price">${p.TSLA}</span> • 
                    BTC <span class="price">${p.BTC}</span> • 
                    ETH <span class="price">${p.ETH}</span>
                `;
            } catch (e) {
                document.getElementById('ticker').innerHTML = 'Prices loading...';
            }
        }
        updatePrices();
        setInterval(updatePrices, 60000);
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
