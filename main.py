from flask import Flask, render_template_string

app = Flask(__name__)

# Dummy top crypto data (real would come from API)
crypto_list = [
    {"rank": 1, "name": "Bitcoin", "symbol": "BTC", "price": "$90,123", "change_24h": "+1.23%", "change_class": "green", "market_cap": "$1.79T", "volume": "$45.2B", "sparkline": [85000, 86000, 88000, 89000, 90000, 90123]},
    {"rank": 2, "name": "Ethereum", "symbol": "ETH", "price": "$3,106", "change_24h": "+0.45%", "change_class": "green", "market_cap": "$374B", "volume": "$23.8B", "sparkline": [3000, 3050, 3080, 3100, 3106]},
    {"rank": 3, "name": "Tether", "symbol": "USDT", "price": "$1.00", "change_24h": "0.00%", "change_class": "gray", "market_cap": "$187B", "volume": "$94B", "sparkline": [1,1,1,1,1]},
    {"rank": 4, "name": "BNB", "symbol": "BNB", "price": "$873", "change_24h": "-1.39%", "change_class": "red", "market_cap": "$120B", "volume": "$829M", "sparkline": [880, 870, 875, 873]},
    {"rank": 5, "name": "Solana", "symbol": "SOL", "price": "$142", "change_24h": "+0.26%", "change_class": "green", "market_cap": "$71B", "volume": "$3.2B", "sparkline": [140, 141, 142]},
    {"rank": 6, "name": "XRP", "symbol": "XRP", "price": "$2.01", "change_24h": "+2.29%", "change_class": "green", "market_cap": "$121B", "volume": "$2.65B", "sparkline": [1.9, 1.95, 2.01]},
    {"rank": 7, "name": "Dogecoin", "symbol": "DOGE", "price": "$0.35", "change_24h": "+3.5%", "change_class": "green", "market_cap": "$51B", "volume": "$2.1B", "sparkline": [0.32, 0.34, 0.35]},
    {"rank": 8, "name": "Cardano", "symbol": "ADA", "price": "$0.85", "change_24h": "-0.8%", "change_class": "red", "market_cap": "$30B", "volume": "$1.2B", "sparkline": [0.86, 0.85]},
    {"rank": 9, "name": "TRON", "symbol": "TRX", "price": "$0.22", "change_24h": "+1.1%", "change_class": "green", "market_cap": "$19B", "volume": "$900M", "sparkline": [0.21, 0.22]},
    {"rank": 10, "name": "Avalanche", "symbol": "AVAX", "price": "$45", "change_24h": "+2.4%", "change_class": "green", "market_cap": "$18B", "volume": "$800M", "sparkline": [43, 44, 45]}
]

@app.route('/')
def home():
    return render_template_string(HTML, crypto_list=crypto_list)

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
        body { margin: 0; font-family: 'Inter', sans-serif; background: #0f172a; color: #e2e8f0; }
        .header { text-align: center; padding: 40px 20px; background: #1e293b; }
        .logo { height: 80px; vertical-align: middle; border-radius: 12px; }
        h1 { display: inline; font-size: 3em; margin-left: 20px; vertical-align: middle; background: linear-gradient(to right, #60a5fa, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th { background: #1e293b; padding: 20px; text-align: left; font-weight: 600; }
        td { padding: 20px; border-bottom: 1px solid #334155; }
        .rank { text-align: center; width: 80px; }
        .name { font-weight: 600; font-size: 1.2em; }
        .price { text-align: right; font-weight: 600; font-size: 1.2em; }
        .change { text-align: right; font-size: 1.1em; }
        .green { color: #10b981; }
        .red { color: #ef4444; }
        .gray { color: #64748b; }
        .chart { height: 60px; width: 150px; }
        .no-data { text-align: center; padding: 100px; color: #64748b; font-size: 1.6em; }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro Logo" class="logo">
        <h1>TradeScout Pro</h1>
    </div>
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
                    <td class="name">{{ coin.name }} <span style="color:#64748b;">{{ coin.symbol }}</span></td>
                    <td class="price">{{ coin.price }}</td>
                    <td class="change {{ coin.change_class }}">{{ coin.change_24h }}</td>
                    <td>{{ coin.market_cap }}</td>
                    <td>{{ coin.volume }}</td>
                    <td><canvas class="chart" id="chart{{ coin.rank }}"></canvas></td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
    <script>
        {% for coin in crypto_list %}
            new Chart(document.getElementById('chart{{ coin.rank }}'), {
                type: 'line',
                data: { labels: ['', '', '', '', '', '', ''], datasets: [{ data: {{ coin.sparkline }}, borderColor: '#3b82f6', backgroundColor: 'rgba(59,130,246,0.1)', fill: true, tension: 0.4, pointRadius: 0 }] },
                options: { responsive: true, plugins: { legend: { display: false } }, scales: { x: { display: false }, y: { display: false } } }
            });
        {% endfor %}
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
