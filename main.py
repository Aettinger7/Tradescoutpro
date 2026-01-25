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
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                        url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed !important;
            background-size: cover !important;
            background-attachment: fixed !important;
            background-color: #0a0a0a !important; 
            color: #ffffff; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
            min-height: 100vh;
        }
        .header { 
            background: linear-gradient(to right, #c8102e, rgba(0,0,0,0.92)); 
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 25px rgba(200, 16, 46, 0.6);
        }
        .logo-text {
            font-family: 'Cinzel', serif;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF4500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 15px rgba(255, 215, 0, 0.7);
        }
        .card { 
            background: rgba(10, 10, 10, 0.88); 
            border: 2px solid #c8102e; 
            border-radius: 1.25rem; 
            box-shadow: 0 10px 35px rgba(200, 16, 46, 0.35);
            transition: all 0.4s ease;
        }
        .card:hover { 
            box-shadow: 0 15px 50px rgba(200, 16, 46, 0.6);
            transform: translateY(-6px);
        }
        .section-title {
            font-family: 'Cinzel', serif;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF4500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(255, 69, 0, 0.6);
        }
        .btn-red {
            background: linear-gradient(135deg, #FF4500, #c8102e);
            color: white;
            padding: 0.9rem 1.8rem;
            border-radius: 9999px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.35s ease;
            white-space: nowrap;
            box-shadow: 0 6px 20px rgba(200, 16, 46, 0.5), inset 0 1px 3px rgba(255,255,255,0.15);
            border: 2px solid #FFD700;
            font-size: 0.95rem;
        }
        .btn-red:hover {
            background: linear-gradient(135deg, #FFD700, #FF8C00);
            color: #000;
            transform: translateY(-3px) scale(1.08);
            box-shadow: 0 12px 40px rgba(255, 215, 0, 0.7), inset 0 1px 4px rgba(255,255,255,0.25);
            border: 2px solid #FFD700;
        }
        .btn-active {
            background: linear-gradient(135deg, #FFD700, #FF8C00);
            color: #000;
            padding: 0.9rem 1.8rem;
            border-radius: 9999px;
            font-weight: 700;
            box-shadow: 0 6px 20px rgba(255, 215, 0, 0.6), inset 0 1px 3px rgba(255,255,255,0.2);
            cursor: default;
            border: 2px solid #FFD700;
            font-size: 0.95rem;
        }
        @media (min-width: 640px) {
            .btn-red, .btn-active {
                padding: 1rem 2rem;
                font-size: 1.05rem;
            }
        }
        .animate-spin-slow { animation: spin 32s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .hero-img { 
            object-fit: cover;
            filter: drop-shadow(0 0 35px rgba(255,215,0,0.7)); 
            aspect-ratio: 1 / 1;
        }
        iframe { border: none; width: 100%; height: 520px; }
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
<header class="header py-5 sm:py-7 px-4 sm:px-8 fixed w-full top-0 z-50">
    <div class="flex justify-between items-center max-w-7xl mx-auto">
        <a href="/" class="flex items-center gap-3 sm:gap-5">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-11 h-11 sm:w-16 sm:h-16 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover"
                 onerror="this.src='https://via.placeholder.com/64/FFD700/000?text=Neko';">
            <div class="logo-text text-2xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-3 sm:gap-6 flex-wrap">
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
    <div class="container mx-auto px-5 sm:px-8 lg:px-10 pt-32 sm:pt-40 md:pt-48 pb-20 md:pb-28 max-w-7xl">
        <section class="text-center mb-24 sm:mb-32 md:mb-40">
            <div class="space-y-8 sm:space-y-10 md:space-y-12">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko the Samurai Cat" 
                     class="hero-img mx-auto rounded-full animate-spin-slow border-8 border-yellow-500 w-48 sm:w-64 md:w-80 h-48 sm:h-64 md:h-80"
                     loading="lazy">
                <h1 class="text-5xl sm:text-6xl md:text-8xl font-extrabold section-title">Zenshin Clan</h1>
                <p class="text-xl sm:text-2xl md:text-3xl">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
                <div class="bg-black/70 inline-block px-8 sm:px-10 md:px-12 py-6 sm:py-7 rounded-2xl font-mono text-base sm:text-lg break-all shadow-lg">
                    Now Live on Uniswap • CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
                </div>
                <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('CA Copied!')" 
                        class="mt-6 px-10 sm:px-12 md:px-16 py-5 sm:py-6 bg-gradient-to-r from-yellow-500 to-yellow-600 text-black rounded-full font-bold hover:from-yellow-400 hover:to-yellow-500 text-lg sm:text-xl shadow-xl hover:shadow-2xl transition-all duration-300">
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
                <p class="text-center mt-4 text-gray-400">If the embed doesn't load, click <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="text-yellow-400 underline">here</a> to open directly.</p>
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

        <footer class="text-center text-gray-400 py-16 sm:py-20 border-t border-red-800 mt-16">
            <p>Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-4">Last Update: {{ last_update }}</p>
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
    <div class="container mx-auto px-5 sm:px-8 lg:px-10 pt-32 sm:pt-40 md:pt-48 pb-20 md:pb-28 max-w-5xl">
        <section class="text-center mb-16 sm:mb-20 md:mb-24">
            <h1 class="section-title text-5xl sm:text-6xl md:text-8xl mb-8">Neko Lore</h1>
            <p class="text-2xl text-gray-300">The Path of the Samurai Cat</p>
        </section>
        <div class="card p-8 sm:p-12 md:p-16 space-y-8 text-lg sm:text-xl leading-relaxed">
            <p>Neko is the silent guardian of the village: soft paws tread quietly in the dawn mist, yet claws are always ready to defend the light. Born under cherry blossoms and forged in shadow, Neko walks the path of Zenshin—forward progress without haste, honor without pride.</p>
            
            <p>"Fate whispers to Neko, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'" This is not arrogance, but acceptance of one's own power when the moment demands it. The true warrior does not seek the storm — the storm finds the warrior.</p>
            
            <p>Every dawn brings new lessons: enjoy slow mornings with tea and reflection, sharpen the blade in silence, protect what is precious without seeking glory. The warrior in the garden tends to both peace and strength, knowing that true power lies in restraint.</p>
            
            <div class="bg-black/60 p-8 rounded-2xl border border-yellow-600/40 shadow-inner">
                <p class="font-bold text-yellow-400 text-xl mb-6">Core Principles of the Zenshin Clan:</p>
                <ul class="list-disc pl-8 space-y-4 text-lg">
                    <li><strong>Soft paws, sharp steel</strong> – Gentleness in peace, ferocity in protection</li>
                    <li><strong>Forward Progress (Zenshin)</strong> – Never stagnant, always advancing with purpose</li>
                    <li><strong>Warrior in a garden</strong> – Balance of strength and serenity</li>
                    <li><strong>Honor the small moments</strong> – Gratitude in every breath, every sunrise</li>
                    <li><strong>Protect the light</strong> – Stand for what matters, even when unseen</li>
                    <li><strong>No glory without duty</strong> – True honor is quiet, not loud</li>
                </ul>
            </div>
            
            <p>The clan grows not through noise or hype, but through shared wisdom, quiet resolve, and consistent action. Neko does not promise riches or fame — only the path. Those who walk it become stronger. Those who stray are left behind.</p>
            
            <p>Join the Zenshin Clan. Forward progress awaits. Zenshin.</p>
        </div>
        <div class="text-center mt-16">
            <a href="/" class="btn-red text-xl sm:text-2xl px-12 sm:px-16 py-6 sm:py-8 inline-block">Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

ART_TEMPLATE = SHARED_HEAD + '''
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-5 sm:px-8 lg:px-10 pt-32 sm:pt-40 md:pt-48 pb-20 md:pb-28 max-w-6xl">
        <section class="text-center mb-16 sm:mb-20 md:mb-24">
            <h1 class="section-title text-5xl sm:text-6xl md:text-8xl mb-8">Neko Art Gallery</h1>
            <p class="text-2xl text-gray-300">Visions of the Samurai Cat</p>
        </section>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-10">
            <div class="overflow-hidden rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-500">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" class="w-full h-auto object-cover">
            </div>
            <div class="overflow-hidden rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-500">
                <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" class="w-full h-auto object-cover">
            </div>
            <div class="overflow-hidden rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-500">
                <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Neko Clan Art 1" class="w-full h-auto object-cover">
            </div>
            <div class="overflow-hidden rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-500">
                <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Neko Clan Art 2" class="w-full h-auto object-cover">
            </div>
            <div class="overflow-hidden rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-500">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Warrior Pose" class="w-full h-auto object-cover">
            </div>
            <div class="card p-10 flex items-center justify-center h-80 sm:h-96 col-span-1 sm:col-span-2 lg:col-span-1">
                <p class="text-gray-400 text-center text-xl sm:text-2xl">More clan art drops coming soon – Zenshin!</p>
            </div>
        </div>
        <div class="text-center mt-16">
            <a href="/" class="btn-red text-xl sm:text-2xl px-12 sm:px-16 py-6 sm:py-8 inline-block">Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
