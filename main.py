# ... (same imports, CG_API_KEY, COINS, fetch_crypto_data as before)

@app.route('/')
def index():
    # ... (same crypto_data, cards generation as before)

    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <!-- same head as before -->
    </head>
    <body class="text-white">
        <!-- same header, grid, footer as before -->
        
        <div id="detailModal" class="fixed inset-0 bg-black/90 hidden items-center justify-center z-50" onclick="closeModal()">
            <div class="bg-gray-900/95 backdrop-blur-xl rounded-3xl p-8 max-w-lg w-full mx-4 shadow-2xl border border-blue-600/50" onclick="event.stopPropagation()">
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
                
                <!-- Fixed Chart -->
                <div class="w-full h-48 bg-gray-800/50 rounded-2xl overflow-hidden border border-gray-700 p-4">
                    <img id="modalChart" src="" class="w-full h-full object-contain" onerror="this.src='https://via.placeholder.com/400x150?text=Chart+Loading...'" alt="7-day price chart">
                </div>
                
                <button onclick="closeModal()" class="mt-8 px-8 py-3 bg-blue-600 hover:bg-blue-700 rounded-full text-white font-bold transition">
                    Close
                </button>
            </div>
        </div>
        
        <script>
            // ... (search and theme toggle same as before)
            
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
                // Fixed chart URL
                document.getElementById('modalChart').src = 'https://www.coingecko.com/coins/' + id + '/sparkline.svg';
                document.getElementById('detailModal').classList.remove('hidden');
                document.getElementById('detailModal').classList.add('flex');
            }}
            
            // closeModal same
        </script>
    </body>
    </html>
    '''
    
    return html
