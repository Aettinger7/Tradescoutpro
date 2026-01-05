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
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
    <script>
      tailwind.config = { darkMode: 'class' }
    </script>
    <style>
        .hover-row:hover { background-color: #333; cursor: pointer; }
        .light .hover-row:hover { background-color: #eee; }
        .sparkline { height: 60px; width: 140px; }
        .modal { display: none; position: fixed; z-index: 50; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.8); }
        .modal-content { background-color: #222; margin: 5% auto; padding: 20px; border-radius: 1rem; width: 90%; max-width: 800px; color: #fff; }
        .light .modal-content { background-color: #fff; color: #000; }
        .close { color: #aaa; float: right; font-size: 28px; font-weight: bold; cursor: pointer; }
        .light .close { color: #000; }
        #candle-chart { height: 300px; }
        #toggle-theme { display: flex; align-items: center; gap: 4px; }
    </style>
</head>
<body class="bg-black text-white transition-colors duration-300">
    <header class="bg-blue-600 py-6 px-8 flex justify-between items-center light:bg-blue-500">
        <a href="/" class="flex items-center gap-4 text-white light:text-black">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12">
            <div class="text-4xl font-bold">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-6">
            <a href="/" class="hover:underline text-white light:text-black {% if is_trending == 'true' %}hidden{% endif %}">Home</a>
            <a href="/trending" class="hover:underline text-white light:text-black {% if is_trending != 'true' %}hidden{% endif %}">Home</a>
            <a href="/trending" class="px-4 py-2 rounded hover:bg-blue-700 light:hover:bg-blue-400 text-white light:text-black {% if is_trending == 'true' %}hidden{% endif %}">Trending</a>
            <input id="search-input" type="text" class="px-6 py-3 rounded-full bg-gray-800 text-white light:bg-gray-200 light:text-black" placeholder="Search any crypto...">
            <button id="toggle-theme" class="px-4 py-2 bg-gradient-to-r from-gray-700 to-gray-600 rounded-lg shadow-md hover:from-gray-600 hover:to-gray-500 light:from-gray-300 light:to-gray-200 light:hover:from-gray-200 light:hover:to-gray-100 light:text-black flex items-center gap-2">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark Mode</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-6 py-8">
        {% if is_trending == 'true' %}
        <h1 class="text-3xl font-bold mb-8 text-center">Top 25 Trending Coins (24h Gainers)</h1>
        {% endif %}

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
            <div class="bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Total Market Cap</p>
                <p id="market-cap" class="text-3xl font-bold">Loading...</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-2 light:bg-gray-300">
                    <div id="cap-bar" class="bg-blue-500 h-2 rounded-full" style="width: 0%"></div>
                </div>
            </div>
            <div class="bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Fear & Greed</p>
                <p id="fear-greed" class="text-4xl font-bold">Loading...</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-2 light:bg-gray-300">
                    <div id="fg-bar" class="bg-yellow-500 h-2 rounded-full" style="width: 0%"></div>
                </div>
            </div>
            <div class="bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">Altcoin Season</p>
                <p id="alt-season" class="text-3xl font-bold">Loading...</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-2 light:bg-gray-300">
                    <div id="alt-bar" class="bg-yellow-500 h-2 rounded-full" style="width: 0%"></div>
                </div>
            </div>
            <div class="bg-gray-900 p-6 rounded-xl light:bg-gray-100">
                <p class="text-gray-400 light:text-gray-600">BTC Dominance</p>
                <p id="btc-dom" class="text-3xl font-bold">Loading...</p>
                <div class="mt-2 w-full bg-gray-700 rounded-full h-2 light:bg-gray-300">
                    <div id="dom-bar" class="bg-blue-500 h-2 rounded-full" style="width: 0%"></div>
                </div>
            </div>
        </div>

        <div class="overflow-x-auto rounded-2xl bg-gray-800 light:bg-gray-200">
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
                        <th class="px-6 py-4 text-right">Volume(24h)</th>
                        <th class="px-6 py-4 text-center">Last 7 Days</th>
                    </tr>
                </thead>
                <tbody id="crypto-table">
                    <tr><td colspan="9" class="px-6 py-8 text-center">Loading data from CoinGecko...</td></tr>
                </tbody>
            </table>
        </div>

        <p class="text-center text-gray-500 mt-8 light:text-gray-400">Last update: {{ last_update }} • Powered by CoinGecko</p>
    </div>

    <!-- Modal -->
    <div id="coin-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2 id="modal-name" class="text-2xl font-bold"></h2>
            <p id="modal-symbol" class="text-lg"></p>
            <p id="modal-price" class="text-lg font-bold">Price: Loading...</p>
            <p id="modal-24h" class="text-lg"></p>
            <p id="modal-cap" class="text-lg"></p>
            <div class="mt-4">
                <canvas id="candle-chart"></canvas>
            </div>
        </div>
    </div>

    <script>
        // Theme toggle fix
        const html = document.documentElement;
        const toggleBtn = document.getElementById('toggle-theme');
        const themeIcon = document.getElementById('theme-icon');
        const themeText = document.getElementById('theme-text');
        function updateThemeUI(isDark) {
            if (isDark) {
                themeIcon.textContent = '🌙';
                themeText.textContent = 'Dark Mode';
            } else {
                themeIcon.textContent = '☀️';
                themeText.textContent = 'Light Mode';
            }
        }
        if (localStorage.theme === 'light') {
            html.classList.remove('dark');
            html.classList.add('light');
            updateThemeUI(false);
        } else {
            html.classList.add('dark');
            html.classList.remove('light');
            updateThemeUI(true);
        }
        toggleBtn.addEventListener('click', () => {
            const isDark = html.classList.contains('dark');
            if (isDark) {
                html.classList.remove('dark');
                html.classList.add('light');
                localStorage.theme = 'light';
                updateThemeUI(false);
            } else {
                html.classList.add('dark');
                html.classList.remove('light');
                localStorage.theme = 'dark';
                updateThemeUI(true);
            }
        });

        let allCoins = [];  // Store all loaded coins for search

        async function loadData() {
            const isTrending = {{ is_trending }};
            try {
                // Global metrics
                const globalRes = await fetch('https://api.coingecko.com/api/v3/global');
                const global = await globalRes.json();
                const data = global.data;
                const totalCap = data.total_market_cap.usd;
                const btcDom = data.market_cap_percentage.btc.toFixed(1);

                document.getElementById('market-cap').textContent = '$' + (totalCap / 1e12).toFixed(2) + 'T';
                document.getElementById('cap-bar').style.width = Math.min(100, (totalCap / 5e12 * 100)) + '%';
                document.getElementById('btc-dom').textContent = btcDom + '%';
                document.getElementById('dom-bar').style.width = btcDom + '%';

                // Fear & Greed
                const fgRes = await fetch('https://api.alternative.me/fng/?limit=1');
                const fg = await fgRes.json();
                const fgValue = fg.data[0].value;
                document.getElementById('fear-greed').textContent = fgValue;
                document.getElementById('fg-bar').style.width = fgValue + '%';
                let fgColor = fgValue < 25 ? 'bg-red-500' : fgValue < 50 ? 'bg-orange-500' : fgValue < 75 ? 'bg-yellow-500' : 'bg-green-500';
                document.getElementById('fg-bar').className = fgColor + ' h-2 rounded-full';

                // Alt Season approx
                const altSeason = Math.round(100 - parseFloat(btcDom));
                document.getElementById('alt-season').textContent = altSeason + '/100';
                document.getElementById('alt-bar').style.width = altSeason + '%';
                let altColor = altSeason < 25 ? 'bg-red-500' : altSeason < 50 ? 'bg-orange-500' : altSeason < 75 ? 'bg-yellow-500' : 'bg-green-500';
                document.getElementById('alt-bar').className = altColor + ' h-2 rounded-full';

                // Coins data
                const coinsUrl = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=true&price_change_percentage=1h,24h,7d&locale=en';
                const coinsRes = await fetch(coinsUrl);
                allCoins = await coinsRes.json();

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

                let displayCoins = [...allCoins];
                if (isTrending) {
                    displayCoins = displayCoins.filter(c => parseFloat(c.change_24h) > 0)
                                               .sort((a, b) => parseFloat(b.change_24h) - parseFloat(a.change_24h))
                                               .slice(0, 25);
                    displayCoins.forEach((c, i) => c.rank = i + 1);
                } else {
                    displayCoins = displayCoins.slice(0, 100);
                }

                renderTable(displayCoins);

            } catch (err) {
                console.error(err);
                document.getElementById('crypto-table').innerHTML = '<tr><td colspan="9" class="px-6 py-4 text-center text-red-500">Failed to load data. Check connection and refresh.</td></tr>';
            }
        }

        function renderTable(coins) {
            const tbody = document.getElementById('crypto-table');
            tbody.innerHTML = '';
            coins.forEach(coin => {
                const up1h = parseFloat(coin.change_1h) > 0;
                const up24h = parseFloat(coin.change_24h) > 0;
                const up7d = parseFloat(coin.change_7d) > 0;
                const tr = document.createElement('tr');
                tr.className = 'hover-row border-b border-gray-700 light:border-gray-300';
                tr.dataset.coin = JSON.stringify(coin);
                tr.innerHTML = `
                    <td class="px-6 py-4 text-gray-400 light:text-gray-600">${coin.rank}</td>
                    <td class="px-6 py-4">
                        <div class="flex items-center gap-4">
                            <img src="${coin.logo}" class="w-10 h-10 rounded-full" onerror="this.src='https://via.placeholder.com/40'">
                            <div>
                                <div class="font-bold">${coin.name}</div>
                                <div class="text-gray-500 light:text-gray-400">${coin.symbol}</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4 text-right font-bold">$${coin.price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 8})}</td>
                    <td class="px-6 py-4 text-right ${up1h ? 'text-green-500' : parseFloat(coin.change_1h) < 0 ? 'text-red-500' : ''}">
                        ${parseFloat(coin.change_1h) !== 0 ? (up1h ? '+' : '') + coin.change_1h + '%' : '-'}
                    </td>
                    <td class="px-6 py-4 text-right ${up24h ? 'text-green-500' : parseFloat(coin.change_24h) < 0 ? 'text-red-500' : ''}">
                        ${parseFloat(coin.change_24h) !== 0 ? (up24h ? '+' : '') + coin.change_24h + '%' : '-'}
                    </td>
                    <td class="px-6 py-4 text-right ${up7d ? 'text-green-500' : parseFloat(coin.change_7d) < 0 ? 'text-red-500' : ''}">
                        ${parseFloat(coin.change_7d) !== 0 ? (up7d ? '+' : '') + coin.change_7d + '%' : '-'}
                    </td>
                    <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">$${coin.market_cap.toLocaleString()}</td>
                    <td class="px-6 py-4 text-right text-gray-400 light:text-gray-600">$${coin.volume_24h.toLocaleString()}</td>
                    <td class="px-6 py-4 text-center">
                        <canvas class="sparkline" data-prices='${JSON.stringify(coin.sparkline_prices)}'></canvas>
                    </td>
                `;
                tbody.appendChild(tr);
            });

            // Sparklines
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

        // Search - fetch any crypto using /search
        const searchInput = document.getElementById('search-input');
        searchInput.addEventListener('input', async () => {
            const query = searchInput.value.trim().toLowerCase();
            if (!query) {
                return loadData();  // Reset to default
            }
            try {
                const searchUrl = `https://api.coingecko.com/api/v3/search?query=${encodeURIComponent(query)}`;
                const res = await fetch(searchUrl);
                const searchData = await res.json();
                const coinIds = searchData.coins.slice(0, 50).map(c => c.id);  // Top 50 matches
                if (!coinIds.length) {
                    document.getElementById('crypto-table').innerHTML = '<tr><td colspan="9" class="px-6 py-4 text-center text-red-500">No results found.</td></tr>';
                    return;
                }
                const marketsUrl = `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=${coinIds.join(',')}&order=market_cap_desc&per_page=50&page=1&sparkline=true&price_change_percentage=1h,24h,7d&locale=en`;
                const marketsRes = await fetch(marketsUrl);
                let coins = await marketsRes.json();
                coins = coins.map((coin, i) => ({
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
                renderTable(coins);
            } catch (err) {
                console.error(err);
                document.getElementById('crypto-table').innerHTML = '<tr><td colspan="9" class="px-6 py-4 text-center text-red-500">Search failed. Try again.</td></tr>';
            }
        });

        // Modal with real-time data and candlestick chart
        const modal = document.getElementById('coin-modal');
        const close = document.querySelector('.close');
        document.getElementById('crypto-table').addEventListener('click', async e => {
            const row = e.target.closest('tr');
            if (!row || !row.dataset.coin) return;
            let coin = JSON.parse(row.dataset.coin);
            document.getElementById('modal-name').textContent = coin.name;
            document.getElementById('modal-symbol').textContent = coin.symbol;
            document.getElementById('modal-24h').textContent = '24h Change: ' + (parseFloat(coin.change_24h) > 0 ? '+' : '') + coin.change_24h + '%';
            document.getElementById('modal-cap').textContent = 'Market Cap: $' + coin.market_cap.toLocaleString();

            // Fetch latest price
            try {
                const priceUrl = `https://api.coingecko.com/api/v3/simple/price?ids=${coin.id}&vs_currencies=usd`;
                const priceRes = await fetch(priceUrl);
                const priceData = await priceRes.json();
                document.getElementById('modal-price').textContent = 'Price: $' + (priceData[coin.id]?.usd || coin.price).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 8});
            } catch {}

            // Fetch OHLC for candlestick (1 day, 5-min intervals)
            try {
                const ohlcUrl = `https://api.coingecko.com/api/v3/coins/${coin.id}/ohlc?vs_currency=usd&days=1`;
                const ohlcRes = await fetch(ohlcUrl);
                const ohlc = await ohlcRes.json();
                const chartData = ohlc.map(d => ({
                    x: new Date(d[0]),
                    o: d[1],
                    h: d[2],
                    l: d[3],
                    c: d[4]
                }));

                const ctx = document.getElementById('candle-chart').getContext('2d');
                if (window.candleChart) window.candleChart.destroy();
                window.candleChart = new Chart(ctx, {
                    type: 'candlestick',
                    data: {
                        datasets: [{
                            label: coin.name + ' 24h Candlestick',
                            data: chartData,
                            borderColor: 'rgb(75, 192, 192)',
                            backgroundColor: 'rgba(75, 192, 192, 0.5)'
                        }]
                    },
                    options: {
                        scales: {
                            x: { type: 'time', time: { unit: 'hour' } },
                            y: { beginAtZero: false }
                        }
                    }
                });
            } catch (err) {
                console.error('Chart error:', err);
                document.getElementById('candle-chart').getContext('2d').clearRect(0, 0, 800, 300);
            }

            modal.style.display = 'block';
        });
        close.onclick = () => { modal.style.display = 'none'; if (window.candleChart) window.candleChart.destroy(); };
        window.onclick = e => { if (e.target === modal) { modal.style.display = 'none'; if (window.candleChart) window.candleChart.destroy(); } };

        loadData();
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
