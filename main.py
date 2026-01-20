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
            padding: 10px 24px;
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
            padding: 10px 24px;
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
        .tweet-media { max-width: 100%; height: auto; border-radius: 0.5rem; }
        .spinner-logo { 
            object-fit: cover; 
            aspect-ratio: 1 / 1;
        }
        img.rounded-full { 
            object-fit: cover; 
            aspect-ratio: 1 / 1;
        }
    </style>
    <script>
        if ('scrollRestoration' in history) {
            history.scrollRestoration = 'manual';
        }
    </script>
    <link rel="preload" as="image" href="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png">
</head>
<body>
    <header class="header py-4 px-4 sm:py-6 sm:px-8 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-3 sm:gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-10 h-10 sm:w-14 sm:h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover"
                 onerror="this.src='https://via.placeholder.com/56/FFD700/000?text=Neko';">
            <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-4 flex-wrap">
            {% if current_path != '/' %}
                <a href="/" class="btn-red text-base sm:text-lg">Home</a>
            {% endif %}
            {% if current_path == '/' %}
                <a href="/whitepaper" class="btn-red text-base sm:text-lg">Whitepaper</a>
            {% else %}
                <span class="btn-active text-base sm:text-lg">Whitepaper</span>
            {% endif %}
            <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red text-base sm:text-lg">Buy $NEKO Now</a>
        </div>
    </header>

    <div class="container mx-auto px-4 sm:px-6 pt-24 sm:pt-32 pb-20 max-w-7xl">
        <section class="text-center mb-20">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="hero-img mx-auto mb-8 rounded-full animate-spin-slow border-8 border-yellow-500 w-48 sm:w-72 h-48 sm:h-72"
                 loading="lazy"
                 onerror="this.src='https://via.placeholder.com/300/FFD700/000?text=Neko+Hero'; this.alt='Fallback Neko Image';">
            <h1 class="text-4xl sm:text-6xl md:text-7xl font-extrabold mb-6 section-title">Zenshin Clan</h1>
            <p class="text-xl sm:text-2xl mb-8">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/60 inline-block px-6 sm:px-8 py-4 rounded-xl mb-6 font-mono text-base sm:text-lg">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <br>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('Contract Address Copied!')" 
                    class="mt-4 px-6 sm:px-8 py-3 sm:py-4 bg-yellow-600 text-black rounded-full font-bold hover:bg-yellow-500 text-base sm:text-lg">
                Copy CA
            </button>
        </section>

        <section class="mb-20">
            <h2 class="section-title text-3xl sm:text-5xl font-extrabold mb-10 text-center">Live on Toshimart (Bonding Curve)</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-yellow-400">Price / Stats</h3>
                    <p class="text-2xl sm:text-3xl font-bold mb-2">Check Live</p>
                    <p class="text-gray-300 mb-4">Bonding curve – price rises as more buy</p>
                    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red inline-block mt-4">View on Toshimart</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-yellow-400">Market Cap / Liquidity</h3>
                    <p class="text-gray-300">Dynamic via bonding curve. Early holders get best entry.</p>
                    <p class="text-sm mt-4 text-gray-400">No Dexscreener yet – coming soon after curve completes</p>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-yellow-400">Holders / Volume</h3>
                    <p class="text-gray-300">Growing clan – join before migration.</p>
                    <p class="text-sm mt-4 text-gray-400">Trade with ETH on Toshimart</p>
                </div>
            </div>
        </section>

        <section class="mb-20">
            <h2 class="section-title text-3xl sm:text-5xl font-extrabold mb-10 text-center">$NEKO Chart & Trade</h2>
            <div class="card p-4 sm:p-6" style="min-height: 520px;">
                <iframe src="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" title="Toshimart Neko Chart" loading="lazy" style="height: 500px;"></iframe>
                <p class="text-center mt-4 text-gray-400">If the embed doesn't load, click <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="text-yellow-400 underline">here</a> to open directly.</p>
            </div>
        </section>

        <section class="mb-20">
            <h2 class="section-title text-3xl sm:text-5xl font-extrabold mb-10 text-center">Join the Zenshin Clan</h2>
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

        <section class="mb-20">
            <h2 class="section-title text-3xl sm:text-5xl font-extrabold mb-10 text-center">Top 10 Trending Base Coins</h2>
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
            <p class="text-center text-gray-400 mt-6 text-sm">Top 5 fixed per clan lore; others dynamic. Links to buy/trade pages. DYOR!</p>
        </section>

        <footer class="text-center text-gray-400 py-10 border-t border-red-800">
            <p>Powered by Toshimart on Base • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-2">Last Update: {{ last_update }}</p>
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

