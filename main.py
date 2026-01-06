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
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = { darkMode: 'class' }
    </script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; }
        .light body { background: #f8fafc; }
        .header { background: linear-gradient(to right, #2563eb, #1e40af); }
        .light .header { background: linear-gradient(to right, #60a5fa, #3b82f6); }
        .metric-card { background: rgba(30, 41, 59, 0.85); backdrop-filter: blur(12px); border-radius: 1.5rem; }
        .light .metric-card { background: rgba(255,255,255,0.9); }
        .progress-bar { height: 12px; border-radius: 9999px; background: #1e293b; }
        .light .progress-bar { background: #e2e8f0; }
        .progress-fill { height: 100%; border-radius: 9999px; transition: width 2s ease; }
        .news-card, .x-post-card { background: rgba(30, 41, 59, 0.85); backdrop-filter: blur(12px); border-radius: 1.5rem; transition: all 0.4s; }
        .news-card:hover, .x-post-card:hover { transform: translateY(-10px); box-shadow: 0 25px 50px rgba(0,0,0,0.4); }
        .light .news-card, .light .x-post-card { background: rgba(255,255,255,0.9); }
        .gradient-text { background: linear-gradient(to right, #60a5fa, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .modal-content { background: #1e293b; }
        .light .modal-content { background: #fff; }
    </style>
</head>
<body class="text-slate-100 light:text-slate-800 min-h-screen">
    <header class="header py-10 px-8 flex justify-between items-center shadow-2xl">
        <a href="/" class="flex items-center gap-6">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-16 h-16 rounded-full shadow-xl">
            <div class="text-5xl font-black tracking-tight">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-10">
            <input id="search-input" type="text" class="px-8 py-4 rounded-full bg-white/10 text-white placeholder-white/50 w-96 focus:outline-none focus:ring-4 focus:ring-white/40 text-lg" placeholder="Search markets, news, posts...">
            <button id="toggle-theme" class="px-8 py-4 rounded-full bg-white/10 hover:bg-white/20 flex items-center gap-4 font-bold text-lg">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark Mode</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-16">
        <h1 class="text-6xl font-black mb-20 text-center gradient-text tracking-wide">Markets News Hub</h1>

        <!-- Live Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-10 mb-24">
            <div class="metric-card p-10 text-center shadow-2xl">
                <p class="text-slate-400 light:text-slate-600 text-xl mb-6 font-medium">Crypto Market Cap</p>
                <p id="crypto-cap" class="text-5xl font-black mb-8">Loading...</p>
                <div class="progress-bar"><div id="cap-fill" class="progress-fill bg-gradient-to-r from-cyan-400 to-blue-600" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-10 text-center shadow-2xl">
                <p class="text-slate-400 light:text-slate-600 text-xl mb-6 font-medium">BTC Dominance</p>
                <p id="btc-dom" class="text-5xl font-black mb-8">–</p>
                <div class="progress-bar"><div id="dom-fill" class="progress-fill bg-gradient-to-r from-orange-400 to-amber-600" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-10 text-center shadow-2xl">
                <p class="text-slate-400 light:text-slate-600 text-xl mb-6 font-medium">Fear & Greed Index</p>
                <p id="fear-greed" class="text-5xl font-black mb-8">–</p>
                <div class="progress-bar"><div id="fg-fill" class="progress-fill bg-gradient-to-r from-red-500 via-yellow-500 to-green-500" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-10 text-center shadow-2xl">
                <p class="text-slate-400 light:text-slate-600 text-xl mb-6 font-medium">S&P 500</p>
                <p id="sp500" class="text-5xl font-black mb-8">Loading...</p>
                <div class="progress-bar"><div id="sp-fill" class="progress-fill bg-gradient-to-r from-purple-500 to-pink-600" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-10 text-center shadow-2xl">
                <p class="text-slate-400 light:text-slate-600 text-xl mb-6 font-medium">Gold Price (oz)</p>
                <p id="gold" class="text-5xl font-black mb-8">Loading...</p>
                <div class="progress-bar"><div id="gold-fill" class="progress-fill bg-gradient-to-r from-yellow-400 to-amber-700" style="width:0%"></div></div>
            </div>
        </div>

        <!-- Feeds Placeholder -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-16">
            <div class="lg:col-span-2">
                <h2 class="text-5xl font-black mb-12 gradient-text">Latest News Headlines</h2>
                <div class="text-center py-40 text-3xl text-slate-500 font-medium">Dynamic news feed loading soon...</div>
            </div>
            <div>
                <h2 class="text-5xl font-black mb-12 gradient-text">Popular X Posts</h2>
                <div class="text-center py-40 text-3xl text-slate-500 font-medium">Live X feed coming next...</div>
            </div>
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

        // Load live metrics with meters
        async function loadMetrics() {
            try {
                const [globalRes, fgRes, goldRes] = await Promise.all([
                    fetch(`https://api.coingecko.com/api/v3/global?x_cg_demo_api_key=${API_KEY}`),
                    fetch('https://api.alternative.me/fng/?limit=1'),
                    fetch(`https://api.coingecko.com/api/v3/simple/price?ids=gold&vs_currencies=usd&x_cg_demo_api_key=${API_KEY}`)
                ]);

                const global = await globalRes.json();
                const fg = await fgRes.json();
                const gold = await goldRes.json();

                // Crypto Cap
                const capT = (global.data.total_market_cap.usd / 1e12).toFixed(2);
                document.getElementById('crypto-cap').textContent = '$' + capT + 'T';
                document.getElementById('cap-fill').style.width = Math.min(100, (global.data.total_market_cap.usd / 5e12) * 100) + '%';

                // BTC Dom
                const dom = global.data.market_cap_percentage.btc.toFixed(1);
                document.getElementById('btc-dom').textContent = dom + '%';
                document.getElementById('dom-fill').style.width = dom + '%';

                // Fear & Greed
                const fgValue = fg.data[0].value;
                document.getElementById('fear-greed').textContent = fgValue;
                document.getElementById('fg-fill').style.width = fgValue + '%';

                // S&P 500 (current as of Jan 6, 2026)
                document.getElementById('sp500').textContent = '6,902.05';
                document.getElementById('sp-fill').style.width = '85%';

                // Gold
                document.getElementById('gold').textContent = '$' + gold.gold.usd.toLocaleString();
                document.getElementById('gold-fill').style.width = Math.min(100, (gold.gold.usd / 3000) * 100) + '%';

            } catch (err) {
                console.error(err);
            }
        }

        loadMetrics();
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
