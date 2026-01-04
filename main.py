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
                "symbol": coin["symbol"].upper(),
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
        change_1h_class = "text-green-500" if coin["change_1h"] > 0 else "text-red-500"
        change_24h_class = "text-green-500" if coin["change_24h"] > 0 else "text-red-500"
        change_7d_class = "text-green-500" if coin["change_7d"] > 0 else "text-red-500"
        change_1h_sign = "+" if coin["change_1h"] > 0 else ""
        change_24h_sign = "+" if coin["change_24h"] > 0 else ""
        change_7d_sign = "+" if coin["change_7d"] > 0 else ""
        mcap = f"${coin['market_cap']:,.0f}" if coin['market_cap'] else "N/A"
        volume = f"${coin['volume_24h']:,.0f}" if coin['volume_24h'] else "N/A"
        supply = f"{coin['circulating_supply']:,.0f} {coin['symbol']}" if coin['circulating_supply'] else "N/A"
        
        table_rows += f'''
        <tr class="hover:bg-gray-50 dark:hover:bg-gray-800/50 transition-colors">
            <td class="py-4 px-6 text-center text-gray-500 dark:text-gray-400">{coin['rank']}</td>
            <td class="py-4 px-6">
                <div class="flex items-center space-x-3">
                    <img src="{coin['logo']}" alt="{coin['name']}" class="w-8 h-8 rounded-full">
                    <div>
                        <div class="font-medium text-gray-900 dark:text-white">{coin['name']}</div>
                        <div class="text-sm text-gray-500 dark:text-gray-400 uppercase">{coin['symbol']}</div>
                    </div>
                </div>
            </td>
            <td class="py-4 px-6 text-right font-medium text-gray-900 dark:text-white">${coin['price']:,.2f}</td>
            <td class="py-4 px-6 text-right {change_1h_class}">{change_1h_sign}{coin['change_1h']}%</td>
            <td class="py-4 px-6 text-right {change_24h_class}">{change_24h_sign}{coin['change_24h']}%</td>
            <td class="py-4 px-6 text-right {change_7d_class}">{change_7d_sign}{coin['change_7d']}%</td>
            <td class="py-4 px-6 text-right text-gray-900 dark:text-white">{mcap}</td>
            <td class="py-4 px-6 text-right text-gray-900 dark:text-white">{volume}</td>
            <td class="py-4 px-6 text-right text-gray-900 dark:text-white">{supply}</td>
            <td class="py-4 px-6">
                <img src="https://www.coingecko.com/coins/{coin['id']}/sparkline.svg" alt="{coin['name']} 7d chart" class="w-32 h-12">
            </td>
        </tr>
        '''
    
    html = f'''
    <!DOCTYPE html>
    <html lang="en" class="scroll-smooth">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TradeScout Pro — Top 100 Cryptocurrencies</title>
        <meta http-equiv="refresh" content="60">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <script>
            tailwind.config = {{
                darkMode: 'class',
                theme: {{
                    extend: {{
                        colors: {{
                            primary: '#0052FF'
                        }}
                    }}
                }}
            }}
        </script>
        <style>
            body {{ font-family: 'Inter', sans-serif; }}
            .table-header {{ position: sticky; top: 0; z-index: 10; }}
        </style>
    </head>
    <body class="bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 transition-colors">
        <!-- Navigation -->
        <nav class="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between items-center h-16">
                    <div class="flex items-center space-x-8">
                        <div class="flex items-center space-x-4">
                            <img src="https://i.ibb.co/tPJ79Fnf/image.png" alt="TradeScout Pro" class="h-10 w-10 rounded-lg">
                            <h1 class="text-2xl font-bold text-primary">TradeScout Pro</h1>
                        </div>
                        <div class="hidden md:flex items-center space-x-8">
                            <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-primary font-medium">Markets</a>
                            <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-primary font-medium">Watchlist</a>
                            <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-primary font-medium">Trending</a>
                        </div>
                    </div>
                    <div class="flex items-center space-x-4">
                        <input type="text" id="searchInput" placeholder="Search cryptos..." class="px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 focus:outline-none focus:border-primary w-64">
                        <button id="themeToggle" class="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition">
                            <span class="text-xl">🌙</span>
                        </button>
                    </div>
                </div>
            </div>
        </nav>
        
        <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div class="text-center mb-8">
                <p class="text-gray-600 dark:text-gray-400">Live cryptocurrency prices • Last updated: {last_update} • Auto-refreshes every minute</p>
            </div>
            
            <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl overflow-hidden">
                <div class="overflow-x-auto">
                    <table class="w-full">
                        <thead class="bg-gray-50 dark:bg-gray-900 table-header">
                            <tr>
                                <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider text-center">#</th>
                                <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Coin</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Price</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">1h</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">24h</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">7d</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Market Cap</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Volume (24h)</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Circulating Supply</th>
                                <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Last 7 Days</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-200 dark:divide-gray-800">
                            {table_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </main>
        
        <footer class="text-center py-8 text-gray-500 dark:text-gray-400 text-sm">
            Powered by CoinGecko API • TradeScout Pro © 2026
        </footer>
        
        <script>
            // Search
            document.getElementById('searchInput').addEventListener('input', function(e) {{
                const term = e.target.value.toLowerCase();
                document.querySelectorAll('tbody tr').forEach(row => {{
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(term) ? '' : 'none';
                }});
            }});
            
            // Theme Toggle
            document.getElementById('themeToggle').addEventListener('click', function() {{
                document.documentElement.classList.toggle('dark-mode');
                this.innerHTML = document.documentElement.classList.contains('dark-mode') ? '☀️' : '🌙';
            }});
        </script>
    </body>
    </html>
    '''
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
