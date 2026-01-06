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
            font-family: 'Helvetica', sans-serif; 
        }
        .light body { 
            background: url('https://img.freepik.com/premium-photo/futuristic-blockchain-technology-background-with-glowing-orange-circuit-board-patterns_980886-2236.jpg?w=2000') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #f0f0f0; 
            color: #000000; 
        }
        .header { 
            background: rgba(0, 0, 0, 0.8); 
            backdrop-filter: blur(10px);
            border-bottom: 3px solid #f7931a;
        }
        .light .header { background: rgba(255,255,255,0.9); }
        .ticker { 
            background: #f7931a; 
            color: #000; 
            font-weight: bold; 
            padding: 0.5rem 0; 
            overflow: hidden; 
        }
        .ticker-item { display: inline-block; padding-right: 2rem; animation: scroll 30s linear infinite; }
        @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .metric-card:hover { box-shadow: 0 0 30px rgba(247, 147, 26, 0.6); }
        .news-card { border: 1px solid #f7931a; }
        .news-card:hover { box-shadow: 0 0 30px rgba(247, 147, 26, 0.5); }
        .x-post-card { border: 1px solid #f7931a; }
        .gradient-text { background: linear-gradient(to right, #f7931a, #ff6600); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .animate-spin-slow { animation: spin 20s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="min-h-screen">
    <div class="ticker">
        <div class="ticker-item">BTC $93,500 (+2.1%) • ETH $3,250 (+1.8%) • SOL $140 (+3.2%) • XRP $2.38 (+11%) • Market Cap $3.3T</div>
    </div>

    <header class="header py-4 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Logo" class="w-10 h-10 animate-spin-slow">
            <div class="text-3xl font-bold gradient-text">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <input id="search-input" type="text" class="px-5 py-2 rounded-full bg-black/50 text-white w-60 focus:ring-2 focus:ring-orange-500 light:bg-white/70 light:text-black" placeholder="Search...">
            <button id="toggle-theme" class="px-5 py-2 rounded-full bg-black/50 hover:bg-orange-600/50 flex items-center gap-2 text-sm font-bold light:bg-white/70 light:text-black">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <h1 class="text-5xl font-bold mb-12 text-center gradient-text">Markets News Hub</h1>

        <!-- Metrics -->
        <div class="grid grid-cols-2 md:grid-cols-5 gap-6 mb-16">
            <!-- Cards as before, compact -->
        </div>

        <!-- Main Content -->
        <div class="grid grid-cols-1 lg:grid-cols-4 gap-10">
            <div class="lg:col-span-3">
                <h2 class="text-3xl font-bold mb-8 gradient-text">Latest News</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- 15+ news cards in grid -->
                </div>
            </div>
            <div>
                <h2 class="text-3xl font-bold mb-8 gradient-text">Trending on X</h2>
                <div class="space-y-8">
                    <!-- 10 X posts -->
                </div>
            </div>
        </div>
    </div>

    <script>
        // Theme, metrics load, news/X arrays (15 news + 10 posts), display functions with clickable links, search filter
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
