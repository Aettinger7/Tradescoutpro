from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update, current_path='/')

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        }
        .header { 
            background: linear-gradient(to right, #c8102e, rgba(0,0,0,0.92)); 
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 25px rgba(200, 16, 46, 0.6);
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 50;
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
            padding: 0.75rem 1.5rem;
            border-radius: 9999px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.35s ease;
            white-space: nowrap;
            box-shadow: 0 6px 20px rgba(200, 16, 46, 0.5), inset 0 1px 3px rgba(255,255,255,0.15);
            border: 1px solid rgba(255,215,0,0.3);
            font-size: 0.875rem;
        }
        .btn-red:hover {
            background: linear-gradient(135deg, #FFD700, #FF8C00);
            color: #000;
            transform: translateY(-2px) scale(1.06);
            box-shadow: 0 12px 35px rgba(255, 215, 0, 0.7), inset 0 1px 4px rgba(255,255,255,0.25);
            border: 1px solid #FFD700;
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
    <header class="header py-4 px-4 sm:py-6 sm:px-8 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-3 sm:gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-10 h-10 sm:w-14 sm:h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover">
            <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-3 sm:gap-4">
            <a href="#lore" class="btn-red">Lore</a>
            <a href="#art" class="btn-red">Art</a>
            <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red">Buy on Uniswap</a>
        </div>
    </header>

    <main class="pt-20 p-4 text-center">
        <section id="hero" class="mb-12">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="hero-img mx-auto mb-8 rounded-full animate-spin-slow border-8 border-yellow-500 w-48 sm:w-72 h-48 sm:h-72"
                 loading="lazy">
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

        <section id="trade" class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-10 section-title text-center">Live on Toshimart (Bonding Curve)</h2>
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

        <section id="chart" class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-10 section-title text-center">$NEKO Chart & Trade</h2>
            <div class="card p-4 sm:p-6" style="min-height: 520px;">
                <iframe src="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" title="Toshimart Neko Chart" loading="lazy" style="height: 500px;"></iframe>
                <p class="text-center mt-4 text-gray-400">If the embed doesn't load, click <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="text-yellow-400 underline">here</a> to open directly.</p>
            </div>
        </section>

        <section id="join" class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-10 section-title text-center">Join the Zenshin Clan</h2>
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

        <section id="lore" class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-10 section-title text-center">Neko Lore</h2>
            <div class="card p-6 sm:p-8">
                <p class="text-lg mb-4">Neko of the Zenshin clan! Zenshin means 'Forward Progress'. Find $neko on @toshimart CA: 0x28973c4ef9ae754b076a024996350d3b16a38453</p>
                <p class="text-lg mb-4">GM fren! Neko hopes you have an amazing day!</p>
                <p class="text-lg mb-4">GM! Soft paws, sharp steel. I walk the path of shadows to protect the light of the village. $neko $toshi @baseapp</p>
                <p class="text-lg mb-4">'Fate whispers to Neko, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'' You can find $neko on @toshimart 0x28973c4ef9ae754b076a024996350d3b16a38453</p>
                <p class="text-lg">GM! Slow mornings are always the best! Neko always stops to enjoy the small things in life. 0x28973c4ef9ae754b076a024996350d3b16a38453 Join us on @toshimart</p>
            </div>
        </section>

        <section id="art" class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-10 section-title text-center">Neko Art Gallery</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="rounded-xl">
                <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Tweet Media" class="rounded-xl">
                <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Tweet Media" class="rounded-xl">
                <!-- Add more art images as needed -->
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-10 section-title text-center">Top 10 Trending Base Coins</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <a href="https://x.com/NekoTheSamurai/status/2013677063660622204" target="_blank" class="tweet-card card p-6 flex flex-col gap-4">
                    <div class="flex items-center gap-2">
                        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="spinner-logo rounded-full animate-spin-slow border-2 border-yellow-500 object-cover" loading="lazy">
                        <p class="text-gray-300 italic">"Neko of the Zenshin clan! Zenshin means 'Forward Progress'. Find $neko on @toshimart CA: 0x28973c4ef9ae754b076a024996350d3b16a38453"</p>
                    </div>
                    <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Tweet Media" class="tweet-media" loading="lazy">
                    <button class="btn-red text-sm self-end">View on X</button>
                </a>
                <a href="https://x.com/NekoTheSamurai/status/2013672007116955790" target="_blank" class="tweet-card card p-6 flex flex-col gap-4">
                    <div class="flex items-center gap-2">
                        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="spinner-logo rounded-full animate-spin-slow border-2 border-yellow-500 object-cover" loading="lazy">
                        <p class="text-gray-300 italic">"GM fren! Neko hopes you have an amazing day!"</p>
                    </div>
                    <button class="btn-red text-sm self-end">View on X</button>
                </a>
                <!-- Add the other tweet cards here -->
            </div>
        </section>

        <footer class="text-center text-gray-400 py-10 border-t border-red-800">
            <p>Powered by Toshimart on Base • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-2">Last Update: {{ last_update }}</p>
        </footer>
    </div>
</body>
</html>
'''

LORE_TEMPLATE = SHARED_HEAD + '''
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-4 sm:px-6 pt-24 sm:pt-32 pb-20 max-w-7xl">
        <section class="text-center mb-20">
            <h1 class="text-4xl sm:text-5xl md:text-7xl font-extrabold mb-6 section-title">Neko Lore</h1>
            <p class="text-xl sm:text-2xl mb-8">The Path of the Samurai Cat</p>
        </section>
        <div class="card p-6 sm:p-8">
            <p class="text-lg mb-4">Neko is the silent guardian of the village: soft paws tread quietly in the dawn mist, yet claws are always ready to defend the light. Born under cherry blossoms and forged in shadow, Neko walks the path of Zenshin—forward progress without haste, honor without pride.</p>
            <p class="text-lg mb-4">"Fate whispers to Neko, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'" This is not arrogance, but acceptance of one's own power when the moment demands it. The true warrior does not seek the storm — the storm finds the warrior.</p>
            <p class="text-lg mb-4">Every dawn brings new lessons: enjoy slow mornings with tea and reflection, sharpen the blade in silence, protect what is precious without seeking glory. The warrior in the garden tends to both peace and strength, knowing that true power lies in restraint.</p>
            <p class="text-lg mb-4">The clan grows not through noise or hype, but through shared wisdom, quiet resolve, and consistent action. Neko does not promise riches or fame — only the path. Those who walk it become stronger. Those who stray are left behind.</p>
            <p class="text-lg">Join the Zenshin Clan. Forward progress awaits. Zenshin.</p>
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
    <div class="container mx-auto px-4 sm:px-6 pt-24 sm:pt-32 pb-20 max-w-7xl">
        <section class="text-center mb-20">
            <h1 class="text-4xl sm:text-5xl md:text-7xl font-extrabold mb-6 section-title">Neko Art Gallery</h1>
            <p class="text-xl sm:text-2xl mb-8">Visions of the Samurai Cat</p>
        </section>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" class="rounded-xl shadow-2xl w-full h-auto">
            <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" class="rounded-xl shadow-2xl w-full h-auto">
            <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Neko Clan Art 1" class="rounded-xl shadow-2xl w-full h-auto">
            <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Neko Clan Art 2" class="rounded-xl shadow-2xl w-full h-auto">
            <!-- Add additional images here if you have more -->
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
