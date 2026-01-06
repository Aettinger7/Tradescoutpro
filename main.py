from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro - Markets News Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .news-card { transition: all 0.3s ease; }
        .news-card:hover { transform: translateY(-8px); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3); }
        .modal { display: none; position: fixed; z-index: 50; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.9); }
        .modal-content { background-color: #1e1e1e; margin: 5% auto; padding: 30px; border-radius: 1rem; width: 90%; max-width: 900px; color: #fff; }
        .light .modal-content { background-color: #fff; color: #000; border: 1px solid #ddd; }
        .close { color: #aaa; float: right; font-size: 32px; font-weight: bold; cursor: pointer; }
        .light .close { color: #333; }
        .sentiment-bullish { @apply text-green-400 font-bold; }
        .sentiment-bearish { @apply text-red-400 font-bold; }
        .sentiment-neutral { @apply text-yellow-400 font-bold; }
    </style>
</head>
<body class="bg-black text-white transition-all duration-500">
    <header class="bg-blue-600 py-6 px-8 flex justify-between items-center light:bg-blue-500">
        <a href="/" class="flex items-center gap-4 text-white light:text-black">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-12 h-12">
            <div class="text-4xl font-bold">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-6">
            <input id="search-input" type="text" class="px-6 py-3 rounded-full bg-gray-800 text-white placeholder-gray-400 light:bg-gray-200 light:text-black light:placeholder-gray-600 w-72" placeholder="Search news...">
            <button id="toggle-theme" class="px-6 py-3 bg-gradient-to-r from-gray-700 to-gray-600 rounded-full shadow-lg hover:from-gray-600 hover:to-gray-500 light:from-gray-300 light:to-gray-200 light:hover:from-gray-200 light:hover:to-gray-100 light:text-black font-medium flex items-center gap-3">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark Mode</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-6 py-8">
        <h1 class="text-4xl font-bold mb-12 text-center">Markets News Hub</h1>

        <!-- Key Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-6 mb-16">
            <div class="bg-gray-900 p-6 rounded-2xl light:bg-gray-100 shadow-xl">
                <p class="text-gray-400 light:text-gray-600 mb-2">Crypto Market Cap</p>
                <p id="crypto-cap" class="text-2xl font-bold">Loading...</p>
            </div>
            <div class="bg-gray-900 p-6 rounded-2xl light:bg-gray-100 shadow-xl">
                <p class="text-gray-400 light:text-gray-600 mb-2">BTC Dominance</p>
                <p id="btc-dom" class="text-2xl font-bold">–</p>
            </div>
            <div class="bg-gray-900 p-6 rounded-2xl light:bg-gray-100 shadow-xl">
                <p class="text-gray-400 light:text-gray-600 mb-2">Fear & Greed</p>
                <p id="fear-greed" class="text-2xl font-bold">–</p>
            </div>
            <div class="bg-gray-900 p-6 rounded-2xl light:bg-gray-100 shadow-xl">
                <p class="text-gray-400 light:text-gray-600 mb-2">S&P 500</p>
                <p id="sp500" class="text-2xl font-bold">Loading...</p>
            </div>
            <div class="bg-gray-900 p-6 rounded-2xl light:bg-gray-100 shadow-xl">
                <p class="text-gray-400 light:text-gray-600 mb-2">Gold Price</p>
                <p id="gold" class="text-2xl font-bold">Loading...</p>
            </div>
        </div>

        <!-- News Feed -->
        <div id="news-feed" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="col-span-full text-center py-20">
                <div class="animate-pulse text-2xl text-gray-400">Loading latest markets news...</div>
            </div>
        </div>
    </div>

    <!-- Modal -->
    <div id="news-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <iframe id="article-frame" class="w-full h-screen border-0 rounded-lg" sandbox="allow-scripts allow-same-origin"></iframe>
        </div>
    </div>

    <script>
        const API_KEY = 'CG-AmnUtrzxMeYvcPeRsWejUaHu';

        // Theme toggle
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

        if (localStorage.theme === 'light') setTheme(false);
        else setTheme(true);

        toggleBtn.addEventListener('click', () => setTheme(!html.classList.contains('dark')));

        async function loadData() {
            try {
                // Metrics
                const globalRes = await fetch(`https://api.coingecko.com/api/v3/global?x_cg_demo_api_key=${API_KEY}`);
                const global = await globalRes.json();
                const cap = global.data.total_market_cap.usd;
                document.getElementById('crypto-cap').textContent = '$' + (cap / 1e12).toFixed(2) + 'T';
                document.getElementById('btc-dom').textContent = global.data.market_cap_percentage.btc.toFixed(1) + '%';

                const fgRes = await fetch('https://api.alternative.me/fng/?limit=1');
                const fg = await fgRes.json();
                document.getElementById('fear-greed').textContent = fg.data[0].value;

                // Placeholder for stocks (real APIs need key - static for now)
                document.getElementById('sp500').textContent = '~6,900';

                // Gold via CoinGecko
                const goldRes = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=gold&vs_currencies=usd&x_cg_demo_api_key=${API_KEY}`);
                const gold = await goldRes.json();
                document.getElementById('gold').textContent = '$' + gold.gold.usd.toLocaleString();

                // News - using a working free crypto/finance news aggregator (CryptoPanic public feed changed, using alternative reliable source)
                const newsRes = await fetch('https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fcointelegraph.com%2Frss');
                const newsData = await newsRes.json();
                const feed = document.getElementById('news-feed');
                feed.innerHTML = '';

                newsData.items.slice(0, 30).forEach(item => {
                    const card = document.createElement('div');
                    card.className = 'news-card bg-gray-900 p-8 rounded-2xl light:bg-gray-100 shadow-xl cursor-pointer';
                    card.onclick = () => {
                        document.getElementById('article-frame').src = item.link;
                        document.getElementById('news-modal').style.display = 'block';
                    };
                    card.innerHTML = `
                        <p class="text-gray-400 text-sm mb-4">${new Date(item.pubDate).toLocaleString()}</p>
                        <h3 class="text-2xl font-bold mb-4">${item.title}</h3>
                        <p class="text-gray-300 light:text-gray-700 line-clamp-3">${item.description.replace(/<[^>]*>/g, '')}</p>
                        <p class="text-blue-400 mt-4">Read more →</p>
                    `;
                    feed.appendChild(card);
                });

            } catch (err) {
                console.error(err);
                document.getElementById('news-feed').innerHTML = '<div class="col-span-full text-center text-red-500 py-20">News load failed — refresh to try again.</div>';
            }
        }

        // Search news
        document.getElementById('search-input').addEventListener('input', async (e) => {
            const query = e.target.value.trim();
            if (!query) {
                loadData();
                return;
            }
            // Simple client-side filter or new fetch - here placeholder
            alert('Search coming soon — type keyword and we\'ll filter news!');
        });

        // Modal
        document.querySelector('.close').onclick = () => document.getElementById('news-modal').style.display = 'none';
        window.onclick = (e) => { if (e.target.id === 'news-modal') document.getElementById('news-modal').style.display = 'none'; };

        loadData();
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
