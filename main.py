from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update, current_path='/')

@app.route('/whitepaper')
def whitepaper():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(WHITEPAPER_TEMPLATE, last_update=last_update, current_path='/whitepaper')

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="scroll-restoration" content="manual">
    <title>Neko the Samurai Cat - Official Memecoin Site</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        body { 
            margin: 0;
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                        url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed;
            background-size: cover;
            background-attachment: fixed;
            background-color: #111111; 
            color: #ffffff; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
            min-height: 100vh;
        }
        .header { 
            background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.9)); 
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(255, 0, 0, 0.5);
        }
        .logo-text {
            font-family: 'Cinzel', serif;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
        }
        .card { 
            background: rgba(0, 0, 0, 0.85); 
            border: 2px solid #FF0000; 
            border-radius: 1rem; 
            box-shadow: 0 8px 32px rgba(255, 0, 0, 0.4);
            transition: all 0.3s;
        }
        .card:hover { 
            box-shadow: 0 0 40px rgba(255, 0, 0, 0.7);
            transform: translateY(-4px);
        }
        .section-title {
            font-family: 'Cinzel', serif;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 25px rgba(255, 215, 0, 0.7);
        }
        .btn-red {
            background: #FF0000;
            color: white;
            padding: 10px 20px;
            border-radius: 9999px;
            font-weight: bold;
            text-decoration: none;
            transition: all 0.3s;
            white-space: nowrap;
        }
        .btn-red:hover {
            background: #FFD700;
            color: black;
            transform: scale(1.05);
        }
        .btn-active {
            background: #FF0000;
            color: white;
            padding: 10px 20px;
            border-radius: 9999px;
            font-weight: bold;
            opacity: 0.8;
            cursor: default;
        }
        .animate-spin-slow { animation: spin 30s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .hero-img { 
            object-fit: cover;
            filter: drop-shadow(0 0 25px rgba(255,215,0,0.6)); 
            aspect-ratio: 1 / 1;
        }
        iframe { border: none; width: 100%; height: 500px; }
    </style>
    <script>
        if ('scrollRestoration' in history) {
            history.scrollRestoration = 'manual';
        }
    </script>
    <link rel="preload" as="image" href="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png">
</head>
<body>
    <header class="header py-5 sm:py-6 px-4 sm:px-6 fixed w-full top-0 z-50">
        <div class="flex justify-between items-center max-w-7xl mx-auto">
            <a href="/" class="flex items-center gap-3 sm:gap-4">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko Logo" 
                     class="w-10 h-10 sm:w-14 sm:h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover"
                     onerror="this.src='https://via.placeholder.com/56/FFD700/000?text=Neko';">
                <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
            </a>
            <div class="flex items-center gap-3 sm:gap-6 flex-wrap">
                {% if current_path != '/' %}
                    <a href="/" class="btn-red text-sm sm:text-base">Home</a>
                {% endif %}
                {% if current_path == '/' %}
                    <a href="/whitepaper" class="btn-red text-sm sm:text-base">Whitepaper</a>
                {% else %}
                    <span class="btn-active text-sm sm:text-base">Whitepaper</span>
                {% endif %}
                <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red text-sm sm:text-base">Buy on Uniswap</a>
            </div>
        </div>
    </header>

    <div class="container mx-auto px-5 sm:px-6 lg:px-8 pt-32 sm:pt-36 md:pt-40 pb-20 md:pb-24 max-w-7xl">
        <section class="text-center mb-24 sm:mb-28 md:mb-32">
            <div class="space-y-6 sm:space-y-8 md:space-y-10">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko the Samurai Cat" 
                     class="hero-img mx-auto rounded-full animate-spin-slow border-8 border-yellow-500 w-44 sm:w-56 md:w-72 h-44 sm:h-56 md:h-72"
                     loading="lazy"
                     onerror="this.src='https://via.placeholder.com/300/FFD700/000?text=Neko+Hero';">
                <h1 class="text-4xl sm:text-5xl md:text-7xl font-extrabold section-title">Zenshin Clan</h1>
                <p class="text-lg sm:text-xl md:text-2xl">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
                <div class="bg-black/60 inline-block px-6 sm:px-8 md:px-10 py-5 sm:py-6 rounded-xl font-mono text-sm sm:text-base break-all">
                    Now Live on Uniswap • CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
                </div>
                <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('CA Copied!')" 
                        class="mt-4 px-8 sm:px-10 md:px-12 py-4 sm:py-5 bg-yellow-600 text-black rounded-full font-bold hover:bg-yellow-500 text-base sm:text-lg">
                    Copy CA
                </button>
            </div>
        </section>

        <section class="mb-24 sm:mb-28 md:mb-32">
            <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-extrabold mb-10 text-center">Trade Live on Uniswap</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-yellow-400">Live Price & Chart</h3>
                    <p class="text-gray-300 mb-4">Real-time trading on Uniswap V3 (Base)</p>
                    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red inline-block mt-4">Swap on Uniswap</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-yellow-400">Dexscreener</h3>
                    <p class="text-gray-300">Full charts, trades, liquidity info</p>
                    <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="btn-red inline-block mt-4">View on Dexscreener</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-yellow-400">Liquidity & Holders</h3>
                    <p class="text-gray-300">Check pool stats & community growth</p>
                    <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="btn-red inline-block mt-4">Explore Stats</a>
                </div>
            </div>
        </section>

        <section class="mb-24 sm:mb-28 md:mb-32">
            <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-extrabold mb-10 text-center">$NEKO Live Chart</h2>
            <div class="card p-4 sm:p-6 md:p-8" style="min-height: 520px;">
                <iframe src="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570?embed=1" title="NEKO Dexscreener Chart" loading="lazy" style="height: 500px;"></iframe>
                <p class="text-center mt-6 text-gray-400">If the chart doesn't load, click <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="text-yellow-400 underline">here</a> to open on Dexscreener.</p>
            </div>
        </section>

        <!-- Keep Join the Zenshin Clan and Top 10 Trending sections as-is from your previous version -->

        <footer class="text-center text-gray-400 py-12 sm:py-14 border-t border-red-800">
            <p>Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-3">Last Update: {{ last_update }}</p>
        </footer>
    </div>

    <script>
        window.addEventListener('load', function() {
            setTimeout(function() {
                window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
            }, 500);
        });
    </script>
</body>
</html>
'''

# WHITEPAPER_TEMPLATE - update footer or add migration note if desired, but keep core content
WHITEPAPER_TEMPLATE = '''
# (Use the same WHITEPAPER_TEMPLATE from previous full version, just update footer to reflect Uniswap live if you want)
<p class="text-sm text-gray-500">© 2026 Neko on Base • Now Live on Uniswap (Base) • Powered by Toshimart & Community</p>
'''

if __name__ == '__main__':
    app.run(debug=True)
