from flask import Flask
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

COINS = [
    "bitcoin", "ethereum", "binancecoin", "ripple", "solana", "cardano",
    "dogecoin", "tron", "avalanche-2", "shiba-inu", "chainlink", "polkadot",
    "litecoin", "bitcoin-cash", "near", "polygon",
    "toshi", "degen-base", "based-brett"
]

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ",".join(COINS),
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "price_change_percentage": "24h",
        "x_cg_demo_api_key": CG_API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        formatted_data = []
        for coin in data:
            formatted_data.append({
                "id": coin["id"],
                "name": coin["name"],
                "logo": coin["image"],
                "price": coin["current_price"] or 0,
                "change_24h": round(coin["price_change_percentage_24h"] or 0, 2),
                "market_cap": coin["market_cap"] or 0,
                "volume_24h": coin["total_volume"] or 0,
                "high_24h": coin["high_24h"] or 0,
                "low_24h": coin["low_24h"] or 0,
                "ath": coin["ath"] or 0,
                "circulating_supply": coin["circulating_supply"] or 0
            })
        
        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    
    cards = ""
    for coin in crypto_data:
        change_class = "text-green-400" if coin["change_24h"] > 0 else "text-red-400"
        change_sign = "+" if coin["change_24h"] > 0 else ""
        mcap = f"${coin['market_cap']:,.0f}" if coin['market_cap'] else "N/A"
        
        cards += f'''
        <div class="crypto-card bg-gray-900/90 backdrop-blur-md rounded-2xl p-6 border border-gray-800 hover:border-[#0052FF] transition-all hover:scale-105 cursor-pointer shadow-xl z-20"
             onclick="openModal('{coin['id']}', '{coin['name']}', {coin['price']}, {coin['change_24h']}, '{change_sign}', '{mcap}', '{coin['logo']}', {coin['volume_24h']}, {coin['high_24h']}, {coin['low_24h']}, {coin['ath']}, {coin['circulating_supply']})">
            <div class="flex items-center space-x-4 mb-4">
                <img src="{coin['logo']}" alt="{coin['name']}" class="w-12 h-12 rounded-full flex-shrink-0">
                <h3 class="text-xl font-bold text-white truncate">{coin['name']}</h3>
            </div>
            <div class="text-3xl font-extrabold text-white mb-2">${coin['price']:,.2f}</div>
            <div class="{change_class} text-xl font-bold mb-2">{change_sign}{coin['change_24h']}%</div>
            <div class="text-sm text-gray-400 truncate">MCap: {mcap}</div>
        </div>
        '''
    
    status_message = '<p class="col-span-full text-center text-red-400 text-2xl mt-20 z-20">Failed to load data — retrying soon...</p>' if not crypto_data else ""
    
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>TradeScout Pro — Live Crypto Prices</title>
        <meta http-equiv="refresh" content="60">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; margin: 0; overflow-x: hidden; background: linear-gradient(to right, #000000, #0052FF); min-height: 100vh; }}
            .light-mode {{ background: linear-gradient(to right, #f1f5f9, #e0e7ff) !important; }}
            .light-mode .bg-gray-900\\/90 {{ background: rgba(241,245,249,0.9) !important; }}
            .light-mode .text-white {{ color: #000000 !important; }}
            .light-mode .text-gray-400 {{ color: #64748b !important; }}
        </style>
    </head>
    <body class="text-white">
        <div class="container mx-auto px-4 py-8 max-w-7xl">
            <header class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 mb-10">
                <div class="flex items-center space-x-5">
                    <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro Logo" class="w-16 h-16 rounded-xl shadow-2xl">
                    <h1 class="text-4xl md:text-6xl font-bold bg-gradient-to-r from-[#0052FF] to-[#00C6FF] bg-clip-text text-transparent">
                        TradeScout Pro
                    </h1>
                </div>
                <div class="flex flex-col md:flex-row items-stretch md:items-center gap-4 w-full md:w-auto">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." 
                           class="px-5 py-3 rounded-full bg-gray-900/70 border border-gray-800 focus:border-[#0052FF] focus:outline-none text-white w-full">
                    <button id="themeToggle" class="p-2 rounded-full bg-gray-900 hover:bg-gray-800 transition text-xl">
                        🌙
                    </button>
                    <!-- X (Twitter) Profile Button -->
                    <a href="https://x.com/yourusername" target="_blank" 
                       class="px-6 py-3 bg-[#0052FF] hover:bg-[#0066FF] rounded-full text-white font-bold transition shadow-lg text-center">
                        Follow on X
                    </a>
                    <!-- ToshiMart Website Button -->
                    <a href="https://toshimart.com" target="_blank" 
                       class="px-6 py-3 bg-[#0052FF] hover:bg-[#0066FF] rounded-full text-white font-bold transition shadow-lg text-center">
                        ToshiMart Website
                    </a>
                </div>
            </header>
            
            <p class="text-center text-gray-400 text-base mb-10">
                Live Cryptocurrency Prices • Last updated: {last_update} • Auto-refreshes every minute
            </p>
            
            <div id="cryptoGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {cards}
                {status_message}
            </div>
            
            <footer class="text-center mt-20 text-gray-500 text-sm">
                Powered by CoinGecko API • TradeScout Pro © 2026
            </footer>
        </div>
        
        <!-- Modal and scripts (same as before) -->
        <!-- (full modal and script from previous working version) -->
    </body>
    </html>
    '''
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