WHITEPAPER_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$NEKO Whitepaper - Neko the Samurai Cat</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed; background-size: cover; background-attachment: fixed; background-color: #111111; color: #ffffff; font-family: 'Helvetica Neue', Arial, sans-serif; min-height: 100vh; }
        .header { background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.9)); backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(255, 0, 0, 0.5); }
        .logo-text { font-family: 'Cinzel', serif; font-weight: 900; background: linear-gradient(to right, #FFD700, #FF0000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 20px rgba(255, 215, 0, 0.8); }
        .card { background: rgba(0, 0, 0, 0.85); border: 2px solid #FF0000; border-radius: 1rem; box-shadow: 0 8px 32px rgba(255, 0, 0, 0.4); }
        .section-title { font-family: 'Cinzel', serif; font-weight: 900; background: linear-gradient(to right, #FFD700, #FF0000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 25px rgba(255, 215, 0, 0.7); }
        .btn-red { background: #FF0000; color: white; padding: 10px 24px; border-radius: 9999px; font-weight: bold; text-decoration: none; transition: all 0.3s; white-space: nowrap; }
        .btn-red:hover { background: #FFD700; color: black; transform: scale(1.05); }
        .btn-active { background: #FF0000; color: white; padding: 10px 24px; border-radius: 9999px; font-weight: bold; opacity: 0.8; cursor: default; }
        .animate-spin-slow { animation: spin 30s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <header class="header py-4 px-4 sm:py-6 sm:px-8 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-3 sm:gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-10 h-10 sm:w-14 sm:h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover">
            <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-4 flex-wrap">
            {% if current_path != '/' %}
                <a href="/" class="btn-red text-base sm:text-lg">Home</a>
            {% endif %}
            {% if current_path == '/' %}
                <a href="/whitepaper" class="btn-red text-base sm:text-lg">Whitepaper</a>
            {% else %}
                <span class="btn-active text-base sm:text-lg">Whitepaper</span>
            {% endif %}
            <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red text-base sm:text-lg">Buy $NEKO Now</a>
        </div>
    </header>

    <div class="container mx-auto px-4 sm:px-6 pt-24 sm:pt-32 pb-20 max-w-5xl">
        <section class="text-center mb-12">
            <h1 class="section-title text-5xl sm:text-7xl font-extrabold mb-6">Whitepaper</h1>
            <p class="text-xl text-gray-300 mb-2">Neko the Samurai Cat – $NEKO</p>
            <p class="text-sm text-gray-500">Last Update: {{ last_update }}</p>
        </section>

        <div class="card p-8 sm:p-12 prose prose-invert max-w-none">
            <h2 class="section-title text-3xl sm:text-4xl mb-6">Overview</h2>
            <p class="text-lg mb-8 leading-relaxed">Neko the Samurai Cat ($NEKO) is a community-driven memecoin launched on the Base blockchain via Toshimart, the premier memecoin launchpad. Inspired by Japanese samurai culture and the spirit of "Zenshin" (Forward Progress), Neko embodies a warrior cat who walks the path of shadows to protect the light, enjoys simple moments, and faces storms with unyielding resolve. The project blends meme culture, daily motivational lore from the clan's guardian, and on-chain bonding curve dynamics to foster an engaged "Zenshin Clan" community.</p>

            <h2 class="section-title text-3xl sm:text-4xl mb-6 mt-12">Token Details</h2>
            <ul class="list-disc pl-8 text-lg space-y-4 mb-8">
                <li><strong>Symbol/Name:</strong> $NEKO / Neko the Samurai Cat</li>
                <li><strong>Contract Address (Base):</strong> 0x28973c4ef9ae754b076a024996350d3b16a38453</li>
                <li><strong>Launch Platform:</strong> Toshimart</li>
                <li><strong>Launch Date:</strong> ~January 13, 2026</li>
                <li><strong>Current Status:</strong> Bonding curve ~98.91% complete • Market Cap ~$1.6K • Holders ~10 • No Dexscreener yet (post-curve)</li>
            </ul>

            <h2 class="section-title text-3xl sm:text-4xl mb-6 mt-12">Tokenomics & Mechanics</h2>
            <p class="text-lg mb-6 leading-relaxed">Fair launch with no presale or team allocations. All supply enters via the Toshimart bonding curve:</p>
            <ul class="list-disc pl-8 text-lg space-y-4 mb-8">
                <li><strong>Bonding Curve:</strong> Price increases progressively with buys → early participants get better entry prices</li>
                <li><strong>Taxes:</strong> 0% buy/sell</li>
                <li><strong>Liquidity:</strong> Automatically migrates to a DEX pool (likely Uniswap on Base) upon curve completion</li>
                <li><strong>Distribution:</strong> 100% to community via open buying</li>
                <li><strong>Dev Holdings:</strong> Minimal (~0.35% visible on launchpad)</li>
            </ul>

            <h2 class="section-title text-3xl sm:text-4xl mb-6 mt-12">Lore & Vision</h2>
            <p class="text-lg mb-8 leading-relaxed">Neko shares daily wisdom on X (@NekoTheSamurai): resilience ("I am the storm"), gratitude ("Slow mornings are always the best!"), and forward progress ("Zenshin means 'Forward Progress'"). The Zenshin Clan is built on honor, fun, and steady advancement—no aggressive hype, just consistent community growth on Base.</p>

            <h2 class="section-title text-3xl sm:text-4xl mb-6 mt-12">Roadmap (Community-Driven)</h2>
            <ul class="list-disc pl-8 text-lg space-y-4 mb-8">
                <li><strong>Phase 1 (Current):</strong> Complete bonding curve, grow clan via X, Telegram, Discord</li>
                <li><strong>Phase 2:</strong> DEX migration, LP lock/renounce proof, Dexscreener listing</li>
                <li><strong>Phase 3:</strong> Expanded lore (art drops, memes, possible mini-games)</li>
                <li><strong>Phase 4:</strong> Long-term clan events, potential Base ecosystem partnerships</li>
            </ul>

            <h2 class="section-title text-3xl sm:text-4xl mb-6 mt-12">Risks & Disclaimer</h2>
            <p class="text-lg text-red-300 leading-relaxed mb-4">Memecoins are highly speculative and volatile. $NEKO is early-stage with low liquidity—high risk of total loss. No guarantees of value, utility, or returns. Do Your Own Research (DYOR). This is not financial advice. Community project only.</p>
            <p class="text-sm text-gray-500">© 2026 Neko on Base • Powered by Toshimart</p>
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
