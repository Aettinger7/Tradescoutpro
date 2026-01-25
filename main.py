from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update, current_path='/')

@app.route('/lore')
def lore():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(LORE_TEMPLATE, last_update=last_update, current_path='/lore')

@app.route('/art')
def art():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(ART_TEMPLATE, last_update=last_update, current_path='/art')

application = app

# Shared head + styles (ensures background loads on all pages)
SHARED_HEAD = '''
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
                        url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed !important;
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
            font-size: 0.875rem; /* smaller on mobile */
        }
        .btn-red:hover {
            background: #FFD700;
            color: black;
            transform: scale(1.08);
        }
        .btn-active {
            background: #FF0000;
            color: white;
            padding: 10px 20px;
            border-radius: 9999px;
            font-weight: bold;
            opacity: 0.85;
            cursor: default;
            font-size: 0.875rem;
        }
        @media (min-width: 640px) {
            .btn-red, .btn-active { font-size: 1rem; padding: 12px 24px; }
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
'''

HEADER_SNIPPET = '''
<header class="header py-5 sm:py-6 px-4 sm:px-6 fixed w-full top-0 z-50">
    <div class="flex justify-between items-center max-w-7xl mx-auto">
        <a href="/" class="flex items-center gap-3 sm:gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-10 h-10 sm:w-14 sm:h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover"
                 onerror="this.src='https://via.placeholder.com/56/FFD700/000?text=Neko';">
            <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-2 sm:gap-4 flex-wrap">
            {% if current_path != '/' %}
                <a href="/" class="btn-red">Home</a>
            {% endif %}
            {% if current_path == '/lore' %}
                <span class="btn-active">Lore</span>
            {% else %}
                <a href="/lore" class="btn-red">Lore</a>
            {% endif %}
            {% if current_path == '/art' %}
                <span class="btn-active">Art</span>
            {% else %}
                <a href="/art" class="btn-red">Art</a>
            {% endif %}
            <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red">Buy on Uniswap</a>
        </div>
    </div>
</header>
'''

