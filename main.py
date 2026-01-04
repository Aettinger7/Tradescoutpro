from flask import Flask, render_template_string, jsonify
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

def get_global_metrics():
    try:
        res = requests.get("https://api.coingecko.com/api/v3/global", timeout=15)
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
        "price_change_percentage": "1h,24h,7d",
        "sparkline": True,
    }
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        formatted = []
        for rank, coin in enumerate(data, 1):
            formatted.append({
                "rank": rank,
                "id": coin["id"],
                "name": coin["name"],
                "symbol": coin["symbol"].upper(),
                "logo": coin["image"],
                "price": coin["current_price"] or 0,
                "change_1h": round(coin.get("price_change_percentage_1h_in_currency") or 0, 2),
                "change_24h": round(coin.get("price_change_percentage_24h_in_currency") or 0, 2),
                "change_7d": round(coin.get("price_change_percentage_7d_in_currency") or 0, 2),
                "market_cap": coin["market_cap"] or 0,
                "volume_24h": coin["total_volume"] or 0,
                "sparkline_prices": coin.get("sparkline_in_7d", {}).get("price", []),
            })
        return formatted
    except Exception as e:
        print(e)
        return []

@app.route('/')
@app.route('/trending')
def main():
    metrics = get_global_metrics()
    data = fetch_crypto_data()
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    title = "Top 100 Cryptocurrencies" if request.path == '/' else "Trending Coins"
    return render_template_string(HTML_TEMPLATE, data=data, last_update=last_update, metrics=metrics, title=title)

@app.route('/api/coin_ohlc/<id>')
def coin_ohlc(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}/ohlc"
    params = {"vs_currency": "usd", "days": "30"}
    headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        return jsonify(response.json())
    except:
        return jsonify([])

application = app

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro - {{ title }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { background: #000; color: #fff; font-family: sans-serif; }
        .header { background: #0066ff; }
        .card { background: #111; }
        .text-green { color: #00ff99; }
        .text-red { color: #ff4444; }
        .hover-row:hover { background: #222; }
        .sparkline { height: 60px; width: 140px; }
    </style>
</head>
<body>
    <header class="header text-white py-6 px-8 flex justify-between items-center sticky top-0">
        <a href="/" class="text-4xl font-bold flex items-center gap-4">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12">
            TradeScout Pro
        </a>
        <div class="flex items-center gap-8">
            <a href="/" class="hover:underline">Top 100</a>
            <a href="/trending" class="hover:underline">Trending</a>
            <input type="text" id="searchInput" class="px-6 py-3 rounded-full bg-black/50 text-white" placeholder="Search crypto...">
            <button id="themeToggle">🌙</button>
        </div>
    </header>

    <div class="container mx-auto px-6 py-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <div class="card rounded-xl p-6 text-center">
                <p class="text-gray-400">Total Market Cap</p>
                <p class="text-3xl font-bold">${{ "{:,.0f}".format(metrics.total_market_cap / 1e12) }}T</p>
            </div>
            <div class="card rounded-xl p-6 text-center">
                <p class="text-gray-400">Fear & Greed</p>
                <p class="text-4xl font-bold">{{ metrics.fear_greed }}</p>
                <p class="text-gray-400">Neutral</p>
            </div>
            <div class="card rounded-xl p-6 text-center">
                <p class="text-gray-400">Altcoin Season</p>
                <p class="text-3xl font-bold">{{ metrics.alt_season }}/100</p>
                <p class="text-gray-400">Bitcoin Season</p>
            </div>
            <div class="card rounded-xl p-6 text-center">
                <p class="text-gray-400">BTC Dominance</p>
                <p class="text-3xl font-bold">{{ metrics.btc_dominance }}%</p>
            </div>
        </div>

        <div class="overflow-x-auto rounded-2xl bg-gray-900/50">
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
                <tbody id="tableBody">
                    {% for coin in data %}
                    <tr class="hover-row cursor-pointer" onclick="openModal('{{ coin.id }}')">
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
                        <td class="px-6 py-4 text-right font-bold">${{ "{:,.2f}".format(coin.price) }}</td>
                        <td class="px-6 py-4 text-right">{{ '%+.' ~ '2f'|format(coin.change_1h) }}%</td>
                        <td class="px-6 py-4 text-right">{{ '%+.' ~ '2f'|format(coin.change_24h) }}%</td>
                        <td class="px-6 py-4 text-right">{{ '%+.' ~ '2f'|format(coin.change_7d) }}%</td>
                        <td class="px-6 py-4 text-right text-gray-400">${{ "{:,.0f}".format(coin.market_cap) }}</td>
                        <td class="px-6 py-4 text-right text-gray-400">${{ "{:,.0f}".format(coin.volume_24h) }}</td>
                        <td class="px-6 py-4 text-center"><canvas class="sparkline" data-prices='{{ coin.sparkline_prices|tojson }}'></canvas></td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <div class="fixed inset-0 hidden flex items-center justify-center bg-black/80 z-50" id="modal">
        <div class="bg-gray-900 rounded-2xl p-8 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
            <button class="text-4xl float-right" onclick="document.getElementById('modal').classList.add('hidden')">&times;</button>
            <h2 class="text-3xl font-bold mb-4">30 Day Candlestick Chart</h2>
            <canvas id="detailChart"></canvas>
        </div>
    </div>

    <script>
        let detailChart = null;

        function openModal(id) {
            document.getElementById('modal').classList.remove('hidden');
            fetch(`/api/coin_ohlc/${id}`)
                .then(res => res.json())
                .then(raw => {
                    const candles = raw.map(d => ({ x: d[0], o: d[1], h: d[2], l: d[3], c: d[4] }));
                    if (detailChart) detailChart.destroy();
                    detailChart = new Chart(document.getElementById('detailChart'), {
                        type: 'candlestick',
                        data: { datasets: [{ data: candles }] },
                        options: { responsive: true }
                    });
                });
        }

        document.querySelectorAll('.sparkline').forEach(canvas => {
            const prices = JSON.parse(canvas.dataset.prices || '[]');
            if (prices.length < 2) return;
            const up = prices[prices.length - 1] >= prices[0];
            new Chart(canvas, {
                type: 'line',
                data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
                options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
            });
        });
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
