from flask import Flask
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

# Expanded list with base memecoins
COINS = [
    "bitcoin", "ethereum", "binancecoin", "ripple", "solana", "cardano",
    "dogecoin", "tron", "avalanche-2", "shiba-inu", "chainlink", "polkadot",
    "litecoin", "bitcoin-cash", "near", "polygon", "toshi", "doginme", "yuki-2"
]

COIN_LOGOS = {
    "bitcoin": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png",
    "ethereum": "https://assets.coingecko.com/coins/images/279/large/ethereum.png",
    "binancecoin": "https://assets.coingecko.com/coins/images/825/large/bnb-icon2_2x.png",
    "ripple": "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png",
    "solana": "https://assets.coingecko.com/coins/images/4128/large/solana.png",
    "cardano": "https://assets.coingecko.com/coins/images/975/large/cardano.png",
    "dogecoin": "https://assets.coingecko.com/coins/images/5/large/dogecoin.png",
    "tron": "https://assets.coingecko.com/coins/images/1094/large/tron-logo.png",
    "avalanche-2": "https://assets.coingecko.com/coins/images/12559/large/Avalanche_Circle_RedWhite_Trans.png",
    "shiba-inu": "https://assets.coingecko.com/coins/images/11939/large/shiba.png",
    "chainlink": "https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png",
    "polkadot": "https://assets.coingecko.com/coins/images/12171/large/polkadot.png",
    "litecoin": "https://assets.coingecko.com/coins/images/2/large/litecoin.png",
    "bitcoin-cash": "https://assets.coingecko.com/coins/images/780/large/bitcoin-cash-circle.png",
    "near": "https://assets.coingecko.com/coins/images/10365/large/near_icon.png",
    "polygon": "https://assets.coingecko.com/coins/images/4713/large/polygon.png",
    "toshi": "https://assets.coingecko.com/coins/images/31071/large/Toshi.jpg",
    "doginme": "https://assets.coingecko.com/coins/images/35533/large/doginme.jpg",
    "yuki-2": "https://assets.coingecko.com/coins/images/35677/large/YUKI_200x200.png"
}

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ",".join(COINS),
        "order": "market_cap_desc",
        "per_page": len(COINS),
        "page": 1,
        "sparkline": false,
        "price_change_percentage": "24h",
        "locale": "en",
        "x_cg_demo_api_key": CG_API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        formatted_data = []
        for info in data:
            formatted_data.append({
                "id": info['id'],
                "name": info['name'],
                "logo": info['image'],
                "price": info['current_price'] or 0,
                "change_24h": info['price_change_percentage_24h'] or 0,
                "market_cap": info['market_cap'] or 0,
                "volume_24h": info['total_volume'] or 0,
                "high_24h": info['high_24h'] or 0,
                "low_24h": info['low_24h'] or 0,
                "ath": info['ath'] or 0,
                "circulating_supply": info['circulating_supply'] or 0
            })
        
        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update
    
    except Exception as e:
        print(f"Error: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    
    cards = ""
    for coin in crypto_data:
        change_class = "text-green-400" if coin["change_24h"] > 0 else "text-red-400"
        change_sign = "+" if coin["change_24h"] > 0 else ""
        mcap = f"${coin['market_cap']:,.0f}" if coin['market_cap'] > 0 else "N/A"
        
        cards += f'''
        <div class="crypto-card bg-gray-800/80 backdrop-blur-lg rounded-2xl p-6 border border-gray-700 hover:border-blue-500 transition-all hover:scale-105 cursor-pointer shadow-2xl"
             onclick="openModal('{coin['id']}', '{coin['name']}', {coin['price']}, {coin['change_24h']}, '{change_sign}', '{mcap}', '{coin['logo']}', {coin['volume_24h']}, {coin['high_24h']}, {coin['low_24h']}, {coin['ath']}, {coin['circulating_supply']})">
            <div class="flex items-center space-x-4 mb-4">
                <img src="{coin['logo']}" alt="{coin['name']}" class="w-12 h-12 rounded-full shadow-md">
                <div>
                    <h3 class="text-xl font-bold text-white">{coin['name']}</h3>
                </div>
            </div>
            <div class="text-3xl font-extrabold text-white mb-2">${coin['price']:,.2f}</div>
            <div class="{change_class} text-xl font-bold mb-2">{change_sign}{coin['change_24h']}%</div>
            <div class="text-sm text-gray-400">MCap: {mcap}</div>
        </div>
        '''
    
    status_message = '<p class="col-span-full text-center text-red-400 text-2xl mt-20">Failed to load data — retrying soon...</p>' if not crypto_data else ""
    
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TradeScout Pro — Live Crypto Prices</title>
        <meta http-equiv="refresh" content="60">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #000000, #0A2540); min-height: 100vh; }}
            .light-mode {{ background: #f8fafc; color: #0A2540; }}
            .light-mode .crypto-card {{ background: rgba(255,255,255,0.9); border-color: #cbd5e1; }}
            .light-mode .text-white {{ color: #0A2540; }}
            .light-mode .text-gray-400 {{ color: #64748b; }}
            .light-mode .backdrop-blur-lg {{ backdrop-filter: blur(16px); }}
            .light-mode .bg-gray-800/80 {{ background: rgba(248,250,252,0.8); }}
        </style>
    </head>
    <body class="text-white" id="body">
        <div class="container mx-auto px-6 py-10 max-w-7xl">
            <header class="flex justify-between items-center mb-10">
                <div class="flex items-center space-x-4">
                    <img src="https://i.ibb.co/tPJ79Fn/image.png" alt="TradeScout Pro Logo" class="w-14 h-14 rounded-xl shadow-lg">
                    <h1 class="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
                        TradeScout Pro
                    </h1>
                </div>
                
                <div class="flex items-center space-x-6">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." 
                           class="px-6 py-3 rounded-full bg-gray-800/70 border border-gray-700 focus:border-blue-500 focus:outline-none text-white w-64">
                    <button onclick="toggleTheme()" class="p-3 rounded-full bg-gray-800 hover:bg-gray-700 transition text-white">
                        <span id="themeIcon">🌙</span>
                    </button>
                </div>
            </header>
            
            <p class="text-center text-gray-400 text-lg mb-8">
                Live Cryptocurrency Prices • Last updated: {last_update} • Auto-refreshes every minute
            </p>
            
            <div id="cryptoGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
                {cards}
                {status_message}
            </div>
            
            <footer class="text-center mt-16 text-gray-500">
                Powered by CoinGecko API • TradeScout Pro © 2026
            </footer>
        </div>
        
        <!-- Modal -->
        <div id="detailModal" class="fixed inset-0 bg-black/80 hidden items-center justify-center z-50" onclick="closeModal()">
            <div class="bg-gray-800/95 backdrop-blur-xl rounded-3xl p-8 max-w-lg w-full mx-4" onclick="event.stopPropagation()">
                <div class="flex items-center space-x-6 mb-6">
                    <img id="modalLogo" src="" class="w-20 h-20 rounded-full">
                    <h2 id="modalName" class="text-4xl font-bold text-white"></h2>
                </div>
                <p class="text-5xl font-extrabold text-white mb-4" id="modalPrice">$0.00</p>
                <p id="modalChange" class="text-3xl mb-4"></p>
                <p class="text-xl text-gray-400 mb-4" id="modalMCap"></p>
                <p class="text-xl text-gray-400 mb-4" id="modalVolume"></p>
                <p class="text-xl text-gray-400 mb-4" id="modalHigh24h"></p>
                <p class="text-xl text-gray-400 mb-4" id="modalLow24h"></p>
                <p class="text-xl text-gray-400 mb-4" id="modalATH"></p>
                <p class="text-xl text-gray-400 mb-4" id="modalSupply"></p>
                <div class="w-full h-32 bg-gray-900/50 rounded-2xl overflow-hidden">
                    <img id="modalChart" src="" class="w-full h-full object-cover">
                </div>
            </div>
        </div>
        
        <script>
            function toggleTheme() {{
                const body = document.getElementById('body');
                body.classList.toggle('light-mode');
                const icon = document.getElementById('themeIcon');
                icon.textContent = body.classList.contains('light-mode') ? '☀️' : '🌙';
            }}
            
            function openModal(id, name, price, change, sign, mcap, logo, volume, high24h, low24h, ath, supply) {{
                document.getElementById('modalName').textContent = name;
                document.getElementById('modalPrice').textContent = '$' + price.toLocaleString(undefined, {{minimumFractionDigits: 2}});
                const changeEl = document.getElementById('modalChange');
                changeEl.textContent = sign + change + '%';
                changeEl.className = (change > 0) ? 'text-green-400 text-3xl mb-4' : 'text-red-400 text-3xl mb-4';
                document.getElementById('modalMCap').textContent = 'Market Cap: ' + mcap;
                document.getElementById('modalVolume').textContent = '24h Volume: $' + volume.toLocaleString(undefined, {{minimumFractionDigits: 0}});
                document.getElementById('modalHigh24h').textContent = '24h High: $' + high24h.toLocaleString(undefined, {{minimumFractionDigits: 2}});
                document.getElementById('modalLow24h').textContent = '24h Low: $' + low24h.toLocaleString(undefined, {{minimumFractionDigits: 2}});
                document.getElementById('modalATH').textContent = 'All-Time High: $' + ath.toLocaleString(undefined, {{minimumFractionDigits: 2}});
                document.getElementById('modalSupply').textContent = 'Circulating Supply: ' + supply.toLocaleString(undefined, {{minimumFractionDigits: 0}});
                document.getElementById('modalLogo').src = logo;
                document.getElementById('modalChart').src = `https://www.coingecko.com/coins/${id}/sparkline`;
                document.getElementById('detailModal').classList.remove('hidden');
                document.getElementById('detailModal').classList.add('flex');
            }}
            
            function closeModal() {{
                document.getElementById('detailModal').classList.add('hidden');
                document.getElementById('detailModal').classList.remove('flex');
            }}
        </script>
    </body>
    </html>
    '''
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
