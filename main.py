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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko the Samurai Cat - $NEKO on Base</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
                        url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed;
            background-size: cover;
            background-attachment: fixed;
            color: #ffffff;
            font-family: Arial, sans-serif;
            scroll-behavior: smooth;
        }
        .header {
            background: rgba(200,16,46,0.9);
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(200,16,46,0.6);
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
        }
        .btn-buy {
            background: linear-gradient(135deg, #FF4500, #c8102e);
            color: white;
            padding: 0.8rem 1.6rem;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.35s ease;
            box-shadow: 0 6px 20px rgba(200,16,46,0.6);
            border: 2px solid #FFD700;
        }
        .btn-buy:hover {
            background: linear-gradient(135deg, #FFD700, #FF8C00);
            color: black;
            transform: translateY(-3px) scale(1.08);
            box-shadow: 0 12px 40px rgba(255,215,0,0.7);
            border: 2px solid #FFD700;
        }
        .section-title {
            font-family: 'Cinzel', serif;
            background: linear-gradient(to right, #FFD700, #FF4500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(255,69,0,0.6);
        }
        .card {
            background: rgba(10,10,10,0.88);
            border: 2px solid #c8102e;
            border-radius: 1.25rem;
            box-shadow: 0 10px 35px rgba(200,16,46,0.4);
            transition: all 0.4s ease;
        }
        .card:hover {
            box-shadow: 0 15px 50px rgba(200,16,46,0.7);
            transform: translateY(-6px);
        }
        .animate-spin-slow {
            animation: spin 30s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <header class="header py-4 px-6 flex justify-between items-center">
        <a href="#" class="flex items-center gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-12 h-12 sm:w-16 sm:h-16 rounded-full border-4 border-yellow-500 animate-spin-slow">
            <div class="logo-text text-2xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <nav class="flex gap-3 sm:gap-6 flex-wrap">
            <a href="#trade" class="btn-buy">Trade</a>
            <a href="#join" class="btn-buy">Join</a>
            <a href="#lore" class="btn-buy">Lore</a>
            <a href="#art" class="btn-buy">Art</a>
        </nav>
    </header>

    <main class="pt-28 px-4 sm:px-6 lg:px-10 max-w-7xl mx-auto">
        <!-- Hero -->
        <section id="hero" class="text-center py-16 sm:py-24">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="mx-auto mb-8 rounded-full border-8 border-yellow-500 w-48 sm:w-64 md:w-80 h-48 sm:h-64 md:h-80 animate-spin-slow">
            <h1 class="text-5xl sm:text-7xl md:text-8xl font-extrabold section-title mb-6">Zenshin Clan</h1>
            <p class="text-xl sm:text-2xl md:text-3xl mb-8">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/70 inline-block px-8 py-5 rounded-2xl font-mono text-base sm:text-lg mb-8 shadow-lg">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-lg">Buy on Uniswap</a>
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-lg">Buy on Toshimart</a>
            </div>
        </section>

        <!-- Trade Section -->
        <section id="trade" class="py-16 sm:py-24">
            <h2 class="text-4xl sm:text-5xl font-extrabold mb-12 section-title text-center">Trade $NEKO Live</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4 text-yellow-400">Uniswap (Primary)</h3>
                    <p class="text-gray-300 mb-6">Live V3 pool on Base chain</p>
                    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy block text-center py-4">Swap Now</a>
                </div>
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4 text-yellow-400">Dexscreener Chart</h3>
                    <p class="text-gray-300 mb-6">Real-time price, volume, liquidity</p>
                    <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="btn-buy block text-center py-4">View Chart</a>
                </div>
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4 text-yellow-400">Toshimart (Legacy)</h3>
                    <p class="text-gray-300 mb-6">Original launch platform</p>
                    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy block text-center py-4">View on Toshimart</a>
                </div>
            </div>
        </section>

        <!-- Chart Embed -->
        <section id="chart" class="py-16 sm:py-24">
            <h2 class="text-4xl sm:text-5xl font-extrabold mb-12 section-title text-center">$NEKO Live Chart</h2>
            <div class="card p-4 sm:p-6 overflow-hidden" style="min-height: 520px;">
                <iframe src="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570?embed=1&theme=dark&trades=0&info=0" title="NEKO Chart" loading="lazy" style="width: 100%; height: 500px; border: 0;"></iframe>
                <p class="text-center mt-4 text-gray-400">If the chart doesn't load, click <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="text-yellow-400 underline">here</a> to open directly.</p>
            </div>
        </section>

        <!-- Join Clan -->
        <section id="join" class="py-16 sm:py-24">
            <h2 class="text-4xl sm:text-5xl font-extrabold mb-12 section-title text-center">Join the Zenshin Clan</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="card p-6 text-center">
                    <h3 class="text-2xl font-bold mb-4">X</h3>
                    <a href="https://x.com/NekoTheSamurai" target="_blank" class="text-yellow-400 hover:underline text-lg">Follow @NekoTheSamurai</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-2xl font-bold mb-4">Telegram</h3>
                    <a href="https://t.me/toshimart" target="_blank" class="text-yellow-400 hover:underline text-lg">Toshimart TG</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-2xl font-bold mb-4">Discord</h3>
                    <a href="https://discord.com/invite/toshibase" target="_blank" class="text-yellow-400 hover:underline text-lg">Toshi Base</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-2xl font-bold mb-4">Warpcast</h3>
                    <a href="https://warpcast.com/toshibase" target="_blank" class="text-yellow-400 hover:underline text-lg">Toshi Base</a>
                </div>
            </div>
        </section>

        <!-- Lore -->
        <section id="lore" class="py-16 sm:py-24">
            <h2 class="text-4xl sm:text-5xl font-extrabold mb-12 section-title text-center">Neko Lore</h2>
            <div class="card p-8 space-y-6 text-lg leading-relaxed">
                <p>Neko is the silent guardian of the village: soft paws tread quietly in the dawn mist, yet claws are always ready to defend the light. Born under cherry blossoms and forged in shadow, Neko walks the path of Zenshin—forward progress without haste, honor without pride.</p>
                <p>"Fate whispers to Neko, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'" This is not arrogance, but acceptance of one's own power when the moment demands it. The true warrior does not seek the storm — the storm finds the warrior.</p>
                <p>Every dawn brings new lessons: enjoy slow mornings with tea and reflection, sharpen the blade in silence, protect what is precious without seeking glory. The warrior in the garden tends to both peace and strength, knowing that true power lies in restraint.</p>
                <p>The clan grows not through noise or hype, but through shared wisdom, quiet resolve, and consistent action. Neko does not promise riches or fame — only the path. Those who walk it become stronger. Those who stray are left behind.</p>
                <p>Join the Zenshin Clan. Forward progress awaits. Zenshin.</p>
            </div>
        </section>

        <!-- Art Gallery -->
        <section id="art" class="py-16 sm:py-24">
            <h2 class="text-4xl sm:text-5xl font-extrabold mb-12 section-title text-center">Neko Art Gallery</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-10">
                <div class="overflow-hidden rounded-2xl shadow-2xl">
                    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" class="w-full h-auto object-cover">
                </div>
                <div class="overflow-hidden rounded-2xl shadow-2xl">
                    <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" class="w-full h-auto object-cover">
                </div>
                <div class="overflow-hidden rounded-2xl shadow-2xl">
                    <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Clan Art 1" class="w-full h-auto object-cover">
                </div>
                <div class="overflow-hidden rounded-2xl shadow-2xl">
                    <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Clan Art 2" class="w-full h-auto object-cover">
                </div>
            </div>
        </section>

        <!-- Trending Coins -->
        <section class="py-16 sm:py-24">
            <h2 class="text-4xl sm:text-5xl font-extrabold mb-12 section-title text-center">Top 10 Trending Base Coins</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="https://dexscreener.com/base/search?q=toshi" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
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
                <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="card p-6 text-center hover:bg-red-900/50 border-4 border-yellow-400">
                    <h3 class="text-2xl font-bold text-yellow-400">#5 - $NEKO</h3>
                    <p class="text-gray-300 mt-2">Neko the Samurai Cat - Zenshin Clan!</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=brett" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#6 - $BRETT</h3>
                    <p class="text-gray-300 mt-2">Base's blue frog meme</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=keycat" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#7 - $KEYCAT</h3>
                    <p class="text-gray-300 mt-2">Keyboard cat meme</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=miggles" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#8 - $MIGGLES</h3>
                    <p class="text-gray-300 mt-2">Miggles the cat</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=popcat" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#9 - $POPCAT</h3>
                    <p class="text-gray-300 mt-2">Popcat meme on Base</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=benji" target="_blank" class="card p-6 text-center hover:bg-red-900/50">
                    <h3 class="text-2xl font-bold text-yellow-400">#10 - $BENJI</h3>
                    <p class="text-gray-300 mt-2">Benji the dog meme</p>
                </a>
            </div>
        </section>

        <footer class="text-center text-gray-400 py-12 border-t border-red-800 mt-12">
            <p>Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-4">Last Update: {{ last_update }}</p>
        </footer>
    </main>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
