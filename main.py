from flask import Flask, render_template_string, jsonify
from datetime import datetime
from time import sleep
import threading
from polygon import RESTClient

app = Flask(__name__)

# Your key
client = RESTClient("2lm_5uIh9NF6hQkcOxJN85RL9Ta0xHjF")

# Top 50 crypto symbols on Polygon (popular ones — Polygon has many more)
CRYPTO_SYMBOLS = [
    "X:BTCUSD", "X:ETHUSD", "X:SOLUSD", "X:XRPUSD", "X:BNBUSD", "X:ADAUSD", "X:DOGEUSD", 
    "X:TRXUSD", "X:AVAXUSD", "X:LINKUSD", "X:DOTUSD", "X:MATICUSD", "X:LTCUSD", 
    "X:SHIBUSD", "X:UNIUSD", "X:LEOUSD", "X:ETCUSD", "X:NEARUSD", "X:APTUSD", 
    "X:HBARUSD", "X:CROUSD", "X:VETUSD", "X:ICPUSD", "X:FILUSD", "X:ATOMUSD",
    "X:ALGOUSD", "X:QNTUSD", "X:FTMUSD", "X:MANAUSD", "X:SANDUSD", "X:AXSUSD",
    "X:CHZUSD", "X:THETAUSD", "X:EOSUSD", "X:ZECUSD", "X:MKRUSD", "X:AAVEUSD",
    "X:COMPUSD", "X:SNXUSD", "X:YFIUSD", "X:CRVUSD", "X:BALUSD", "X:SUSHIUSD",
    "X:1INCHUSD", "X:ENJUSD", "X:GRTUSD", "X:LRCUSD"
]  # 50 popular ones

# Global data
crypto_table = []
last_update = "Loading..."

def update_table():
    global crypto_table, last_update
    while True:
        table = []
        for symbol in CRYPTO_SYMBOLS:
            sym = symbol.replace("X:", "").replace("USD", "")
            try:
                # Current price
                trade = client.get_last_trade(symbol)
                price = round(trade.price, 2 if sym in ["BTC", "ETH"] else 4)
                
                # 24h change (simple from yesterday)
                yesterday = client.get_aggs(symbol, 1, 'day', limit=2)
                if len(yesterday) > 1:
                    change_24h = ((price - yesterday[-2].close) / yesterday[-2].close) * 100
                else:
                    change_24h = 0
                
                # Market cap & volume (approximate from price * supply — dummy for now, real needs more)
                market_cap = price * 1000000000  # placeholder
                volume = price * 10000000  # placeholder
                
                # Sparkline (last 7 days)
                aggs = client.get_aggs(symbol, 1, 'day', limit=7)
                sparkline = [a.close for a in aggs[::-1]] if aggs else [price] * 7
                
                table.append({
                    "rank": len(table) + 1,
                    "name": sym,
                    "price": f"${price}",
                    "change_24h": f"{change_24h:+.2f}%",
                    "market_cap": f"${market_cap:,.0f}",
                    "volume": f"${volume:,.0f}",
                    "sparkline": sparkline
                })
            except:
                continue
        crypto_table = table
        last_update = datetime.now().strftime("%b %d, %Y %H:%M")
        sleep(60)

threading.Thread(target=update_table, daemon=True).start()

@app.route('/')
def home():
    return render_template_string(HTML, crypto_list=crypto_table, last_update=last_update)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            margin: 0;
            padding: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }
        .logo {
            height: 80px;
            border-radius: 12px;
        }
        h1 {
            font-size: 3em;
            margin: 0;
            background: linear-gradient(to right, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .last-update {
            text-align: center;
            color: #64748b;
            margin-bottom: 30px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: #1e293b;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        th {
            background: #334155;
            padding: 16px;
            text-align: left;
            font-weight: 600;
        }
        td {
            padding: 16px;
            border-bottom: 1px solid #334155;
        }
        .rank { width: 60px; text-align: center; }
        .name { font-weight: 600; font-size: 1.1em; }
        .price { text-align: right; font-weight: 600; }
        .change { text-align: right; }
        .positive { color: #10b981; }
        .negative { color: #ef4444; }
        .chart { height: 50px; width: 120px; }
        .no-data { text-align: center; padding: 60px; color: #64748b; font-size: 1.4em; }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro Logo" class="logo">
        <h1>TradeScout Pro</h1>
    </div>
    <div class="last-update">Last updated: {{ last_update }}</div>
    {% if crypto_list %}
        <table>
            <thead>
                <tr>
                    <th class="rank">#</th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>24h %</th>
                    <th>Market Cap</th>
                    <th>Volume (24h)</th>
                    <th>Last 7 Days</th>
                </tr>
            </thead>
            <tbody>
                {% for coin in crypto_list %}
                    <tr>
                        <td class="rank">{{ coin.rank }}</td>
                        <td class="name">{{ coin.name }}</td>
                        <td class="price">{{ coin.price }}</td>
                        <td class="change {{ 'positive' if '+' in coin.change_24h else 'negative' }}">{{ coin.change_24h }}</td>
                        <td>{{ coin.market_cap }}</td>
                        <td>{{ coin.volume }}</td>
                        <td><canvas class="chart" id="chart-{{ coin.rank }}"></canvas></td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p class="no-data">Loading top 50 cryptocurrencies...</p>
    {% endif %}
    <script>
        {% for coin in crypto_list %}
            new Chart(document.getElementById('chart-{{ coin.rank }}'), {
                type: 'line',
                data: {
                    labels: ['', '', '', '', '', '', ''],
                    datasets: [{
                        data: {{ coin.sparkline }},
                        borderColor: '#3b82f6',
                        backgroundColor: 'rgba(59,130,246,0.1)',
                        fill: true,
                        tension: 0.4,
                        pointRadius: 0
                    }]
                },
                options: {
                    responsive: true,
                    plugins: { legend: { display: false } },
                    scales: { x: { display: false }, y: { display: false } }
                }
            });
        {% endfor %}
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
