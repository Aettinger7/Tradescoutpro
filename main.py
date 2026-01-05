from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/trending')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    is_trending = 'true' if request.path == '/trending' else 'false'
    return render_template_string(HTML_TEMPLATE, last_update=last_update, is_trending=is_trending)

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if is_trending == 'true' %}Trending - {% endif %}TradeScout Pro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
      tailwind.config = { darkMode: 'class' }
    </script>
    <style>
        .hover-row:hover { background-color: #333; cursor: pointer; }
        .light .hover-row:hover { background-color: #eee; }
        .sparkline { height: 60px; width: 140px; }
        .modal { display: none; position: fixed; z-index: 50; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.9); }
        .modal-content { background-color: #1e1e1e; margin: 5% auto; padding: 30px; border-radius: 1rem; width: 90%; max-width: 800px; color: #fff; }
        .light .modal-content { background-color: #fff; color: #000; border: 1px solid #ddd; }
        .close { color: #aaa; float: right; font-size: 32px; font-weight: bold; cursor: pointer; }
        .light .close { color: #333; }
        #modal-sparkline { height: 300px; }
        #toggle-theme { display: flex; align-items: center; gap: 10px; padding: 10px 20px; }
    </style>
</head>
<body class="bg-black text-white transition-all duration-500">
    <header class="bg-blue-600 py-6 px-8 flex justify-between items-center light:bg-blue-500">
        <a href="/" class="flex items-center gap-4 text-white light:text-black">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12">
            <div class="text-4xl font-bold">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-6">
            <a href="/" class="hover:underline text-white light:text-black {% if is_trending == 'true' %}hidden{% endif %}">Home</a>
            <a href="/trending" class="hover:underline text-white light:text-black {% if is_trending != 'true' %}hidden{% endif %}">Home</a>
            <a href="/trending" class="px-5 py-3 rounded-lg bg-blue-700 hover:bg-blue-800 light:bg-blue-600 light:hover:bg-blue-700 text-white {% if is_trending == 'true' %}hidden{% endif %}">Trending</a>
            <input id="search-input" type="text" class="px-6 py-3 rounded-full bg-gray-800 text-white placeholder-gray-400 light:bg-gray-200 light:text-black light:placeholder-gray-600 w-64" placeholder="Search any crypto...">
            <button id="toggle-theme" class="px-6 py-3 bg-gradient-to-r from-gray-700 to-gray-600 rounded-full shadow-lg hover:from-gray-600 hover:to-gray-500 light:from-gray-300 light:to-gray-200 light:hover:from-gray-200 light:hover:to-gray-100 light:text-black font-medium">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark Mode</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-6 py-8">
        {% if is_trending == 'true' %}
        <h1 class="text-4xl font-bold mb-10 text-center">Top 25 Trending Coins (24h Gainers)</h1>
        {% endif %}

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
            <div class="bg-gray-900 p-8 rounded-2xl light:bg-gray-100 shadow-lg">
                <p class="text-gray-400 light:text-gray-600 mb-2">Total Market Cap</p>
                <p id="market-cap" class="text-3xl font-bold">Loading...</p>
                <div class="mt-4 w-full bg-gray-700 rounded-full h-3 light:bg-gray-300">
                    <div id="cap-bar" class="bg-blue-500 h-3 rounded-full transition-all duration-1000" style="width: 0%"></div>
                </div>
            </div>
            <div class="bg-gray-900 p-8 rounded-2xl light:bg-gray-100 shadow-lg">
                <p class="text-gray-400 light:text-gray-600 mb-2">Fear & Greed Index</p>
                <p id="fear-greed" class="text-4xl font-bold">–</p>
                <div class="mt-4 w-full bg-gray-700 rounded-full h-3 light:bg-gray-300">
                    <div id="fg-bar" class="h-3 rounded-full transition-all duration-1000" style="width: 0%"></div>
                </div>
            </div>
            <div class="bg-gray-900 p-8 rounded-2xl light:bg-gray-100 shadow-lg">
                <p class="text-gray-400 light:text-gray-600 mb-2">Altcoin Season</p>
                <p id="alt-season" class="text-3xl font-bold">–</p>
                <div class="mt-4 w-full bg-gray-700 rounded-full h-3 light:bg-gray-300">
                    <div id="alt-bar" class="h-3 rounded-full transition-all duration-1000" style="width: 0%"></div>
                </div>
            </div>
            <div class="bg-gray-900 p-8 rounded-2xl light:bg-gray-100 shadow-lg">
                <p class="text-gray-400 light:text-gray-600 mb-2">BTC Dominance</p>
                <p id="btc-dom" class="text-3xl font-bold">–</p>
                <div class="mt-4 w-full bg-gray-700 rounded-full h-3 light:bg-gray-300">
                    <div id="dom-bar" class="bg-blue-500 h-3 rounded-full transition-all duration-1000" style="width: 0%"></div>
                </div>
            </div>
        </div>

        <div class="overflow-x-auto rounded-2xl bg-gray-800 light:bg-gray-200 shadow-xl">
            <table class="w-full">
                <thead class="bg-gray-700 text-gray-300 text-sm uppercase light:bg-gray-300 light:text-gray-700">
                    <tr>
                        <th class="px-6 py-4 text-left">#</th>
                        <th class="px-6 py-4 text-left">Name</th>
                        <th class="px-6 py-4 text-right">Price</th>
                        <th class="px-6 py-4 text-right">1h %</th>
                        <th class="px-6 py-4 text-right">24h %</th>
                        <th class="px-6 py-4 text-right">7d %</th>
                        <th class="px-6 py-4 text-right">Market Cap</th>
                        <th class="px-6 py-4 text-right">Volume (24h)</th>
                        <th class="px-6 py-4 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody id="crypto-table">
                    <tr>
                        <td colspan="9" class="px-6 py-12 text-center text-gray-400 animate-pulse">
                            Loading live data from CoinGecko...
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <p class="text-center text-gray-500 mt-10 light:text-gray-400">Last update: {{ last_update }} • Powered by CoinGecko</p>
    </div>

    <!-- Modal -->
    <div id="coin-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2 id="modal-title" class="text-3xl font-bold mb-6"></h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8 text-lg">
                <div>
                    <p id="modal-price" class="font-bold text-2xl mb-4"></p>
                    <p id="modal-24h"></p>
                    <p id="modal-market-cap"></p>
                    <p id="modal-volume"></p>
                </div>
                <div>
                    <canvas id="modal-sparkline"></canvas>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Your CoinGecko Demo API Key
        const API_KEY = 'CG-AmnUtrzxMeYvcPeRsWejUaHu';

        // Light/Dark Mode - fully fixed
        const html = document.documentElement;
        const toggleBtn = document.getElementById('toggle-theme');
        const themeIcon = document.getElementById('theme-icon');
        const themeText = document.getElementById('theme-text');

        function setTheme(isDark) {
            if (isDark) {
                html.classList.add('dark');
                html.classList.remove('light');
                themeIcon.textContent = '🌙';
                themeText.textContent = 'Dark Mode';
                localStorage.theme = 'dark';
            } else {
                html.classList.add('light');
                html.classList.remove('dark');
                themeIcon.textContent = '☀️';
                themeText.textContent = 'Light Mode';
                localStorage.theme = 'light';
            }
        }

        // Load saved theme or default to dark
        if (localStorage.theme === 'light') {
            setTheme(false);
        } else {
            setTheme(true);
        }

        toggleBtn.addEventListener('click', () => {
            setTheme(!html.classList.contains('dark'));
        });

        let allCoins = [];
        let currentDisplayCoins = [];

        async function loadMainData() {
            const isTrending = {{ is_trending }};
            try {
                // Parallel fetch for speed
                const [globalRes, fgRes, coinsRes] = await Promise.all([
                    fetch(`https://api.coingecko.com/api/v3/global?x_cg_demo_api_key=${API_KEY}`),
                    fetch('https://api.alternative.me/fng/?limit=1'),
                    fetch(`https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=true&price_change_percentage=1h,24h,7d&x_cg_demo_api_key=${API_KEY}`)
                ]);

                const global = await globalRes.json();
                const fg = await fgRes.json();
                allCoins = await coinsRes.json();

                // Update metrics
                const totalCap = global.data.total_market_cap.usd;
                const btcDom = global.data.market_cap_percentage.btc.toFixed(1);
                const fgValue = fg.data[0].value;
                const altSeason = Math.max(0, Math.min(100, Math.round(100 - btcDom)));

                document.getElementById('market-cap').textContent = '$' + (totalCap / 1e12).toFixed(2) + 'T';
                document.getElementById('cap-bar').style.width = Math.min(100, (totalCap / 5e12) * 100) + '%';

                document.getElementById('btc-dom').textContent = btcDom + '%';
                document.getElementById('dom-bar').style.width = btcDom + '%';

                document.getElementById('fear-greed').textContent = fgValue;
                document.getElementById('fg-bar').style.width = fgValue + '%';
                document.getElementById('fg-bar').className = fgValue < 25 ? 'bg-red-500' : fgValue < 50 ? 'bg-orange-500' : fgValue < 75 ? 'bg-yellow-500' : 'bg-green-500' + ' h-3 rounded-full transition-all duration-1000';

                document.getElementById('alt-season').textContent = altSeason + '/100';
                document.getElementById('alt-bar').style.width = altSeason + '%';
                document.getElementById('alt-bar').className = altSeason < 25 ? 'bg-red-500' : altSeason < 50 ? 'bg-orange-500' : altSeason < 75 ? 'bg-yellow-500' : 'bg-green-500' + ' h-3 rounded-full transition-all duration-1000';

                // Format coins
                allCoins = allCoins.map((coin, i) => ({
                    id: coin.id,
                    rank: i + 1,
                    name: coin.name,
                    symbol: coin.symbol.toUpperCase(),
                    logo: coin.image,
                    price: coin.current_price || 0,
                    change_1h: (coin.price_change_percentage_1h_in_currency || 0).toFixed(2),
                    change_24h: (coin.price_change_percentage_24h_in_currency || 0).toFixed(2),
                    change_7d: (coin.price_change_percentage_7d_in_currency || 0).toFixed(2),
                    market_cap: coin.market_cap || 0,
                    volume_24h: coin.total_volume || 0,
                    sparkline_prices: coin.sparkline_in_7d?.price || []
                }));

                // Display logic
                currentDisplayCoins = isTrending
                    ? allCoins.filter(c => parseFloat(c.change_24h) > 0)
                              .sort((a, b) => parseFloat(b.change_24h) - parseFloat(a.change_24h))
                              .slice(0, 25)
                    : allCoins.slice(0, 100);

                currentDisplayCoins.forEach((c, i) => c.rank = i + 1);
                renderTable(currentDisplayCoins);

            } catch (err) {
                console.error(err);
                document.getElementById('crypto-table').innerHTML = '<tr><td colspan="9" class="px-6 py-12 text-center text-red-500">Failed to load data. Please refresh.</td></tr>';
            }
        }

        function renderTable(coins) {
            const tbody = document.getElementById('crypto-table');
            tbody.innerHTML = '';
            coins.forEach(coin => {
                const tr = document.createElement('tr');
                tr.className = 'hover-row border-b border-gray-700 light:border-gray-300';
                tr.dataset.coin = JSON.stringify(coin);
                const priceFormatted = coin.price.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 8 });
                tr.innerHTML = `
                    <td class="px-6 py-4 text-gray-400 light:text-gray-600">${coin.rank}</td>
                    <td class="px-6 py-4">
                        <div class="flex items-center gap-4">
                            <img src="${coin.logo}" class="w-10 h-10 rounded-full" onerror="this.src='https://via.placeholder.com/40?text=?">
                            <div>
                                <div class="font-bold">${coin.name}</div>
                                <div class="text-gray-500 light:text-gray-400">${coin.symbol}</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4 text-right font-bold">$${priceFormatted}</td>
                    <td class="px-6 py-4 text-right ${parseFloat(coin.change_1h) > 0 ? 'text-green-400' : parseFloat(coin.change_1h) < 0 ? 'text-red-400' : ''}">
                        ${parseFloat(coin.change_1h) !== 0 ? (parseFloat(coin.change_1h) > 0 ? '+' : '') + coin.change_1h + '%' : '–'}
                    </td>
                    <td class="px-6 py-4 text-right ${parseFloat(coin.change_24h) > 0 ? 'text-green-400' : parseFloat(coin.change_24h) < 0 ? 'text-red-400' : ''}">
                        ${parseFloat(coin.change_24h) !== 0 ? (parseFloat(coin.change_24h) > 0 ? '+' : '') + coin.change_24h + '%' : '–'}
                    </td>
                    <td class="px-6 py-4 text-right ${parseFloat(coin.change_7d) > 0 ? 'text-green-400' : parseFloat(coin.change_7d) < 0 ? 'text-red-400' : ''}">
                        ${parseFloat(coin.change_7d) !== 0 ? (parseFloat(coin.change_7d) > 0 ? '+' : '') + coin.change_7d + '%' : '–'}
                    </td>
                    <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">$${coin.market_cap.toLocaleString()}</td>
                    <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">$${coin.volume_24h.toLocaleString()}</td>
                    <td class="px-6 py-4 text-center">
                        <canvas class="sparkline" data-prices='${JSON.stringify(coin.sparkline_prices)}'></canvas>
                    </td>
                `;
                tbody.appendChild(tr);
            });

            // Draw sparklines
            document.querySelectorAll('.sparkline').forEach(canvas => {
                const prices = JSON.parse(canvas.dataset.prices || '[]');
                if (prices.length < 2) return;
                const up = prices[prices.length - 1] >= prices[0];
                new Chart(canvas, {
                    type: 'line',
                    data: { datasets: [{ data: prices, borderColor: up ? '#00ff99' : '#ff4444', tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
                    options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } } }
                });
            });
        }

        // Search - works for ANY crypto (even obscure ones)
        const searchInput = document.getElementById('search-input');
        searchInput.addEventListener('input', async () => {
            const query = searchInput.value.trim();
            if (!query) {
                loadMainData();
                return;
            }

            try {
                const searchRes = await fetch(`https://api.coingecko.com/api/v3/search?query=${encodeURIComponent(query)}&x_cg_demo_api_key=${API_KEY}`);
                const searchData = await searchRes.json();
                const ids = searchData.coins.slice(0, 50).map(c => c.id).join(',');

                if (!ids) {
                    document.getElementById('crypto-table').innerHTML = '<tr><td colspan="9" class="px-6 py-12 text-center text-red-500">No results found</td></tr>';
                    return;
                }

                const marketsRes = await fetch(`https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=${ids}&order=market_cap_desc&sparkline=true&price_change_percentage=1h,24h,7d&x_cg_demo_api_key=${API_KEY}`);
                const results = await marketsRes.json();

                const formatted = results.map((coin, i) => ({
                    id: coin.id,
                    rank: i + 1,
                    name: coin.name,
                    symbol: coin.symbol.toUpperCase(),
                    logo: coin.image,
                    price: coin.current_price || 0,
                    change_1h: (coin.price_change_percentage_1h_in_currency || 0).toFixed(2),
                    change_24h: (coin.price_change_percentage_24h_in_currency || 0).toFixed(2),
                    change_7d: (coin.price_change_percentage_7d_in_currency || 0).toFixed(2),
                    market_cap: coin.market_cap || 0,
                    volume_24h: coin.total_volume || 0,
                    sparkline_prices: coin.sparkline_in_7d?.price || []
                }));

                currentDisplayCoins = formatted;
                renderTable(formatted);
            } catch (err) {
                console.error(err);
            }
        });

        // Modal with real-time price + 7-day sparkline
        const modal = document.getElementById('coin-modal');
        const closeBtn = document.querySelector('.close');
        let modalChart = null;

        document.getElementById('crypto-table').addEventListener('click', async (e) => {
            const row = e.target.closest('tr');
            if (!row || !row.dataset.coin) return;

            const coin = JSON.parse(row.dataset.coin);

            document.getElementById('modal-title').textContent = `${coin.name} (${coin.symbol})`;
            document.getElementById('modal-market-cap').textContent = `Market Cap: $${coin.market_cap.toLocaleString()}`;
            document.getElementById('modal-volume').textContent = `24h Volume: $${coin.volume_24h.toLocaleString()}`;
            document.getElementById('modal-24h').textContent = `24h Change: ${parseFloat(coin.change_24h) > 0 ? '+' : ''}${coin.change_24h}%`;

            // Real-time latest price
            try {
                const priceRes = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${coin.id}&vs_currencies=usd&x_cg_demo_api_key=${API_KEY}`);
                const priceData = await priceRes.json();
                const latestPrice = priceData[coin.id]?.usd || coin.price;
                document.getElementById('modal-price').textContent = `Price: $${latestPrice.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 8})}`;
            } catch {}

            // 7-day sparkline chart in modal
            const ctx = document.getElementById('modal-sparkline').getContext('2d');
            if (modalChart) modalChart.destroy();
            const up = coin.sparkline_prices[coin.sparkline_prices.length - 1] >= coin.sparkline_prices[0];
            modalChart = new Chart(ctx, {
                type: 'line',
                data: {
                    datasets: [{
                        data: coin.sparkline_prices,
                        borderColor: up ? '#00ff99' : '#ff4444',
                        backgroundColor: up ? 'rgba(0, 255, 153, 0.1)' : 'rgba(255, 68, 68, 0.1)',
                        fill: true,
                        tension: 0.4,
                        pointRadius: 0,
                        borderWidth: 3
                    }]
                },
                options: {
                    scales: { x: { display: false }, y: { display: false } },
                    plugins: { legend: { display: false } }
                }
            });

            modal.style.display = 'block';
        });

        closeBtn.onclick = () => {
            modal.style.display = 'none';
            if (modalChart) modalChart.destroy();
        };
        window.onclick = (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
                if (modalChart) modalChart.destroy();
            }
        };

        // Initial load
        loadMainData();
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