HTML_TEMPLATE = SHARED_HEAD + '''
<body>
    ''' + HEADER_SNIPPET + '''
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

        <section class="mb-24 sm:mb-28 md:mb-32">
            <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-extrabold mb-10 text-center">Join the Zenshin Clan</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8">
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4">X</h3>
                    <a href="https://x.com/NekoTheSamurai" target="_blank" class="text-yellow-400 hover:underline text-lg sm:text-xl">Follow @NekoTheSamurai</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4">Telegram</h3>
                    <a href="https://t.me/toshimart" target="_blank" class="text-yellow-400 hover:underline text-lg sm:text-xl">Toshimart TG</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4">Discord</h3>
                    <a href="https://discord.com/invite/toshibase" target="_blank" class="text-yellow-400 hover:underline text-lg sm:text-xl">Toshi Base</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4">Warpcast</h3>
                    <a href="https://warpcast.com/toshibase" target="_blank" class="text-yellow-400 hover:underline text-lg sm:text-xl">Toshi Base</a>
                </div>
            </div>
        </section>

        <section class="mb-24 sm:mb-28 md:mb-32">
            <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-extrabold mb-10 text-center">Top 10 Trending Base Coins</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="https://toshimart.xyz/0xac1bd2486aaf3b5c0fc3fd868558b082a531b2b4" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#1 - $TOSHI</h3>
                    <p class="text-gray-300 mt-2">The original Base cat meme leader</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=doginme" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#2 - $DOGINME</h3>
                    <p class="text-gray-300 mt-2">High-energy dog meme on Base</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=yuki" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#3 - $YUKI</h3>
                    <p class="text-gray-300 mt-2">Popular Base cat-themed token</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=moto" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#4 - $MOTO</h3>
                    <p class="text-gray-300 mt-2">Speed & adventure meme coin</p>
                </a>
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="card p-6 text-center hover:bg-red-900/50 border-4 border-yellow-400">
                    <h3 class="text-2xl font-bold text-yellow-400">#5 - $NEKO</h3>
                    <p class="text-gray-300 mt-2">Neko the Samurai Cat - Zenshin Clan!</p>
                </a>
                <a href="https://dexscreener.com/base" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#6 - Trending #6</h3>
                    <p class="text-gray-300 mt-2">Check Dexscreener for latest</p>
                </a>
                <a href="https://dexscreener.com/base" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#7 - Trending #7</h3>
                    <p class="text-gray-300 mt-2">Check Dexscreener for latest</p>
                </a>
                <a href="https://dexscreener.com/base" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#8 - Trending #8</h3>
                    <p class="text-gray-300 mt-2">Check Dexscreener for latest</p>
                </a>
                <a href="https://dexscreener.com/base" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#9 - Trending #9</h3>
                    <p class="text-gray-300 mt-2">Check Dexscreener for latest</p>
                </a>
                <a href="https://dexscreener.com/base" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#10 - Trending #10</h3>
                    <p class="text-gray-300 mt-2">Check Dexscreener for latest</p>
                </a>
            </div>
            <p class="text-center text-gray-400 mt-8 text-sm sm:text-base">Top 5 fixed per clan lore; others dynamic. Links to buy/trade pages. DYOR!</p>
        </section>

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

LORE_TEMPLATE = SHARED_HEAD + '''
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-5 sm:px-6 lg:px-8 pt-32 sm:pt-36 md:pt-40 pb-20 md:pb-24 max-w-5xl">
        <section class="text-center mb-12">
            <h1 class="section-title text-5xl sm:text-7xl mb-6">Neko Lore</h1>
            <p class="text-xl text-gray-300">The Path of the Samurai Cat</p>
        </section>
        <div class="card p-8 sm:p-12 space-y-6">
            <p class="text-lg leading-relaxed">Neko is the silent guardian of the village: soft paws tread quietly in the dawn mist, yet claws are always ready to defend the light. Born under cherry blossoms and forged in shadow, Neko walks the path of Zenshin—forward progress without haste, honor without pride.</p>
            <p class="text-lg leading-relaxed">"Fate whispers, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'" Daily meditations remind the clan: enjoy slow mornings, sharpen the blade in silence, protect what is precious.</p>
            <p class="text-lg leading-relaxed">The Zenshin Clan grows through shared wisdom, resilience, and community. No rush, only steady advancement. Join us on this path.</p>
            <ul class="list-disc pl-6 text-lg space-y-3">
                <li>Soft paws, sharp steel.</li>
                <li>Forward Progress (Zenshin).</li>
                <li>Warrior in a garden.</li>
            </ul>
        </div>
        <div class="text-center mt-12">
            <a href="/" class="btn-red text-xl px-12 py-6 inline-block">Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

ART_TEMPLATE = SHARED_HEAD + '''
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-5 sm:px-6 lg:px-8 pt-32 sm:pt-36 md:pt-40 pb-20 md:pb-24 max-w-5xl">
        <section class="text-center mb-12">
            <h1 class="section-title text-5xl sm:text-7xl mb-6">Neko Art Gallery</h1>
            <p class="text-xl text-gray-300">Visions of the Samurai Cat</p>
        </section>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
            <div class="overflow-hidden rounded-xl shadow-2xl">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" class="w-full h-auto object-cover hover:scale-105 transition-transform duration-300">
            </div>
            <div class="overflow-hidden rounded-xl shadow-2xl">
                <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" class="w-full h-auto object-cover hover:scale-105 transition-transform duration-300">
            </div>
            <!-- Add more images here as you create/upload them -->
            <div class="card p-8 flex items-center justify-center h-64 sm:h-80">
                <p class="text-gray-400 text-center text-lg">More clan art drops coming soon – Zenshin!</p>
            </div>
        </div>
        <div class="text-center mt-12">
            <a href="/" class="btn-red text-xl px-12 py-6 inline-block">Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
