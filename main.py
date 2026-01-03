from flask import Flask, render_template_string
from time import sleep
import threading
from coingecko import CoinGeckoAPI

app = Flask(__name__)

cg = CoinGeckoAPI()

# Global data
crypto_list = []
last_update = "Loading..."

def update_data():
    global crypto_list, last_update
    while True:
        try:
            data = cg.get_coins_markets(vs_currency='usd', per_page=50, page=1, sparkline=True)
            table = []
            for i, coin in enumerate(data, 1):
                table.append({
                    "rank": i,
                    "name": coin['name'],
                    "symbol": coin['symbol'].upper(),
                    "price": f"${coin['current_price']:.2f}",
                    "change_24h": f"{coin['price_change_percentage_24h']:+.2f}%" if coin['price_change_percentage_24h'] is not None else "N/A",
                    "change_class": "green" if coin['price_change_percentage_24h'] and coin['price_change_percentage_24h'] > 0 else "red",
                    "market_cap": f"${coin['market_cap']:,.0f}",
                    "volume": f"${coin['total_volume']:,.0f}",
                    "sparkline": coin['sparkline_in_7d']['price'] if coin['sparkline_in_7d'] else [coin['current_price']]*50
                })
            crypto_list = table
            last_update = datetime.now().strftime("%b %d, %Y %H:%M")
        except:
            crypto_list = []
        sleep(60)

threading.Thread(target=update_data, daemon=True).start()

@app.route('/')
def home():
    return render_template_string(HTML, crypto_list=crypto_list, last_update=last_update)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #e0e0e0; }
        .header { text-align: left; padding: 15px 25px; background: #121212; display: flex; align-items: center; gap: 10px; }
        .logo { height: 40px; }
        h1 { font-size: 1.4em; margin: 0; color: #ffffff; font-weight: 500; }
        .last-update { text-align: center; color: #808080; margin: 10px 0; font-size: 0.9em; }
        table { width: 100%; border-collapse: collapse; margin: 0 auto; font-size: 0.85em; max-width: 1200px; }
        th { background: #181818; padding: 8px 12px; text-align: left; font-weight: 500; color: #b0b0b0; font-size: 0.9em; }
        td { padding: 8px 12px; border-bottom: 1px solid #242424; text-align: left; font-weight: 400; }
        .rank { width: 40px; text-align: center; color: #b0b0b0; }
        .name { display: flex; align-items: center; gap: 8px; font-weight: 500; color: #ffffff; font-size: 0.95em; }
        .symbol { color: #808080; font-size: 0.85em; }
        .price { text-align: right; color: #ffffff; font-weight: 500; font-size: 0.95em; }
        .change { text-align: right; font-size: 0.9em; }
        .green { color: #00cc88; }
        .red { color: #ff4d4d; }
        .market-cap, .volume { text-align: right; color: #b0b0b0; font-size: 0.9em; }
        .chart { height: 40px; width: 100px; margin: 0 auto; }
        .no-data { text-align: center; padding: 80px; color: #808080; font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro Logo" class="logo">
        <h1>TradeScout Pro</h1>
    </div>
    <div class="last-update">Last updated: {{ last_update }}</div>
    <table>
        <thead>
            <tr>
                <th class="rank">#</th>
                <th>Name</th>
                <th>Price</th>
                <th>24h %</th>
                <th>Market Cap</th>
                <th>Volume</th>
                <th>Last 7 Days</th>
            </tr>
        </thead>
        <tbody>
            {% if crypto_list %}
                {% for coin in crypto_list %}
                    <tr>
                        <td class="rank">{{ coin.rank }}</td>
                        <td class="name">{{ coin.name }} <span class="symbol">{{ coin.symbol }}</span></td>
                        <td class="price">{{ coin.price }}</td>
                        <td class="change {{ coin.change_class }}">{{ coin.change_24h }}</td>
                        <td class="market-cap">{{ coin.market_cap }}</td>
                        <td class="volume">{{ coin.volume }}</td>
                        <td class="chart"><canvas id="chart{{ coin.rank }}"></canvas></td>
                    </tr>
                {% endfor %}
            {% else %}
                <tr><td colspan="7" class="no-data">Loading top 50 cryptocurrencies...</td></tr>
            {% endif %}
        </tbody>
    </table>
    <script>
        {% for coin in crypto_list %}
            new Chart(document.getElementById('chart{{ coin.rank }}'), {
                type: 'line',
                data: {
                    labels: new Array({{ coin.sparkline | length }}).fill(''),
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
