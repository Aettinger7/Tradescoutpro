from flask import Flask, render_template_string
import requests

app = Flask(__name__)

def get_global_metrics():
    try:
        res = requests.get("https://api.coingecko.com/api/v3/global")
        data = res.json()['data']
        total_cap = data['total_market_cap']['usd']
        btc_dom = round(data['market_cap_percentage']['btc'], 1)
        return {
            "total_market_cap": total_cap,
            "btc_dominance": btc_dom,
            "fear_greed": 40,
            "alt_season": 24,
        }
    except:
        return {
            "total_market_cap": 3120000000000,
            "btc_dominance": 58.4,
            "fear_greed": 40,
            "alt_season": 24,
        }

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": True,
        "price_change_percentage": "1h,24h,7d",
    }
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        formatted = []
        for rank, coin in enumerate(data, 1):
            sparkline = coin.get("sparkline_in_7d", {}).get("price", [])
            formatted.append({
                "rank": rank,
                "name": coin["name"],
                "symbol": coin["symbol"].upper(),
                "logo": coin["image"],
                "price": coin["current_price"] or 0,
                "change_1h": round(coin.get("price_change_percentage_1h_in_currency") or 0, 2),
                "change_24h": round(coin.get("price_change_percentage_24h_in_currency") or 0, 2),
                "change_7d": round(coin.get("price_change_percentage_7d_in_currency") or 0, 2),
                "market_cap": coin["market_cap"] or 0,
                "volume_24h": coin["total_volume"] or 0,
                "sparkline_prices": sparkline,
            })
        return formatted
    except:
        return []

@app.route('/')
def index():
    metrics = get_global_metrics()
    data = fetch_crypto_data()
    return render_template_string(HTML_TEMPLATE, data=data, metrics=metrics)

application = app

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { background: #000; color: #fff; }
        .header { background: #0066ff; }
        .card { background: #111; border-radius: 1rem; padding: 1.5rem; text-align: center; }
        .hover-row:hover { background: #222; }
        .sparkline { height: 60px; width: 140px; }
        .text-green { color: #00ff99; }
        .text-red { color: #ff4444; }
    </style>
</head>
<body>
    <header class="header text-white py-6 px-8 flex justify-between items-center">
        <div class="text-4xl font-bold flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12">
            TradeScout Pro
        </div>
        <input type="text" class="px-6 py-3 rounded-full bg-black/50 text-white" placeholder="Search crypto...">
    </header>

    <div class="container mx-auto px-6 py-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <div class="card">
                <p class="text-gray-400">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.0f}".format(metrics.total_market_cap / 1e12) }}T</p>
            </div>
            <div class="card">
                <p class="text-gray-400">Fear & Greed</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-gray-400">Neutral</p>
            </div>
            <div class="card">
                <p class="text-gray-400">Altcoin Season</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}/100</p>
                <p class="text-gray-400">Bitcoin Season</p>
            </div>
            <div class="card">
                <p class="text-gray-400">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ metrics.btc_dominance }}%</p>
            </div>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full">
                <thead class="bg-gray-800 text-gray-300 text-sm uppercase">
                    <tr>
                        <th class="px-6 py-4 text-left">#</th>
                        <th class="px-6 py-4 text-left">Name</th>
                        <th class="px-6 py-4 text-right">Price</th>
                        <th class="px-6 py-4 text-right">1h %</th>
                        <th class="px-6 py-4 text-right">24h %</th>
                        <th class="px-6 py-4 text-right">7d %</th>
                        <th class="px-6 py-4 text-right">Market Cap</th>
                        <th class="px-6 py-4 text-right">Volume(24h)</th>
                        <th class="px-6 py-4 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody>
                    {% for coin in data %}
                    <tr class="hover-row">
                        <td class="px-6 py-4 text-gray-400">{{ coin.rank }}</td>
                        <td class="px-6 py-4">
                            <div class="flex items-center gap-4">
                                <img src="{{ coin.logo }}" class="w-10 h-10 rounded-full">
                                <div>
                                    <div class="font-bold">{{ coin.name }}</div>
                                    <div class="text-gray-500">{{ coin.symbol }}</div>
                                </div>
                            </div>
                        </td>
                        <td class="px-6 py-4 text-right font-bold">${{ "{:.2f}".format(coin.price) }}</td>
                        <td class="px-6 py-4 text-right">
                            {% if coin.change_1h > 0 %}
                            <span class="text-green">+{{ "{:.2f}".format(coin.change_1h) }}%</span>
                            {% elif coin.change_1h < 0 %}
                            <span class="text-red">{{ "{:.2f}".format(coin.change_1h) }}%</span>
                            {% else %}
                            -
                            {% endif %}
                        </td>
                        <td class="px-6 py-4 text-right">
                            {% if coin.change_24h > 0 %}
                            <span class="text-green">+{{ "{:.2f}".format(coin.change_24h) }}%</span>
                            {% elif coin.change_24h < 0 %}
                            <span class="text-red">{{ "{:.2f}".format(coin.change_24h) }}%</span>
                            {% else %}
                            -
                            {% endif %}
                        </td>
                        <td class="px-6 py-4 text-right">
                            {% if coin.change_7d > 0 %}
                            <span class="text-green">+{{ "{:.2f}".format(coin.change_7d) }}%</span>
                            {% elif coin.change_7d < 0 %}
                            <span class="text-red">{{ "{:.2f}".format(coin.change_7d) }}%</span>
                            {% else %}
                            -
                            {% endif %}
                        </td>
                        <td class="px-6 py-4 text-right text-gray-400">${{ "{:,.0f}".format(coin.market_cap) }}</td>
                        <td class="px-6 py-4 text-right text-gray-400">${{ "{:,.0f}".format(coin.volume_24h) }}</td>
                        <td class="px-6 py-4 text-center">
                            <canvas class="sparkline" data-prices="{{ coin.sparkline_prices }}"></canvas>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <script>
        document.querySelectorAll('.sparkline').forEach(canvas => {
            const prices = JSON.parse(canvas.dataset.prices || '[]');
            if (prices.length < 2) return;
            const up = prices[prices.length - 1] >= prices[0];
            new Chart(canvas, {
                type: 'line',
                data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
                options: { responsive: true, scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
            });
        });
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
