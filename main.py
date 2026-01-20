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
    <title>Neko the Samurai Cat - Official Memecoin Site</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        html, body {
            margin: 0;
            overflow-x: hidden;
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
            font-size: 1.125rem sm:1.75rem md:2.25rem;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
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
            font-size: 2.25rem sm:4rem;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 25px rgba(255, 215, 0, 0.7);
        }
        .btn-buy {
            background: #FF0000;
            color: white;
            padding: 8px 16px;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.3s;
        }
        .btn-buy:hover {
            background: #FFD700;
            color: black;
            transform: scale(1.05);
        }
        .animate-spin-slow { animation: spin 30s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .hero-img-container {
            width: 9rem sm:12rem md:16rem;
            height: 9rem sm:12rem md:16rem;
            border-radius: 9999px;
            overflow: hidden;
            border: 6px solid #FFD700;
        }
        .hero-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .logo-container {
            width: 2.5rem sm:3.5rem;
            height: 2.5rem sm:3.5rem;
            border-radius: 9999px;
            overflow: hidden;
            border: 3px solid #FFD700;
            flex-shrink: 0;
        }
        .logo-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        iframe, img, video {
            max-width: 100%;
            height: auto;
        }
        .spinner-logo-container {
            width: 1.75rem;
            height: 1.75rem;
            border-radius: 9999px;
            overflow: hidden;
            border: 2px solid #FFD700;
            flex-shrink: 0;
        }
    </style>
</head>
<body>
    <header class="header py-2 px-4 sm:py-4 sm:px-6 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-2 sm:gap-3">
            <div class="logo-container">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko Logo" 
                     class="logo-img animate-spin-slow"
                     onerror="this.src='https://via.placeholder.com/40/FFD700/000?text=Neko';">
            </div>
            <div class="logo-text">Neko the Samurai Cat</div>
        </a>
        <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-xs sm:text-sm">Buy $NEKO Now</a>
    </header>

    <div class="container mx-auto px-4 sm:px-6 pt-16 sm:pt-24 pb-16 max-w-7xl">
        <section class="text-center mb-12">
            <div class="hero-img-container mx-auto mb-6 animate-spin-slow">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko the Samurai Cat" 
                     class="hero-img"
                     loading="lazy"
                     onerror="this.src='https://via.placeholder.com/200/FFD700/000?text=Neko+Hero';">
            </div>
            <h1 class="text-4xl sm:text-6xl font-extrabold mb-4 section-title">Zenshin Clan</h1>
            <p class="text-lg sm:text-2xl mb-6">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/60 inline-block px-6 py-3 rounded-xl mb-6 font-mono text-base">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <br>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('Contract Address Copied!')" 
                    class="mt-2 px-6 py-3 bg-yellow-600 text-black rounded-full font-bold hover:bg-yellow-500 text-base">
                Copy CA
            </button>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 section-title text-center">Live on Toshimart (Bonding Curve)</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="card p-6 text-center">
                    <h3 class="text-xl font-bold mb-4 text-yellow-400">Price / Stats</h3>
                    <p class="text-2xl font-bold mb-2">Check Live</p>
                    <p class="text-gray-300 mb-4">Bonding curve – price rises as more buy</p>
                    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy inline-block mt-4">View on Toshimart</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl font-bold mb-4 text-yellow-400">Market Cap / Liquidity</h3>
                    <p class="text-gray-300">Dynamic via bonding curve. Early holders get best entry.</p>
                    <p class="text-sm mt-4 text-gray-400">No Dexscreener yet – coming soon after curve completes</p>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl font-bold mb-4 text-yellow-400">Holders / Volume</h3>
                    <p class="text-gray-300">Growing clan – join before migration.</p>
                    <p class="text-sm mt-4 text-gray-400">Trade with ETH on Toshimart</p>
                </div>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 section-title text-center">$NEKO Chart & Trade</h2>
            <div class="card p-4" style="min-height: 400px;">
                <iframe src="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" title="Toshimart Neko Chart" loading="lazy" style="height: 400px;"></iframe>
                <p class="text-center mt-4 text-gray-400">If the embed doesn't load, click <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="text-yellow-400 underline">here</a>.</p>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 section-title text-center">Join the Zenshin Clan</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="card p-6 text-center">
                    <h3 class="text-xl font-bold mb-4">X</h3>
                    <a href="https://x.com/NekoTheSamurai" target="_blank" class="text-yellow-400 hover:underline text-xl">Follow @NekoTheSamurai</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl font-bold mb-4">Telegram</h3>
                    <a href="https://t.me/toshimart" target="_blank" class="text-yellow-400 hover:underline text-xl">Toshimart TG</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl font-bold mb-4">Discord</h3>
                    <a href="https://discord.com/invite/toshibase" target="_blank" class="text-yellow-400 hover:underline text-xl">Toshi Base</a>
                </div>
                <div class="card p-6 text-center">
                    <h3 class="text-xl font-bold mb-4">Warpcast</h3>
                    <a href="https://warpcast.com/toshibase" target="_blank" class="text-yellow-400 hover:underline text-xl">Toshi Base</a>
                </div>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 section-title text-center">Recent Clan Updates</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <a href="https://x.com/NekoTheSamurai/status/2013677063660622204" target="_blank" class="card p-6 flex flex-col gap-4 cursor-pointer">
                    <div class="flex items-center gap-3">
                        <div class="spinner-logo-container">
                            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="logo-img animate-spin-slow">
                        </div>
                        <p class="text-gray-300 italic">"Neko of the Zenshin clan! Zenshin means 'Forward Progress'. Find $neko on @toshimart CA: 0x28973c4ef9ae754b076a024996350d3b16a38453"</p>
                    </div>
                    <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Tweet Media" loading="lazy">
                    <button class="btn-buy text-sm self-end">View on X</button>
                </a>
                <!-- Add your other tweet cards here in the same format -->
                <!-- Example for second tweet -->
                <a href="https://x.com/NekoTheSamurai/status/2013672007116955790" target="_blank" class="card p-6 flex flex-col gap-4 cursor-pointer">
                    <div class="flex items-center gap-3">
                        <div class="spinner-logo-container">
                            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="logo-img animate-spin-slow">
                        </div>
                        <p class="text-gray-300 italic">"GM fren! Neko hopes you have an amazing day!"</p>
                    </div>
                    <button class="btn-buy text-sm self-end">View on X</button>
                </a>
                <!-- Continue with remaining tweets -->
            </div>
        </section>

        <footer class="text-center text-gray-400 py-8 border-t border-red-800">
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

if __name__ == '__main__':
    app.run(debug=True)
