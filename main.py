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
        <div class="crypto-card group bg-gray-900/60 backdrop-blur-xl rounded-3xl p-8 border border-white/10 hover:border-[#0052FF]/60 transition-all duration-300 shadow-2xl hover:shadow-[#0052FF]/30 hover:-translate-y-2 cursor-pointer">
            <div class="flex items-center justify-between mb-6">
                <div class="flex items-center space-x-4">
                    <img src="{coin['logo']}" alt="{coin['name']}" class="w-16 h-16 rounded-full ring-4 ring-white/20">
                    <h3 class="text-2xl font-bold text-white">{coin['name']}</h3>
                </div>
            </div>
            <div class="text-4xl font-extrabold text-white mb-3">${coin['price']:,.2f}</div>
            <div class="{change_class} text-2xl font-bold mb-4">{change_sign}{coin['change_24h']}%</div>
            <div class="text-gray-400">MCap: {mcap}</div>
        </div>
        '''
    
    status_message = '<p class="col-span-full text-center text-red-400 text-3xl mt-32">Failed to load data — retrying soon...</p>' if not crypto_data else ""
    
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>TradeScout Pro — Live Crypto Prices</title>
        <meta http-equiv="refresh" content="60">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #000000, #001a33); min-height: 100vh; margin: 0; }}
            h1 {{ font-family: 'Orbitron', sans-serif; }}
            .light-mode {{ background: linear-gradient(135deg, #f8fafc, #e2e8f0) !important; }}
            .light-mode .bg-gray-900\\/60 {{ background: rgba(241,245,249,0.8) !important; }}
            .light-mode .text-white {{ color: #000000 !important; }}
            .light-mode .text-gray-400 {{ color: #64748b !important; }}
        </style>
    </head>
    <body class="text-white">
        <div class="container mx-auto px-6 py-12 max-w-7xl">
            <!-- Header -->
            <header class="flex flex-col lg:flex-row justify-between items-center mb-16">
                <div class="flex items-center space-x-6 mb-8 lg:mb-0">
                    <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro Logo" class="w-20 h-20 rounded-2xl shadow-2xl">
                    <h1 class="text-5xl lg:text-7xl font-black bg-gradient-to-r from-[#0052FF] to-[#00D4FF] bg-clip-text text-transparent">
                        TradeScout Pro
                    </h1>
                </div>
                <div class="flex flex-col sm:flex-row items-center gap-6">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." 
                           class="w-full sm:w-96 px-8 py-4 rounded-full bg-white/10 backdrop-blur-md border border-white/20 focus:border-[#0052FF] focus:outline-none text-white text-lg">
                    <button id="themeToggle" class="p-4 rounded-full bg-white/10 backdrop-blur-md hover:bg-white/20 transition text-2xl">
                        🌙
                    </button>
                </div>
            </header>
            
            <p class="text-center text-gray-400 text-xl mb-12">
                Live Cryptocurrency Prices • Last updated: {last_update} • Auto-refreshes every minute
            </p>
            
            <div id="cryptoGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
                {cards}
                {status_message}
            </div>
            
            <footer class="text-center mt-32 text-gray-500 text-sm">
                Powered by CoinGecko API • TradeScout Pro © 2026
            </footer>
        </div>
        
        <!-- Modal (same as before) -->
        <!-- (full modal code from previous version) -->
        
        <script>
            // (same search, theme toggle, openModal, closeModal as before)
        </script>
    </body>
    </html>
    '''
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
