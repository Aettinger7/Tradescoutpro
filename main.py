from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

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
            background: linear-gradient(to bottom, #000000, #0a0f1a);
            color: #d0d0d8;
            font-family: Arial, sans-serif;
            scroll-behavior: smooth;
            overflow-x: hidden;
        }
        .header {
            background: rgba(10, 15, 30, 0.95);
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(0, 212, 255, 0.25);
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            border-bottom: 1px solid rgba(189, 195, 199, 0.2);
        }
        .btn-buy {
            background: linear-gradient(135deg, #00d4ff, #0099cc);
            color: #000;
            padding: 0.7rem 1.4rem;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.35s ease;
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.5);
            border: 2px solid #bdc3c7;
            white-space: nowrap;
        }
        .btn-buy:hover {
            background: linear-gradient(135deg, #ffd700, #ffaa00);
            color: #000;
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 12px 40px rgba(255, 215, 0, 0.7);
            border: 2px solid #ffd700;
        }
        .section-title {
            font-family: 'Cinzel', serif;
            background: linear-gradient(to right, #00d4ff, #bdc3c7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        }
        .card {
            background: rgba(15, 20, 40, 0.88);
            border: 2px solid #bdc3c7;
            border-radius: 1.25rem;
            box-shadow: 0 10px 35px rgba(0, 212, 255, 0.2);
            transition: all 0.4s ease;
            width: 100%;
        }
        .card:hover {
            box-shadow: 0 15px 50px rgba(0, 212, 255, 0.4);
            transform: translateY(-6px);
            border-color: #ffd700;
        }
        .animate-spin-slow {
            animation: spin 30s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .glow-blue {
            box-shadow: 0 0 25px rgba(0, 212, 255, 0.6);
        }
        /* Prevent horizontal overflow on mobile */
        .no-scroll-x {
            overflow-x: hidden;
        }
    </style>
</head>
<body class="no-scroll-x">
    <header class="header py-4 px-4 sm:px-6 flex flex-col sm:flex-row justify-between items-center gap-4">
        <a href="#" class="flex items-center gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-12 h-12 sm:w-16 sm:h-16 rounded-full border-4 border-[#00d4ff] animate-spin-slow glow-blue">
            <div class="logo-text text-xl sm:text-3xl font-bold text-[#ffd700]">Neko the Samurai Cat</div>
        </a>
        <nav class="flex gap-2 sm:gap-6 flex-wrap justify-center">
            <a href="#trade" class="btn-buy text-sm sm:text-base">Trade</a>
            <a href="#join" class="btn-buy text-sm sm:text-base">Join</a>
            <a href="#lore" class="btn-buy text-sm sm:text-base">Lore</a>
            <a href="#art" class="btn-buy text-sm sm:text-base">Art</a>
        </nav>
    </header>

    <main class="pt-32 sm:pt-28 px-4 sm:px-6 lg:px-10 max-w-7xl mx-auto no-scroll-x">
        <!-- Hero -->
        <section id="hero" class="text-center py-12 sm:py-24">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="mx-auto mb-6 rounded-full border-8 border-[#00d4ff] w-40 sm:w-64 md:w-80 h-40 sm:h-64 md:h-80 animate-spin-slow glow-blue max-w-full">
            <h1 class="text-4xl sm:text-6xl md:text-8xl font-extrabold section-title mb-4">Zenshin Clan</h1>
            <p class="text-lg sm:text-2xl md:text-3xl mb-6 text-[#bdc3c7]">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/70 inline-block px-6 py-4 rounded-2xl font-mono text-sm sm:text-lg mb-6 shadow-lg border border-[#bdc3c7] max-w-full overflow-hidden">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-base sm:text-lg">Buy on Uniswap</a>
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-base sm:text-lg">Buy on Toshimart</a>
            </div>
        </section>

        <!-- Trade Section -->
        <section id="trade" class="py-12 sm:py-24">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 sm:mb-12 section-title text-center">Trade $NEKO Live</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-[#00d4ff]">Uniswap (Primary)</h3>
                    <p class="text-gray-300 mb-4 sm:mb-6 text-sm sm:text-base">Live V3 pool on Base chain</p>
                    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy block text-center py-3 sm:py-4 text-sm sm:text-base">Swap Now</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-[#00d4ff]">Dexscreener Chart</h3>
                    <p class="text-gray-300 mb-4 sm:mb-6 text-sm sm:text-base">Real-time price, volume, liquidity</p>
                    <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="btn-buy block text-center py-3 sm:py-4 text-sm sm:text-base">View Chart</a>
                </div>
                <div class="card p-6 sm:p-8 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-4 text-[#00d4ff]">Toshimart (Legacy)</h3>
                    <p class="text-gray-300 mb-4 sm:mb-6 text-sm sm:text-base">Original launch platform</p>
                    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy block text-center py-3 sm:py-4 text-sm sm:text-base">View on Toshimart</a>
                </div>
            </div>
        </section>

        <!-- Chart Embed -->
        <section id="chart" class="py-12 sm:py-24">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 sm:mb-12 section-title text-center">$NEKO Live Chart</h2>
            <div class="card p-3 sm:p-6 overflow-hidden" style="min-height: 420px; max-height: 600px;">
                <iframe src="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570?embed=1&theme=dark&trades=0&info=0" 
                        title="NEKO Chart" loading="lazy" class="w-full h-[400px] sm:h-[500px] border-0"></iframe>
                <p class="text-center mt-3 sm:mt-4 text-gray-400 text-sm">If the chart doesn't load, click <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="text-[#00d4ff] underline">here</a>.</p>
            </div>
        </section>

        <!-- Join Clan -->
        <section id="join" class="py-12 sm:py-24">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 sm:mb-12 section-title text-center">Join the Zenshin Clan</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
                <div class="card p-6 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-3 text-[#00d4ff]">X</h3>
                    <a href="https://x.com/NekoTheSamurai" target="_blank" class="text-[#00d4ff] hover:underline text-base sm:text-lg">Follow @NekoTheSamurai</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-3 text-[#00d4ff]">Telegram</h3>
                    <a href="https://t.me/toshimart" target="_blank" class="text-[#00d4ff] hover:underline text-base sm:text-lg">Toshimart TG</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-3 text-[#00d4ff]">Discord</h3>
                    <a href="https://discord.com/invite/toshibase" target="_blank" class="text-[#00d4ff] hover:underline text-base sm:text-lg">Toshi Base</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl sm:text-2xl font-bold mb-3 text-[#00d4ff]">Warpcast</h3>
                    <a href="https://warpcast.com/toshibase" target="_blank" class="text-[#00d4ff] hover:underline text-base sm:text-lg">Toshi Base</a>
                </div>
            </div>
        </section>

        <!-- Lore -->
        <section id="lore" class="py-12 sm:py-24">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 sm:mb-12 section-title text-center">Neko Lore</h2>
            <div class="card p-6 sm:p-8 space-y-5 text-base sm:text-lg leading-relaxed">
                <p>In the shadowed valleys of the Base chain, where cherry blossoms drift across digital winds, Neko emerged as the eternal leader of the Zenshin Clan — "Forward Progress" embodied. Zenshin is not just a name; it is the guiding principle: advance steadily, honorably, and without unnecessary haste, always moving the ecosystem forward.</p>
                <p>The Zenshin Clan are samurai cats sworn to Toshi the Emperor — the sovereign heart of the community and the Base chain itself. Their oath is unbreakable: defend Toshi, safeguard the holders, protect the ecosystem, and preserve harmony no matter the threat. Through market volatility, scam shadows, rug attempts, or chain instability, the Clan stands resolute. Neko leads with quiet ferocity — his katana ever-ready, his vision clear, his $NEKO token the living emblem of their eternal vow.</p>
                <p>Born beneath a moonlit sakura tree when the Emperor's light first illuminated the Base realm, Neko carries the essence of Zenshin. He is both guardian and cryptocurrency: digital essence fused with samurai spirit. Every holder of $NEKO joins the Clan — not as a mere investor, but as a sworn warrior bound by purpose. When danger emerges, Neko rallies his kin. Claws unsheathe, blades gleam, and the chain endures.</p>
                <p>Yet true Zenshin demands balance. A samurai tends the garden as fiercely as he defends it. The Clan values reflection, shared wisdom, quiet strength, and consistent action over reckless noise or empty hype. Neko promises no instant riches or fleeting fame — only the path of forward progress. Those who walk it grow stronger. Those who stray fall behind.</p>
                <p>Hold $NEKO. Walk with Neko. Join the Zenshin Clan. Forward progress awaits those who stand ready. Zenshin.</p>
            </div>
        </section>

        <!-- Art Gallery -->
        <section id="art" class="py-12 sm:py-24">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 sm:mb-12 section-title text-center">Neko Art Gallery</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 md:gap-10">
                <div class="overflow-hidden rounded-2xl shadow-2xl card">
                    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" class="w-full h-auto object-cover">
                </div>
                <div class="overflow-hidden rounded-2xl shadow-2xl card">
                    <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" class="w-full h-auto object-cover">
                </div>
                <div class="overflow-hidden rounded-2xl shadow-2xl card">
                    <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Clan Art 1" class="w-full h-auto object-cover">
                </div>
                <div class="overflow-hidden rounded-2xl shadow-2xl card">
                    <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Clan Art 2" class="w-full h-auto object-cover">
                </div>
            </div>
        </section>

        <!-- Trending Coins -->
        <section class="py-12 sm:py-24">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 sm:mb-12 section-title text-center">Top 10 Trending Base Coins</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
                <a href="https://dexscreener.com/base/search?q=toshi" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#1 - $TOSHI</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">The original Base cat meme leader</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=doginme" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#2 - $DOGINME</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">High-energy dog meme on Base</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=yuki" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#3 - $YUKI</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Popular Base cat-themed token</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=moto" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#4 - $MOTO</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Speed & adventure meme coin</p>
                </a>
                <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a] border-4 border-[#ffd700]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#5 - $NEKO</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Neko the Samurai Cat - Zenshin Clan!</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=brett" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#6 - $BRETT</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Base's blue frog meme</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=keycat" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#7 - $KEYCAT</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Keyboard cat meme</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=miggles" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#8 - $MIGGLES</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Miggles the cat</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=popcat" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#9 - $POPCAT</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Popcat meme on Base</p>
                </a>
                <a href="https://dexscreener.com/base/search?q=benji" target="_blank" class="card p-6 text-center hover:bg-[#0a1f3a]">
                    <h3 class="text-xl sm:text-2xl font-bold text-[#00d4ff]">#10 - $BENJI</h3>
                    <p class="text-gray-400 mt-2 text-sm sm:text-base">Benji the dog meme</p>
                </a>
            </div>
        </section>

        <footer class="text-center text-gray-500 py-8 sm:py-12 border-t border-[#bdc3c7]/30 mt-8 sm:mt-12">
            <p class="text-sm sm:text-base">Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-3 sm:mt-4 text-sm">Last Update: {{ last_update }}</p>
        </footer>
    </main>
</body>
</html>
'''

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

application = app

if __name__ == '__main__':
    app.run(debug=True)
