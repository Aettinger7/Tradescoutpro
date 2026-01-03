from flask import Flask
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

COINS = ["bitcoin", "ethereum", "solana", "ripple", "cardano", "dogecoin", "litecoin", "polygon"]

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(COINS),
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_market_cap": "true",
        "include_24h_vol": "true",
        "x_cg_demo_api_key": CG_API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        formatted_data = []
        for coin in COINS:
            info = data.get(coin, {})
            formatted_data.append({
                "id": coin,
                "name": coin.capitalize(),
                "symbol": coin.upper()[:4],  # Simplified
                "price": info.get("usd", 0),
                "change_24h": info.get("usd_24h_change", 0),
                "market_cap": info.get("usd_market_cap", 0),
                "volume_24h": info.get("usd_24h_vol", 0)
            })
        
        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    
    # Build cards
    cards = ""
    for coin in crypto_data:
        change_class = "text-green-400" if coin["change_24h"] > 0 else "text-red-400"
        change_sign = "+" if coin["change_24h"] > 0 else ""
        
        market_cap_display = f"${coin['market_cap']:,.0f}" if coin["market_cap"] else "N/A"
        
        cards += f"""
        <div class="bg-gray-800/60 backdrop-blur-md rounded-2xl p-6 border border-gray-700 hover:border-gray-600 transition-all hover:scale-105 hover:shadow-2xl shadow-lg">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center space-x-4">
                    <img src="https://assets.coingecko.com/coins/images/{coin['id']}/large/{coin['id']}.png?fallback=https://assets.coingecko.com/coins/images/1/large/bitcoin.png" 
                         alt="{coin['name']}" class="w-12 h-12 rounded-full">
                    <div>
                        <h3 class="text-xl font-bold text-white">{coin['name']}</h3>
                        <p class="text-gray-400 uppercase text-sm">{coin['id']}</p>
                    </div>
                </div>
                <span class="{change_class} text-2xl font-bold">{change_sign}{coin['change_24h']:.2f}%</span>
            </div>
            <div class="text-3xl font-extrabold text-white mb-2">${coin['price']:,.2f}</div>
            <div class="text-sm text-gray-400">MCap: {market_cap_display}</div>
        </div>
        """
    
    status_message = '<p class="text-center text-red-400 text-xl col-span-full">Failed to load data — retrying soon...</p>' if not crypto_data else ""
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en" class="bg-gray-900">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TradeScout Pro — Live Crypto Prices</title>
        <meta http-equiv="refresh" content="60"> <!-- Auto-refresh every 60s -->
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Roboto', sans-serif; }}
            h1 {{ font-family: 'Orbitron', sans-serif; }}
        </style>
    </head>
    <body class="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-gray-900">
        <div class="container mx-auto px-4 py-12 max-w-7xl">
            <header class="text-center mb-12">
                <h1 class="text-5xl md:text-6xl font-bold bg-gradient-to-r from-cyan-400 to-purple-600 bg-clip-text text-transparent mb-4">
                    TradeScout Pro
                </h1>
                <p class="text-xl text-gray-300">Live Cryptocurrency Prices</p>
                <p class="text-gray-400 mt-4">Last updated: {last_update} • Auto-refreshes every minute</p>
            </header>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
                {cards}
                {status_message}
            </div>
            
            <footer class="text-center mt-16 text-gray-500">
                <p>Powered by CoinGecko API • TradeScout Pro © 2026</p>
            </footer>
        </div>
    </body>
    </html>
    """
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
