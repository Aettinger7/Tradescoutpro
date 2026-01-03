from flask import Flask
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

# Top 16 cryptos
COINS = [
    "bitcoin", "ethereum", "binancecoin", "ripple", "solana", "cardano",
    "dogecoin", "tron", "avalanche-2", "shiba-inu", "chainlink", "polkadot",
    "litecoin", "bitcoin-cash", "near", "polygon"
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
    "polygon": "https://assets.coingecko.com/coins/images/4713/large/polygon.png"
}

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
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        formatted_data = []
        for coin in COINS:
            info = data.get(coin, {})
            name = coin.replace("-", " ").title()
            if "binancecoin" in coin: name = "BNB"
            if "avalanche-2" in coin: name = "Avalanche"
            
            formatted_data.append({
                "id": coin,
                "name": name,
                "logo": COIN_LOGOS.get(coin, ""),
                "price": info.get("usd", 0),
                "change_24h": round(info.get("usd_24h_change", 0), 2),
                "market_cap": info.get("usd_market_cap", 0) or 0
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
        <div class="crypto-card bg-gray-800/80 backdrop-blur-lg rounded-2xl p-6 border border-gray-700 hover:border-purple-500 transition-all hover:scale-105 cursor-pointer shadow-2xl"
             onclick="openModal('{coin['id']}', '{coin['name']}', {coin['price']}, {coin['change_24h']}, '{change_sign}', '{mcap}', '{coin['logo']}')">
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
            body {{ font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #0f0f1e, #1a0033, #0f0f1e); min-height: 100vh; }}
        </style>
    </head>
    <body class="text-white">
        <div class="container mx-auto px-6 py-10 max-w-7xl">
            <header class="flex justify-between items-center mb-10">
                <div class="flex items-center space-x-5">
                    <!-- YOUR LOGO HERE -->
                    <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro Logo" class="w-16 h-16 rounded-xl shadow-2xl">
                    <h1 class="text-4xl md:text-5xl font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">
                        TradeScout Pro
                    </h1>
                </div>
                <div class="flex items-center space-x-6">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." 
                           class="px-6 py-3 rounded-full bg-gray-800/70 border border-gray-600 focus:border-purple-500 focus:outline-none text-white w-64 transition">
                    <button onclick="document.body.classList.toggle('bg-gray-100'); document.body.classList.toggle('text-black'); this.innerHTML = this.innerHTML === '🌙' ? '☀️' : '🌙'" class="text-3xl hover:scale-110 transition">🌙</button>
                </div>
            </header>
            
            <p class="text-center text-gray-300 text-lg mb-10">
                Live Cryptocurrency Prices • Last updated: {last_update} • Auto-refreshes every minute
            </p>
            
            <div id="cryptoGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
                {cards}
                {status_message}
            </div>
            
            <footer class="text-center mt-20 text-gray-500 text-sm">
                Powered by CoinGecko API • TradeScout Pro © 2026
            </footer>
        </div>
        
        <!-- Modal Popup -->
        <div id="detailModal" class="fixed inset-0 bg-black/90 hidden items-center justify-center z-50" onclick="closeModal()">
            <div class="bg-gray-800/95 backdrop-blur-2xl rounded-3xl p-10 max-w-2xl w-full mx-6 shadow-2xl border border-purple-600/50" onclick="event.stopPropagation()">
                <div class="flex items-center space-x-8 mb-8">
                    <img id="modalLogo" src="" alt="" class="w-24 h-24 rounded-full shadow-xl">
                    <h2 id="modalName" class="text-4xl font-extrabold text-white"></h2>
                </div>
                <div class="text-5xl font-extrabold text-white mb-6" id="modalPrice">$0.00</div>
                <div id="modalChange" class="text-3xl font-bold mb-8"></div>
                <div class="text-xl text-gray-300 mb-10" id="modalMCap"></div>
                
                <!-- Live 7-day Sparkline Chart -->
                <div class="w-full h-48 bg-gray-900/60 rounded-2xl overflow-hidden border border-gray-700">
                    <img id="modalChart" src="" class="w-full h-full object-contain" alt="7-day price chart">
                </div>
                
                <button onclick="closeModal()" class="mt-8 px-8 py-3 bg-purple-600 hover:bg-purple-700 rounded-full text-white font-bold transition">
                    Close
                </button>
            </div>
        </div>
        
        <script>
            // Search
            document.getElementById('searchInput').addEventListener('input', function(e) {{
                const term = e.target.value.toLowerCase();
                document.querySelectorAll('.crypto-card').forEach(card => {{
                    const text = card.textContent.toLowerCase();
                    card.style.display = text.includes(term) ? 'block' : 'none';
                }});
            }});
            
            // Modal
            function openModal(id, name, price, change, sign, mcap, logo) {{
                document.getElementById('modalName').textContent = name;
                document.getElementById('modalPrice').textContent = new Intl.NumberFormat('en-US', {{style: 'currency', currency: 'USD', minimumFractionDigits: 2, maximumFractionDigits: 8}}).format(price);
                const changeEl = document.getElementById('modalChange');
                changeEl.textContent = sign + change + '%';
                changeEl.className = change > 0 ? 'text-green-400 text-3xl font-bold mb-8' : 'text-red-400 text-3xl font-bold mb-8';
                document.getElementById('modalMCap').textContent = 'Market Cap: ' + mcap;
                document.getElementById('modalLogo').src = logo;
                document.getElementById('modalChart').src = 'https://www.coingecko.com/coins/' + id + '/sparkline';
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
