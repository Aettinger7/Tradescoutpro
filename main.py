from flask import Flask, render_template_string, jsonify
from datetime import datetime
from time import sleep
import threading
import pandas as pd
import numpy as np
from polygon import RESTClient

app = Flask(__name__)

# Your Polygon key
client = RESTClient("2lm_5uIh9NF6hQkcOxJN85RL9Ta0xHjF")

# Assets
ASSETS = ["AAPL", "MSFT", "TSLA", "X:BTCUSD", "X:ETHUSD"]

# Global data
results = {"time": "Loading...", "signals": []}
live_prices = {"AAPL": "-", "MSFT": "-", "TSLA": "-", "BTC": "-", "ETH": "-"}

# Simple signal check (same logic)
def check_signal(df):
    if len(df) < 60: return None
    close = df['close']
    low = df['low']
    volume = df['volume']
    last = df.iloc[-1]

    score = 0
    reasons = []

    current_rsi = rsi(close).iloc[-1]
    prev_rsi = rsi(close).iloc[-2]
    if prev_rsi < 30 and current_rsi > 30:
        score += 30
        reasons.append("RSI reclaim")

    hist = macd_histogram(close)
    if hist.iloc[-1] > 0 and hist.iloc[-1] > hist.iloc[-2] > hist.iloc[-3]:
        score += 25
        reasons.append("MACD expansion")

    if last['close'] > ema(close, 10).iloc[-1] > ema(close, 20).iloc[-1] > ema(close, 50).iloc[-1]:
        score += 25
        reasons.append("EMA stack")

    avg_vol = volume.rolling(20).mean().iloc[-1]
    if volume.iloc[-1] > 1.5 * avg_vol:
        score += 20
        reasons.append("Volume spike")

    if score >= 70:
        return {"score": score, "reasons": ", ".join(reasons)}
    return None

# Scanner loop
def scanner_loop():
    global results, live_prices
    while True:
        signals = []
        prices = {}
        for symbol in ASSETS:
            try:
                aggs = client.get_aggs(symbol, 1, 'day', limit=100)
                if aggs:
                    df = pd.DataFrame(aggs)
                    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                    df.set_index('timestamp', inplace=True)
                    df = df[['open', 'high', 'low', 'close', 'volume']]
                    signal = check_signal(df)
                    if signal:
                        sym = symbol.replace("X:", "").replace("USD", "")
                        signals.append({"symbol": sym, **signal})
                    prices[sym] = round(df['close'].iloc[-1], 2)
            except:
                continue
        results = {"time": datetime.now().strftime("%H:%M:%S"), "signals": signals}
        live_prices.update(prices)
        sleep(60)  # Update every minute for ticker

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
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <style>
        :root {
            --bg: #0f172a;
            --sidebar: #1e293b;
            --card: #1e293b;
            --text: #e2e8f0;
            --accent: #3b82f6;
            --green: #10b981;
            --red: #ef4444;
            --gray: #64748b;
        }
        [data-theme="light"] {
            --bg: #f1f5f9;
            --sidebar: #e2e8f0;
            --card: #ffffff;
            --text: #1e293b;
            --accent: #2563eb;
            --green: #059669;
            --red: #dc2626;
            --gray: #64748b;
        }
        body { margin: 0; font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); display: flex; min-height: 100vh; }
        .sidebar {
            width: 280px;
            background: var(--sidebar);
            padding: 20px;
            box-shadow: 4px 0 20px rgba(0,0,0,0.2);
            position: fixed;
            height: 100vh;
            overflow-y: auto;
        }
        .logo { font-size: 2em; font-weight: 700; color: var(--accent); margin-bottom: 40px; }
        .menu-item { padding: 15px; border-radius: 12px; margin-bottom: 10px; cursor: pointer; transition: 0.3s; }
        .menu-item:hover, .menu-item.active { background: var(--accent); color: white; }
        .main { margin-left: 280px; padding: 30px; width: calc(100% - 280px); }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .ticker { background: var(--card); padding: 15px; border-radius: 12px; font-size: 1.4em; font-weight: 600; display: flex; gap: 30px; flex-wrap: wrap; }
        .price-up { color: var(--green); }
        .price-down { color: var(--red); }
        .chart-container { background: var(--card); border-radius: 16px; padding: 20px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
        .signals-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 24px; margin-top: 40px; }
        .signal-card {
            background: var(--card);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            border-left: 6px solid var(--green);
        }
        .symbol { font-size: 2em; font-weight: 700; color: var(--green); }
        .score { font-size: 1.8em; color: var(--accent); margin: 16px 0; }
        .reasons { margin: 16px 0; line-height: 1.6; }
        .action-buttons { display: flex; gap: 16px; margin-top: 20px; }
        .btn-buy { background: var(--green); color: white; padding: 12px 24px; border-radius: 12px; font-weight: bold; cursor: pointer; }
        .btn-sell { background: var(--red); color: white; padding: 12px 24px; border-radius: 12px; font-weight: bold; cursor: pointer; }
        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--card);
            border: none;
            border-radius: 50px;
            padding: 12px 20px;
            cursor: pointer;
            font-size: 1.2em;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        .no-signal { text-align: center; font-size: 2em; color: var(--gray); margin: 100px; }
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
        <div class="header">
            <h1>Advanced Trading Dashboard</h1>
            <button class="theme-toggle" onclick="toggleTheme()">🌙 Dark Mode</button>
        </div>
        <div class="ticker" id="ticker">
            Loading live prices...
        </div>
        <div class="chart-container">
            <canvas id="candlestickChart"></canvas>
        </div>
        <h2>Active Signals</h2>
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
                    AAPL $${p.AAPL} • MSFT $${p.MSFT} • TSLA $${p.TSLA} • BTC $${p.BTC} • ETH $${p.ETH}
                `;
            } catch (e) {}
        }
        updatePrices();
        setInterval(updatePrices, 60000);
        // Dummy chart (real one would use Polygon data)
        new Chart(document.getElementById('candlestickChart'), {
            type: 'candlestick',
            data: {
                datasets: [{
                    label: 'Price',
                    data: [] // would load real data
                }]
            },
            options: { responsive: true }
        });
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
