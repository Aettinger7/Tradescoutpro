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
            background: url('https://img.freepik.com/premium-photo/futuristic-blockchain-technology-background-with-glowing-orange-circuit-board-patterns_980886-2236.jpg?w=2000') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #000000; 
            color: #ffffff; 
            font-family: 'Arial', sans-serif; 
        }
        .light body { 
            background: url('https://img.freepik.com/premium-photo/futuristic-blockchain-technology-background-with-glowing-orange-circuit-board-patterns_980886-2236.jpg?w=2000') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #f8fafc; 
            color: #000000; 
        }
        .header { 
            background: linear-gradient(to right, #f7931a, #000000); 
            box-shadow: 0 4px 20px rgba(247, 147, 26, 0.5);
        }
        .light .header { 
            background: linear-gradient(to right, #f7931a, #ffffff); 
        }
        .metric-card { 
            background: rgba(0, 0, 0, 0.8); 
            border: 2px solid #f7931a; 
            border-radius: 1rem; 
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.3);
            transition: all 0.4s;
            padding: 1.5rem; 
        }
        .metric-card:hover { 
            box-shadow: 0 0 30px rgba(247, 147, 26, 0.5); 
        }
        .light .metric-card { 
            background: rgba(255,255,255,0.8); 
            border: 2px solid #f7931a; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        .progress-bar { 
            height: 8px; 
            border-radius: 9999px; 
            background: #1a1a1a; 
            overflow: hidden;
        }
        .light .progress-bar { 
            background: #e0e0e0; 
        }
        .progress-fill { 
            height: 100%; 
            border-radius: 9999px; 
            background: linear-gradient(to right, #f7931a, #ff6600);
            transition: width 2s ease-in-out;
        }
        .news-card, .x-post-card { 
            background: rgba(0, 0, 0, 0.85); 
            border: 2px solid #f7931a; 
            border-radius: 1rem; 
            transition: all 0.4s;
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.2);
            padding: 1.5rem; 
        }
        .news-card:hover, .x-post-card:hover { 
            box-shadow: 0 0 40px rgba(247, 147, 26, 0.5);
            transform: translateY(-5px);
        }
        .light .news-card, .light .x-post-card { 
            background: rgba(255,255,255,0.85); 
            border: 2px solid #f7931a; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        }
        .gradient-text { 
            background: linear-gradient(to right, #f7931a, #ff6600); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            animation: pulse 2s infinite; 
        }
        @keyframes pulse { 
            0% { opacity: 1; } 
            50% { opacity: 0.7; } 
            100% { opacity: 1; } 
        }
        .modal { 
            display: none; 
            position: fixed; 
            z-index: 1000; 
            left: 0; 
            top: 0; 
            width: 100%; 
            height: 100%; 
            background-color: rgba(0,0,0,0.95); 
        }
        .modal-content { 
            background: #1a1a1a; 
            margin: 5% auto; 
            padding: 40px; 
            border-radius: 2rem; 
            width: 90%; 
            max-width: 1200px; 
            color: #ffffff; 
            border: 2px solid #f7931a;
            box-shadow: 0 16px 64px rgba(247, 147, 26, 0.5);
        }
        .light .modal-content { 
            background: #ffffff; 
            color: #000000; 
            border: 2px solid #f7931a; 
            box-shadow: 0 16px 64px rgba(0,0,0,0.2);
        }
        .close { 
            color: #f7931a; 
            font-size: 40px; 
            cursor: pointer; 
        }
        .light .close { 
            color: #000000; 
        }
        .animate-spin-slow { animation: spin 20s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="transition-all duration-500">
    <header class="header py-6 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Bitcoin Logo" class="w-10 h-10 animate-spin-slow">
            <div class="text-3xl font-extrabold gradient-text">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <input id="search-input" type="text" class="px-5 py-2 rounded-full bg-black/50 text-white placeholder-orange-300 w-60 focus:outline-none focus:ring-2 focus:ring-f7931a light:bg-white/50 light:text-black light:placeholder-orange-700 border border-f7931a text-sm" placeholder="Search...">
            <button id="toggle-theme" class="px-5 py-2 rounded-full bg-black/50 hover:bg-black/70 light:bg-white/50 light:hover:bg-white/70 flex items-center gap-2 font-bold text-sm text-white light:text-black border border-f7931a shadow-lg">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <h1 class="text-5xl font-extrabold mb-12 text-center gradient-text">Markets News Hub</h1>

        <!-- Live Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-6 mb-16">
            <div class="metric-card p-4 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Crypto Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-1">Crypto Market Cap</p>
                <p id="crypto-cap" class="text-2xl font-bold mb-2 gradient-text">Loading...</p>
                <div class="progress-bar"><div id="cap-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-4 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="BTC Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-1">BTC Dominance</p>
                <p id="btc-dom" class="text-2xl font-bold mb-2 gradient-text">–</p>
                <div class="progress-bar"><div id="dom-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-4 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Fear Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-1">Fear & Greed</p>
                <p id="fear-greed" class="text-2xl font-bold mb-2 gradient-text">–</p>
                <div class="progress-bar"><div id="fg-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-4 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="S&P Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-1">S&P 500</p>
                <p id="sp500" class="text-2xl font-bold mb-2 gradient-text">Loading...</p>
                <div class="progress-bar"><div id="sp-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-4 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Gold Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-1">Gold Price</p>
                <p id="gold" class="text-2xl font-bold mb-2 gradient-text">Loading...</p>
                <div class="progress-bar"><div id="gold-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
        </div>

        <!-- News & X Posts -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
            <div class="lg:col-span-2">
                <h2 class="text-4xl font-extrabold mb-8 gradient-text">Latest News</h2>
                <div id="news-feed" class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <p class="text-center text-orange-400">Loading news...</p>
                </div>
            </div>
            <div>
                <h2 class="text-4xl font-extrabold mb-8 gradient-text">Trending X Posts</h2>
                <div id="x-feed" class="space-y-6">
                    <p class="text-center text-orange-400">Loading posts...</p>
                </div>
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
                themeText.textContent = 'Dark';
                localStorage.theme = 'dark';
            } else {
                html.classList.add('light');
                html.classList.remove('dark');
                themeIcon.textContent = '☀️';
                themeText.textContent = 'Light';
                localStorage.theme = 'light';
            }
        }

        if (localStorage.theme === 'light') setTheme(false);
        else setTheme(true);

        toggleBtn.addEventListener('click', () => setTheme(!html.classList.contains('dark')));

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

                document.getElementById('crypto-cap').textContent = '$' + (global.data.total_market_cap.usd / 1e12).toFixed(2) + 'T';
                document.getElementById('cap-fill').style.width = Math.min(100, (global.data.total_market_cap.usd / 5e12) * 100) + '%';

                const dom = global.data.market_cap_percentage.btc.toFixed(1);
                document.getElementById('btc-dom').textContent = dom + '%';
                document.getElementById('dom-fill').style.width = dom + '%';

                const fgValue = fg.data[0].value;
                document.getElementById('fear-greed').textContent = fgValue;
                document.getElementById('fg-fill').style.width = fgValue + '%';

                document.getElementById('sp500').textContent = '6,902.05';
                document.getElementById('sp-fill').style.width = '98%';

                document.getElementById('gold').textContent = '$' + gold.gold.usd.toLocaleString();
                document.getElementById('gold-fill').style.width = Math.min(100, (gold.gold.usd / 3000) * 100) + '%';

            } catch (err) {
                console.error(err);
            }
        }

        loadMetrics();

        // Placeholder content until dynamic
        const news = [
            { title: "Bitcoin starts 2026 strong with new highs", link: "#" },
            { title: "Morgan Stanley launches Bitcoin ETF", link: "#" },
            // ... more
        ];

        const xPosts = [
            { author: "@CryptoKing", content: "BTC to $100k soon!", url: "#" },
            // ... more
        ];

        // Display functions as before
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)


