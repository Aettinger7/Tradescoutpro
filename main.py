from flask import Flask
import requests
import datetime

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "price_change_percentage": "1h,24h,7d",
        "x_cg_demo_api_key": CG_API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        formatted_data = []
        for rank, coin in enumerate(data, 1):
            formatted_data.append({
                "rank": rank,
                "id": coin["id"],
                "name": coin["name"],
                "symbol": coin["symbol"],
                "logo": coin["image"],
                "price": coin["current_price"] or 0,
                "change_1h": round(coin["price_change_percentage_1h_in_currency"] or 0, 2),
                "change_24h": round(coin["price_change_percentage_24h_in_currency"] or 0, 2),
                "change_7d": round(coin["price_change_percentage_7d_in_currency"] or 0, 2),
                "market_cap": coin["market_cap"] or 0,
                "volume_24h": coin["total_volume"] or 0,
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
    
    table_rows = ""
    for coin in crypto_data:
        change_1h_class = "text-green-400" if coin["change_1h"] > 0 else "text-red-400"
        change_24h_class = "text-green-400" if coin["change_24h"] > 0 else "text-red-400"
        change_7d_class = "text-green-400" if coin["change_7d"] > 0 else "text-red-400"
        change_1h_sign = "+" if coin["change_1h"] > 0 else ""
        change_24h_sign = "+" if coin["change_24h"] > 0 else ""
        change_7d_sign = "+" if coin["change_7d"] > 0 else ""
        mcap = f"${coin['market_cap']:,.0f}" if coin['market_cap'] else "N/A"
        volume = f"${coin['volume_24h']:,.0f}" if coin['volume_24h'] else "N/A"
        supply = f"{coin['circulating_supply']:,.0f}" if coin['circulating_supply'] else "N/A"
        
        table_rows += f'''
        <tr class="border-b border-white/10 hover:bg-white/5 transition-all duration-200 cursor-pointer" onclick="openModal('{coin['id']}', '{coin['name']}', {coin['price']}, {coin['change_24h']}, '{change_24h_sign}', '{mcap}', '{coin['logo']}', {coin['volume_24h']}, {coin['high_24h']}, {coin['low_24h']}, {coin['ath']}, {coin['circulating_supply']})">
            <td class="py-6 px-4 text-center text-gray-400">{coin['rank']}</td>
            <td class="py-6 px-4 flex items-center space-x-4">
                <img src="{coin['logo']}" alt="{coin['name']}" class="w-10 h-10 rounded-full">
                <div>
                    <div class="text-white font-bold">{coin['name']}</div>
                    <div class="text-gray-400 text-sm uppercase">{coin['symbol']}</div>
                </div>
            </td>
            <td class="py-6 px-4 text-white font-bold text-right">${coin['price']:,.2f}</td>
            <td class="py-6 px-4 {change_1h_class} text-right">{change_1h_sign}{coin['change_1h']}%</td>
            <td class="py-6 px-4 {change_24h_class} text-right">{change_24h_sign}{coin['change_24h']}%</td>
            <td class="py-6 px-4 {change_7d_class} text-right">{change_7d_sign}{coin['change_7d']}%</td>
            <td class="py-6 px-4 text-white text-right">{mcap}</td>
            <td class="py-6 px-4 text-white text-right">{volume}</td>
            <td class="py-6 px-4 text-white text-right">{supply}</td>
            <td class="py-6 px-4">
                <img src="https://www.coingecko.com/coins/{coin['id']}/sparkline.svg" class="w-32 h-16" alt="{coin['name']} sparkline">
            </td>
        </tr>
        '''
    
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>TradeScout Pro — Live Crypto Prices</title>
        <meta http-equiv="refresh" content="60">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; background: #f1f5f9; min-height: 100vh; margin: 0; color: #0f172a; }}
            .dark-mode {{ background: #0f172a; color: #f1f5f9; }}
            .dark-mode .bg-white/5 {{ background: rgba(255,255,255,0.05) !important; }}
            .dark-mode .text-gray-400 {{ color: #94a3b8 !important; }}
            .dark-mode .border-white/10 {{ border-color: rgba(255,255,255,0.1) !important; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th {{ text-align: left; padding: 16px 24px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.875rem; color: #94a3b8; }}
            tr:hover {{ background: rgba(0, 82, 255, 0.05); }}
            .sticky-header {{ position: sticky; top: 0; background: #f1f5f9; z-index: 10; }}
            .dark-mode .sticky-header {{ background: #0f172a; }}
        </style>
    </head>
    <body>
        <nav class="fixed top-0 left-0 right-0 bg-white/80 backdrop-blur-md border-b border-gray-200 dark:bg-gray-900/80 dark:border-gray-800 z-50">
            <div class="container mx-auto px-6 py-4 flex items-center justify-between">
                <div class="flex items-center space-x-6">
                    <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro Logo" class="w-10 h-10 rounded-full">
                    <h1 class="text-3xl font-bold text-[#0052FF]">
                        TradeScout Pro
                    </h1>
                    <a href="#" class="text-gray-600 hover:text-[#0052FF] dark:text-gray-400 dark:hover:text-[#00D4FF]">
                        Markets
                    </a>
                    <a href="#" class="text-gray-600 hover:text-[#0052FF] dark:text-gray-400 dark:hover:text-[#00D4FF]">
                        Watchlist
                    </a>
                    <a href="#" class="text-gray-600 hover:text-[#0052FF] dark:text-gray-400 dark:hover:text-[#00D4FF]">
                        Trending
                    </a>
                </div>
                <div class="flex items-center space-x-4">
                    <input type="text" id="searchInput" placeholder="Search cryptos..." class="px-4 py-2 rounded-full bg-gray-100 border border-gray-300 focus:border-[#0052FF] focus:outline-none text-gray-900 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:placeholder-gray-500">
                    <button id="themeToggle" class="p-2 rounded-full bg-gray-100 hover:bg-gray-200 dark:bg-gray-800 dark:hover:bg-gray-700 transition text-xl">
                        🌙
                    </button>
                </div>
            </div>
        </nav>
        
        <div class="container mx-auto px-6 py-28 max-w-7xl">
            <p class="text-center text-gray-500 text-base mb-12">
                Live Cryptocurrency Prices • Last updated: {last_update} • Auto-refreshes every minute
            </p>
            
            <table class="bg-white dark:bg-gray-900 rounded-3xl shadow-2xl overflow-hidden">
                <thead class="sticky-header border-b border-gray-200 dark:border-gray-800">
                    <tr>
                        <th>Rank</th>
                        <th>Coin</th>
                        <th class="text-right">Price</th>
                        <th class="text-right">1h</th>
                        <th class="text-right">24h</th>
                        <th class="text-right">7d</th>
                        <th class="text-right">Market Cap</th>
                        <th class="text-right">24h Volume</th>
                        <th class="text-right">Circulating Supply</th>
                        <th class="text-right">Sparkline</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
            
            <footer class="text-center mt-16 text-gray-500 text-sm">
                Powered by CoinGecko API • TradeScout Pro © 2026
            </footer>
        </div>
        
        <div id="detailModal" class="fixed inset-0 bg-black/90 hidden items-center justify-center z-50" onclick="closeModal()">
            <div class="bg-gray-900/95 backdrop-blur-xl rounded-3xl p-10 max-w-lg w-full mx-4 shadow-2xl border border-[#0052FF]/50" onclick="event.stopPropagation()">
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
                
                <div class="w-full h-64 bg-gray-800/50 rounded-2xl overflow-hidden border border-gray-700 p-4">
                    <img id="modalChart" src="" class="w-full h-full object-contain" alt="7-day price chart">
                </div>
                
                <button onclick="closeModal()" class="mt-8 px-8 py-3 bg-[#0052FF] hover:bg-[#0066FF] rounded-full text-white font-bold transition">
                    Close
                </button>
            </div>
        </div>
        
        <script>
            document.getElementById('searchInput').addEventListener('input', function(e) {{
                const term = e.target.value.toLowerCase();
                document.querySelectorAll('tbody tr').forEach(row => {{
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(term) ? '' : 'none';
                }});
            }});
            
            document.getElementById('themeToggle').addEventListener('click', function() {{
                document.body.classList.toggle('dark-mode');
                this.innerHTML = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
            }});
            
            function openModal(id, name, price, change, sign, mcap, logo, volume, high24h, low24h, ath, supply) {{
                document.getElementById('modalName').textContent = name;
                document.getElementById('modalPrice').textContent = new Intl.NumberFormat('en-US', {{style: 'currency', currency: 'USD', minimumFractionDigits: 2, maximumFractionDigits: 8}}).format(price);
                const changeEl = document.getElementById('modalChange');
                changeEl.textContent = sign + change + '%';
                changeEl.className = change > 0 ? 'text-green-400 text-3xl font-bold mb-8' : 'text-red-400 text-3xl font-bold mb-8';
                document.getElementById('modalMCap').textContent = 'Market Cap: ' + mcap;
                document.getElementById('modalVolume').textContent = '24h Volume: $' + volume.toLocaleString();
                document.getElementById('modalHigh24h').textContent = '24h High: $' + high24h.toLocaleString(undefined, {{minimumFractionDigits: 2}});
                document.getElementById('modalLow24h').textContent = '24h Low: $' + low24h.toLocaleString(undefined, {{minimumFractionDigits: 2}});
                document.getElementById('modalATH').textContent = 'All-Time High: $' + ath.toLocaleString(undefined, {{minimumFractionDigits: 2}});
                document.getElementById('modalSupply').textContent = 'Circulating Supply: ' + supply.toLocaleString();
                document.getElementById('modalLogo').src = logo;
                document.getElementById('modalChart').src = 'https://www.coingecko.com/coins/' + id + '/sparkline.svg';
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
