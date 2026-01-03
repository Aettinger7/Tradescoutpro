from flask import Flask
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

COINS = ["bitcoin", "ethereum", "solana", "ripple", "cardano", "dogecoin", "litecoin", "polygon"]

# CoinGecko logo URLs (reliable and high-quality)
COIN_LOGOS = {
    "bitcoin": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png",
    "ethereum": "https://assets.coingecko.com/coins/images/279/large/ethereum.png",
    "solana": "https://assets.coingecko.com/coins/images/4128/large/solana.png",
    "ripple": "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png",
    "cardano": "https://assets.coingecko.com/coins/images/975/large/cardano.png",
    "dogecoin": "https://assets.coingecko.com/coins/images/5/large/dogecoin.png",
    "litecoin": "https://assets.coingecko.com/coins/images/2/large/litecoin.png",
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
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        formatted_data = []
        for coin in COINS:
            info = data.get(coin, {})
            formatted_data.append({
                "id": coin,
                "name": coin.capitalize(),
                "symbol": coin.upper(),
                "logo": COIN_LOGOS.get(coin, ""),
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
    
    # Generate card HTML
    cards = ""
    for coin in crypto_data:
        change_class = "text-green-400" if coin["change_24h"] > 0 else "text-red-400"
        change_sign = "+" if coin["change_24h"] > 0 else ""
        market_cap_display = f"${coin['market_cap']:,.0f}" if coin["market_cap"] else "N/A"
        
        cards += f'''
        <div class="crypto-card bg-gray-800/80 backdrop-blur-lg rounded-2xl p-6 border border-gray-700 hover:border-blue-500 transition-all hover:scale-105 cursor-pointer shadow-xl"
             onclick="openModal('{coin['id']}', '{coin['name']}', '${coin['price']:,.2f}', '{coin['change_24h']:.2f}', '{change_sign}', '{market_cap_display}')">
            <div class="flex items-center space-x-4 mb-4">
                <img src="{coin['logo']}" alt="{coin['name']}" class="w-12 h-12 rounded-full">
                <div>
                    <h3 class="text-xl font-bold text-white">{coin['name']}</h3>
                    <p class="text-gray-400 text-sm uppercase">{coin['id']}</p>
                </div>
            </div>
            <div class="text-3xl font-extrabold text-white mb-2">${coin['price']:,.2f}</div>
            <div class="{change_class} text-xl font-bold">{change_sign}{coin['change_24h']:.2f}%</div>
            <div class="text-sm text-gray-400 mt-2">MCap: {market_cap_display}</div>
        </div>
        '''
    
    status_message = '<p class="col-span-full text-center text-red-400 text-2xl">Failed to load data — retrying soon...</p>' if not crypto_data else ""
    
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TradeScout Pro — Live Crypto Prices</title>
        <meta http-equiv="refresh" content="60">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; }}
            .dark-mode {{ background: linear-gradient(135deg, #000000, #0f172a, #1e293b); }}
            .light-mode {{ background: #f8fafc; color: #0f172a; }}
            .light-mode .crypto-card {{ background: rgba(255,255,255,0.9); border-color: #cbd5e1; }}
            .light-mode .text-white {{ color: #0f172a; }}
            .light-mode .text-gray-400 {{ color: #64748b; }}
        </style>
    </head>
    <body class="min-h-screen dark-mode text-white transition-all duration-500">
        <div class="container mx-auto px-6 py-10 max-w-7xl">
            <!-- Header -->
            <header class="flex justify-between items-center mb-10">
                <div class="flex items-center space-x-4">
                    <!-- REPLACE THIS URL WITH YOUR ACTUAL LOGO -->
                    <img src="https://via.placeholder.com/60x60/1e40af/ffffff?text=TS" alt="TradeScout Pro Logo" class="w-12 h-12 rounded-lg">
                    <h1 class="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
                        TradeScout Pro
                    </h1>
                </div>
                
                <div class="flex items-center space-x-6">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." 
                           class="px-6 py-3 rounded-full bg-gray-800/70 border border-gray-700 focus:border-blue-500 focus:outline-none text-white w-64">
                    <button onclick="toggleTheme()" class="p-3 rounded-full bg-gray-800 hover:bg-gray-700 transition">
                        <span id="themeIcon">🌙</span>
                    </button>
                </div>
            </header>
            
            <p class="text-center text-gray-400 text-lg mb-8">
                Live Cryptocurrency Prices • Last updated: {last_update} • Auto-refreshes every minute
            </p>
            
            <!-- Crypto Grid -->
            <div id="cryptoGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
                {cards}
                {status_message}
            </div>
            
            <footer class="text-center mt-16 text-gray-500 text-sm">
                Powered by CoinGecko API • TradeScout Pro © 2026
            </footer>
        </div>
        
        <!-- Modal -->
        <div id="detailModal" class="fixed inset-0 bg-black/80 hidden items-center justify-center z-50" onclick="closeModal()">
            <div class="bg-gray-800 rounded-2xl p-8 max-w-md w-full mx-4" onclick="event.stopPropagation()">
                <h2 id="modalName" class="text-3xl font-bold mb-4"></h2>
                <p class="text-4xl font-extrabold text-blue-400 mb-6" id="modalPrice">$0.00</p>
                <p class="text-2xl mb-4" id="modalChange"></p>
                <p class="text-lg text-gray-400" id="modalMCap"></p>
            </div>
        </div>
        
        <script>
            // Search functionality
            document.getElementById('searchInput').addEventListener('input', function(e) {{
                const term = e.target.value.toLowerCase();
                document.querySelectorAll('.crypto-card').forEach(card => {{
                    const name = card.querySelector('h3').textContent.toLowerCase();
                    const symbol = card.querySelector('p').textContent.toLowerCase();
                    card.style.display = (name.includes(term) || symbol.includes(term)) ? 'block' : 'none';
                }});
            }});
            
            // Theme toggle
            function toggleTheme() {{
                document.body.classList.toggle('light-mode');
                document.body.classList.toggle('dark-mode');
                document.getElementById('themeIcon').textContent = document.body.classList.contains('light-mode') ? '☀️' : '🌙';
            }}
            
            // Modal functions
            function openModal(id, name, price, change, sign, mcap) {{
                document.getElementById('modalName').textContent = name;
                document.getElementById('modalPrice').textContent = '$' + parseFloat(price).toLocaleString();
                const changeEl = document.getElementById('modalChange');
                changeEl.textContent = sign + change + '%';
                changeEl.className = parseFloat(change) > 0 ? 'text-green-400 text-2xl mb-4' : 'text-red-400 text-2xl mb-4';
                document.getElementById('modalMCap').textContent = 'Market Cap: ' + mcap;
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
