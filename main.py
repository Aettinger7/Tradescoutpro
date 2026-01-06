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
            background: linear-gradient(to right, #f7931a, rgba(0,0,0,0.8)); 
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.4);
        }
        .light .header { 
            background: linear-gradient(to right, #f7931a, rgba(255,255,255,0.8)); 
        }
        .metric-card { 
            background: rgba(0, 0, 0, 0.8); 
            border: 2px solid #f7931a; 
            border-radius: 1rem; 
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.3);
            transition: all 0.4s;
        }
        .metric-card:hover { 
            box-shadow: 0 0 40px rgba(247, 147, 26, 0.6); /* Faint neon glow */
        }
        .light .metric-card { 
            background: rgba(255,255,255,0.9); 
            border: 2px solid #f7931a; 
        }
        .progress-bar { 
            height: 10px; 
            border-radius: 9999px; 
            background: #1a1a1a; 
        }
        .light .progress-bar { background: #e2e8f0; }
        .progress-fill { 
            height: 100%; 
            border-radius: 9999px; 
            background: linear-gradient(to right, #f7931a, #ff6600);
            transition: width 2s ease;
        }
        .news-card, .x-post-card { 
            background: rgba(0, 0, 0, 0.85); 
            border: 2px solid #f7931a; 
            border-radius: 1rem; 
            transition: all 0.4s;
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.2);
        }
        .news-card:hover, .x-post-card:hover { 
            box-shadow: 0 0 40px rgba(247, 147, 26, 0.5);
            transform: translateY(-5px);
        }
        .light .news-card, .light .x-post-card { 
            background: rgba(255,255,255,0.9); 
            border: 2px solid #f7931a; 
        }
        .gradient-text { 
            background: linear-gradient(to right, #f7931a, #ff6600); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            animation: glow 2s infinite alternate; 
        }
        @keyframes glow { 
            from { text-shadow: 0 0 10px #f7931a; } 
            to { text-shadow: 0 0 30px #f7931a; } 
        }
        .animate-spin-slow { animation: spin 25s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="transition-all duration-500">
    <header class="header py-6 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Bitcoin Logo" class="w-12 h-12 animate-spin-slow">
            <div class="text-4xl font-extrabold gradient-text">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <input id="search-input" type="text" class="px-5 py-2 rounded-full bg-black/50 text-white placeholder-orange-300 w-60 focus:outline-none focus:ring-2 focus:ring-f7931a light:bg-white/50 light:text-black light:placeholder-orange-700 border border-f7931a text-sm" placeholder="Search...">
            <button id="toggle-theme" class="px-5 py-2 rounded-full bg-black/50 hover:bg-black/70 light:bg-white/50 light:hover:bg-white/70 flex items-center gap-2 font-bold text-sm text-white light:text-black border border-f7931a">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <h1 class="text-6xl font-extrabold mb-16 text-center gradient-text animate-glow">Markets News Hub</h1>

        <!-- Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-8 mb-20">
            <!-- Same as before, smaller -->
            <div class="metric-card p-6 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-2">Crypto Market Cap</p>
                <p id="crypto-cap" class="text-3xl font-bold mb-4 gradient-text">Loading...</p>
                <div class="progress-bar"><div id="cap-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <!-- Repeat for others... -->
        </div>

        <!-- News & X -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
            <div class="lg:col-span-2">
                <h2 class="text-4xl font-extrabold mb-8 gradient-text">Latest News</h2>
                <div id="news-feed" class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- Filled with 15 news cards -->
                </div>
            </div>
            <div>
                <h2 class="text-4xl font-extrabold mb-8 gradient-text">Trending X Posts</h2>
                <div id="x-feed" class="grid grid-cols-1 gap-8">
                    <!-- Filled with 10 X posts -->
                </div>
            </div>
        </div>
    </div>

    <script>
        // Same live metrics load + theme

        // Top 15 news (from today)
        const news = [ /* 15 items from search results */ ];

        // Top 10 X posts (high engagement today)
        const xPosts = [ /* 10 items from X search */ ];

        // displayNews() and displayXPosts() with clickable links

        // Search filters both
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
