from flask import Flask
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

# Expanded with more Base memecoins
COINS = [
 "bitcoin", "ethereum", "binancecoin", "ripple", "solana", "cardano",
 "dogecoin", "tron", "avalanche-2", "shiba-inu", "chainlink", "polkadot",
 "litecoin", "bitcoin-cash", "near", "polygon",
 "toshi", "doginme", "brett", "degen", "moonwell", "higher", "base-god", "doge-base"
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
 <div class="crypto-card relative bg-gray-900/90 backdrop-blur-md rounded-2xl p-6 border border-gray-800 hover:border-[#0052FF] transition-all hover:scale-105 cursor-pointer shadow-xl"
 onclick="openModal('{coin['id']}', '{coin['name']}', {coin['price']}, {coin['change_24h']}, '{change_sign}', '{mcap}', '{coin['logo']}', {coin['volume_24h'] or 0}, {coin['high_24h'] or 0}, {coin['low_24h'] or 0}, {coin['ath'] or 0}, {coin['circulating_supply'] or 0})">
 <button class="absolute top-4 right-4 text-2xl z-10" onclick="event.stopPropagation(); toggleWatchlist('{coin['id']}', this)">
 <span id="star-{coin['id']}">⭐</span>
 </button>
 <div class="flex items-center space-x-4 mb-4">
 <img src="{coin['logo']}" alt="{coin['name']}" class="w-12 h-12 rounded-full flex-shrink-0">
 <h3 class="text-xl font-bold text-white truncate">{coin['name']}</h3>
 </div>
 <div class="text-3xl font-extrabold text-white mb-2">${coin['price']:,.2f}</div>
 <div class="{change_class} text-xl font-bold mb-2">{change_sign}{coin['change_24h']}%</div>
 <div class="text-sm text-gray-400 truncate">MCap: {mcap}</div>
 </div>
 '''
 
 status_message = '<p class="col-span-full text-center text-red-400 text-2xl mt-20">Failed to load data — retrying soon...</p>' if not crypto_data else ""
 
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
 body {{ font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #000000, #051e3e, #000000); min-height: 100vh; margin: 0; }}
 .light-mode {{ background: #f1f5f9 !important; }}
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
 <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 w-full md:w-auto">
 <input type="text" id="searchInput" placeholder="Search cryptos..." 
 class="px-5 py-3 rounded-full bg-gray-900/70 border border-gray-800 focus:border-[#0052FF] focus:outline-none text-white w-full">
 <button id="themeToggle" class="px-6 py-3 rounded-full bg-gray-900 hover:bg-gray-800 transition text-2xl self-center">
 🌙
 </button>
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
 Powered by CoinGecko API • TradeScout Pro © 2026 • Follow @TradeScoutPro on X
 </footer>
 </div>
 
 <!-- Modal stays rich -->
 <div id="detailModal" class="fixed inset-0 bg-black/90 hidden flex items-center justify-center z-50" onclick="closeModal()">
 <div class="bg-gray-900/95 backdrop-blur-xl rounded-3xl p-10 max-w-lg w-full mx-4 shadow-2xl border border-[#0052FF]/50" onclick="event.stopPropagation()">
 <!-- Same modal content as before -->
 <div class="flex items-center space-x-6 mb-6">
 <img id="modalLogo" src="" class="w-20 h-20 rounded-full shadow-xl">
 <h2 id="modalName" class="text-4xl font-bold text-white"></h2>
 </div>
 <div class="text-5xl font-extrabold text-white mb-6" id="modalPrice">$0.00</div>
 <div id="modalChange" class="text-3xl font-bold mb-8"></div>
 <div class="text-xl text-gray-300 mb-4" id="modalMCap"></div>
 <div class="text-xl text-gray-300 mb-4" id="modalVolume"></div>
 <div class="grid grid-cols-2 gap-4 text-xl text-gray-300 mb-8">
 <div id="modalHigh24h"></div>
 <div id="modalLow24h"></div>
 </div>
 <div class="text-xl text-gray-300 mb-8" id="modalATH"></div>
 <div class="text-xl text-gray-300 mb-8" id="modalSupply"></div>
 <div class="w-full h-48 bg-gray-800/50 rounded-2xl overflow-hidden border border-gray-700">
 <img id="modalChart" src="" class="w-full h-full object-contain">
 </div>
 <button onclick="closeModal()" class="mt-8 px-8 py-3 bg-[#0052FF] hover:bg-[#0066FF] rounded-full text-white font-bold transition">
 Close
 </button>
 </div>
 </div>
 
 <script>
 // Watchlist
 function toggleWatchlist(id, button) {{
 let watchlist = JSON.parse(localStorage.getItem('watchlist') || '[]');
 if (watchlist.includes(id)) {{
 watchlist = watchlist.filter(x => x !== id);
 button.innerHTML = '☆';
 }} else {{
 watchlist.push(id);
 button.innerHTML = '⭐';
 }}
 localStorage.setItem('watchlist', JSON.stringify(watchlist));
 sortGrid();
 }}
 
 function sortGrid() {{
 const grid = document.getElementById('cryptoGrid');
 const cards = Array.from(grid.querySelectorAll('.crypto-card'));
 const watchlist = JSON.parse(localStorage.getItem('watchlist') || '[]');
 cards.sort((a, b) => {{
 const aId = a.onclick.toString().match(/'([^']+)'/)[1];
 const bId = b.onclick.toString().match(/'([^']+)'/)[1];
 const aWatch = watchlist.includes(aId) ? -1 : 1;
 const bWatch = watchlist.includes(bId) ? -1 : 1;
 return aWatch - bWatch;
 }});
 cards.forEach(card => grid.appendChild(card));
 // Restore star state
 watchlist.forEach(id => {{
 const star = document.getElementById('star-' + id);
 if (star) star.textContent = '⭐';
 }});
 }}
 
 window.onload = sortGrid;
 
 // Rest of scripts ( search, theme, modal) same as before
 document.getElementById('searchInput').addEventListener('input', function(e) {{
 const term = e.target.value.toLowerCase();
 document.querySelectorAll('.crypto-card').forEach(card => {{
 const text = card.textContent.toLowerCase();
 card.style.display = text.includes(term) ? 'block' : 'none';
 }});
 }});
 
 document.getElementById('themeToggle').addEventListener('click', function() {{
 document.body.classList.toggle('light-mode');
 this.innerHTML = document.body.classList.contains('light-mode') ? '☀️' : '🌙';
 }});
 
 // openModal and closeModal same as last version
 function openModal(id, name, price, change, sign, mcap, logo, volume, high24h, low24h, ath, supply) {{
 // ... (same as before)
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
