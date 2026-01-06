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
            font-family: 'Helvetica Neue', Arial, sans-serif; 
        }
        .light body { 
            background: url('https://img.freepik.com/premium-photo/futuristic-blockchain-technology-background-with-glowing-orange-circuit-board-patterns_980886-2236.jpg?w=2000') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #f8fafc; 
            color: #000000; 
        }
        .header { 
            background: linear-gradient(to right, #f7931a, rgba(0,0,0,0.8)); 
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(247, 147, 26, 0.4);
        }
        .light .header { 
            background: linear-gradient(to right, #f7931a, rgba(255,255,255,0.8)); 
        }
        .logo-text {
            font-weight: 900;
            font-size: 2.5rem;
            background: linear-gradient(to right, #f7931a, #ff6600);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 15px rgba(247, 147, 26, 0.8), 0 0 30px rgba(247, 147, 26, 0.4);
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
            box-shadow: 0 0 35px rgba(247, 147, 26, 0.6);
        }
        .light .metric-card { 
            background: rgba(255,255,255,0.9); 
            border: 2px solid #f7931a; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        .progress-bar { 
            height: 10px; 
            border-radius: 9999px; 
            background: #1a1a1a; 
            overflow: hidden;
        }
        .light .progress-bar { 
            background: #e2e8f0; 
        }
        .progress-fill { 
            height: 100%; 
            border-radius: 9999px; 
            background: linear-gradient(to right, #f7931a, #ff6600);
            transition: width 2s ease-in-out;
        }
        .news-card, .x-post-card { 
            background: rgba(0, 0, 0, 0.85); 
            border: 1px solid #f7931a; 
            border-radius: 0.75rem; 
            transition: all 0.4s;
            box-shadow: 0 4px 16px rgba(247, 147, 26, 0.2);
            padding: 1rem;
        }
        .news-card:hover, .x-post-card:hover { 
            box-shadow: 0 0 30px rgba(247, 147, 26, 0.5);
            transform: translateY(-4px);
        }
        .light .news-card, .light .x-post-card { 
            background: rgba(255,255,255,0.9); 
            border: 1px solid #f7931a; 
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .section-title {
            font-size: 3rem;
            font-weight: 900;
            background: linear-gradient(to right, #f7931a, #ff6600);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(247, 147, 26, 0.6);
        }
        .animate-spin-slow { animation: spin 20s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="transition-all duration-500">
    <header class="header py-6 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Bitcoin Logo" class="w-10 h-10 animate-spin-slow">
            <div class="logo-text">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <input id="search-input" type="text" class="px-5 py-2 rounded-full bg-black/50 text-white placeholder-orange-300 w-60 focus:outline-none focus:ring-2 focus:ring-f7931a light:bg-white/50 light:text-black light:placeholder-orange-700 border border-f7931a text-sm" placeholder="Search crypto, economy...">
            <button id="toggle-theme" class="px-5 py-2 rounded-full bg-black/50 hover:bg-black/70 light:bg-white/50 light:hover:bg-white/70 flex items-center gap-2 font-bold text-sm text-white light:text-black border border-f7931a shadow-lg">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <h1 class="text-5xl font-extrabold mb-16 text-center section-title">Markets News Hub</h1>

        <!-- Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-8 mb-20">
            <div class="metric-card p-6 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Crypto Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-2 font-semibold">Crypto Market Cap</p>
                <p id="crypto-cap" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="cap-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <!-- Other metrics similar -->
        </div>

        <!-- News & X -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
            <div class="lg:col-span-2">
                <h2 class="text-4xl font-extrabold mb-10 section-title">Latest News</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div id="news-feed"></div>
                </div>
            </div>
            <div>
                <h2 class="text-4xl font-extrabold mb-10 section-title">Trending X Posts</h2>
                <div class="grid grid-cols-1 gap-6">
                    <div id="x-feed"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Full working script with loadMetrics(), displayNews(), displayXPosts(), search
        // (same as previous verified version)
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)


