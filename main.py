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
        body { 
            background: #0f172a; /* Deep slate blue - easier on eyes */
            min-height: 100vh;
        }
        .light body { background: #f8fafc; }
        .header { 
            background: linear-gradient(to right, #2563eb, #1d4ed8); 
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        .light .header { background: linear-gradient(to right, #3b82f6, #2563eb); }
        .metric-card { 
            background: rgba(30, 41, 59, 0.9); 
            backdrop-filter: blur(10px);
            border-radius: 1.5rem; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            transition: all 0.3s;
        }
        .metric-card:hover { transform: translateY(-8px); }
        .light .metric-card { 
            background: rgba(255,255,255,0.9); 
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .progress-bar { height: 8px; border-radius: 9999px; background: #334155; overflow: hidden; }
        .light .progress-bar { background: #e2e8f0; }
        .progress-fill { height: 100%; border-radius: 9999px; transition: width 1.5s ease; }
        .news-card { 
            background: rgba(30, 41, 59, 0.9); 
            backdrop-filter: blur(10px);
            border-radius: 1.5rem; 
            transition: all 0.3s;
        }
        .news-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
        .light .news-card { background: rgba(255,255,255,0.9); }
        .x-post-card { 
            background: rgba(15, 23, 42, 0.9); 
            backdrop-filter: blur(10px);
            border-radius: 1.5rem; 
            transition: all 0.3s;
        }
        .x-post-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
        .light .x-post-card { background: rgba(248,250,252,0.9); }
        .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.95); }
        .modal-content { background: #1e293b; margin: 5% auto; padding: 30px; border-radius: 1.5rem; width: 90%; max-width: 1000px; }
        .light .modal-content { background: #fff; }
        .close { color: #cbd5e1; font-size: 36px; cursor: pointer; }
        .light .close { color: #475569; }
    </style>
</head>
<body class="text-white light:text-gray-900">
    <header class="header py-8 px-8 flex justify-between items-center text-white">
        <a href="/" class="flex items-center gap-5">
            <img src="https://i.ibb.co/sJjcKmPs/ttn41attn41attn4.png" alt="Logo" class="w-14 h-14 rounded-full shadow-2xl">
            <div class="text-4xl font-extrabold tracking-tight">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-8">
            <input id="search-input" type="text" class="px-8 py-4 rounded-full bg-white/10 text-white placeholder-white/60 w-96 focus:outline-none focus:ring-4 focus:ring-white/30" placeholder="Search news, posts, or assets...">
            <button id="toggle-theme" class="px-8 py-4 rounded-full bg-white/10 hover:bg-white/20 flex items-center gap-4 font-semibold">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark Mode</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <h1 class="text-5xl font-extrabold mb-16 text-center bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">Markets News Hub</h1>

        <!-- Live Metrics with Progress Meters -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-8 mb-20">
            <div class="metric-card p-8 text-center">
                <p class="text-slate-300 light:text-slate-600 text-lg mb-4">Crypto Market Cap</p>
                <p id="crypto-cap" class="text-4xl font-bold mb-6">Loading...</p>
                <div class="progress-bar">
                    <div id="cap-fill" class="progress-fill bg-gradient-to-r from-blue-500 to-cyan-500" style="width: 0%"></div>
                </div>
            </div>
            <div class="metric-card p-8 text-center">
                <p class="text-slate-300 light:text-slate-600 text-lg mb-4">BTC Dominance</p>
                <p id="btc-dom" class="text-4xl font-bold mb-6">–</p>
                <div class="progress-bar">
                    <div id="dom-fill" class="progress-fill bg-gradient-to-r from-orange-500 to-yellow-500" style="width: 0%"></div>
                </div>
            </div>
            <div class="metric-card p-8 text-center">
                <p class="text-slate-300 light:text-slate-600 text-lg mb-4">Fear & Greed Index</p>
                <p id="fear-greed" class="text-4xl font-bold mb-6">–</p>
                <div class="progress-bar">
                    <div id="fg-fill" class="progress-fill bg-gradient-to-r from-red-500 via-yellow-500 to-green-500" style="width: 0%"></div>
                </div>
            </div>
            <div class="metric-card p-8 text-center">
                <p class="text-slate-300 light:text-slate-600 text-lg mb-4">S&P 500</p>
                <p id="sp500" class="text-4xl font-bold mb-6">Loading...</p>
                <div class="progress-bar">
                    <div id="sp-fill" class="progress-fill bg-gradient-to-r from-purple-500 to-pink-500" style="width: 0%"></div>
                </div>
            </div>
            <div class="metric-card p-8 text-center">
                <p class="text-slate-300 light:text-slate-600 text-lg mb-4">Gold Price (oz)</p>
                <p id="gold" class="text-4xl font-bold mb-6">Loading...</p>
                <div class="progress-bar">
                    <div id="gold-fill" class="progress-fill bg-gradient-to-r from-yellow-400 to-amber-600" style="width: 0%"></div>
                </div>
            </div>
        </div>

        <!-- News & X Posts -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
            <div class="lg:col-span-2">
                <h2 class="text-4xl font-bold mb-8 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">Latest News Headlines</h2>
                <div id="news-feed" class="grid grid-cols-1 gap-8">
                    <div class="text-center py-20">
                        <div class="animate-pulse text-2xl text-slate-400">Loading latest markets news...</div>
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-4xl font-bold mb-8 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">Popular X Posts</h2>
                <div id="x-feed" class="grid grid-cols-1 gap-8">
                    <div class="text-center py-20">
                        <div class="animate-pulse text-2xl text-slate-400">Loading viral market posts...</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Article Modal -->
    <div id="article-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <iframe id="article-frame" class="w-full h-[85vh] rounded-2xl border-0"></iframe>
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

        async function loadMetrics() {
            try {
                // Fetch all live data in parallel
                const [globalRes, fgRes, goldRes] = await Promise.all([
                    fetch(`https://api.coingecko.com/api/v3/global?x_cg_demo_api_key=${API_KEY}`),
                    fetch('https://api.alternative.me/fng/?limit=1'),
                    fetch(`https://api.coingecko.com/api/v3/simple/price?ids=gold&vs_currencies=usd&x_cg_demo_api_key=${API_KEY}`)
                ]);

                const global = await globalRes.json();
                const fg = await fgRes.json();
                const gold = await goldRes.json();

                // Crypto Market Cap
                const cap = global.data.total_market_cap.usd;
                const capT = (cap / 1e12).toFixed(2);
                document.getElementById('crypto-cap').textContent = '$' + capT + 'T';
                const capPercent = Math.min(100, (cap / 5e12) * 100); // Scale to $5T max
                document.getElementById('cap-fill').style.width = capPercent + '%';

                // BTC Dominance
                const dom = global.data.market_cap_percentage.btc.toFixed(1);
                document.getElementById('btc-dom').textContent = dom + '%';
                document.getElementById('dom-fill').style.width = dom + '%';

                // Fear & Greed
                const fgValue = fg.data[0].value;
                document.getElementById('fear-greed').textContent = fgValue;
                document.getElementById('fg-fill').style.width = fgValue + '%';

                // S&P 500 - placeholder (real-time needs paid API; static example)
                document.getElementById('sp500').textContent = '6,900.45';
                document.getElementById('sp-fill').style.width = '75%';

                // Gold Price
                const goldPrice = gold.gold.usd.toLocaleString();
                document.getElementById('gold').textContent = '$' + goldPrice;
                const goldPercent = Math.min(100, (gold.gold.usd / 3000) * 100); // Scale to $3000 max
                document.getElementById('gold-fill').style.width = goldPercent + '%';

            } catch (err) {
                console.error('Metrics load error:', err);
            }
        }

        // Load live metrics on start
        loadMetrics();

        // News & X posts placeholder (we'll expand next)
        document.getElementById('news-feed').innerHTML = '<div class="col-span-full text-center py-32 text-3xl text-slate-500">News feed coming in next update...</div>';
        document.getElementById('x-feed').innerHTML = '<div class="text-center py-32 text-3xl text-slate-500">Popular X posts coming soon...</div>';

        // Modal
        document.querySelector('.close').onclick = () => document.getElementById('article-modal').style.display = 'none';
        window.onclick = (e) => { if (e.target.id === 'article-modal') document.getElementById('article-modal').style.display = 'none'; };
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
