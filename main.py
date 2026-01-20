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
        .btn-buy {
            background: #FF0000;
            color: white;
            padding: 12px 28px;
            border-radius: 9999px;
            font-weight: bold;
            text-decoration: none;
            transition: all 0.3s;
        }
        .btn-buy:hover {
            background: #FFD700;
            color: black;
            transform: scale(1.05);
        }
        .animate-spin-slow { animation: spin 30s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .hero-img { 
            object-fit: cover;
            filter: drop-shadow(0 0 25px rgba(255,215,0,0.6)); 
            aspect-ratio: 1 / 1;
        }
        iframe { border: none; width: 100%; height: 500px; }
        .tweet-card { cursor: pointer; }
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
    <!-- Preload background for faster render -->
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
        <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-base sm:text-lg">Buy $NEKO Now</a>
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
                    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy inline-block mt-4">View on Toshimart</a>
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
            <h2 class="section-title text-3xl sm:text-5xl font-extrabold mb-10 text-center">Recent Clan Updates</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Tweet 1 -->
                <a href="https://x.com/NekoTheSamurai/status/2013677063660622204" target="_blank" class="tweet-card card p-6 flex flex-col gap-4">
                    <div class="flex items-center gap-2">
                        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="spinner-logo w-8 h-8 rounded-full animate-spin-slow border-2 border-yellow-500" loading="lazy">
                        <p class="text-gray-300 italic">"Neko of the Zenshin clan! Zenshin means 'Forward Progress'. Find $neko on @toshimart CA: 0x28973c4ef9ae754b076a024996350d3b16a38453"</p>
                    </div>
                    <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Tweet Media" class="tweet-media" loading="lazy">
                    <button class="btn-buy text-sm self-end">View on X</button>
                </a>
                <!-- Tweet 2 -->
                <a href="https://x.com/NekoTheSamurai/status/2013672007116955790" target="_blank" class="tweet-card card p-6 flex flex-col gap-4">
                    <div class="flex items-center gap-2">
                        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="spinner-logo w-8 h-8 rounded-full animate-spin-slow border-2 border-yellow-500" loading="lazy">
                        <p class="text-gray-300 italic">"GM fren! Neko hopes you have an amazing day!"</p>
                    </div>
                    <button class="btn-buy text-sm self-end">View on X</button>
                </a>
                <!-- Tweet 3 -->
                <a href="https://x.com/NekoTheSamurai/status/2013668982323323071" target="_blank" class="tweet-card card p-6 flex flex-col gap-4">
                    <div class="flex items-center gap-2">
                        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="spinner-logo w-8 h-8 rounded-full animate-spin-slow border-2 border-yellow-500" loading="lazy">
                        <p class="text-gray-300 italic">"GM! Soft paws, sharp steel. I walk the path of shadows to protect the light of the village. $neko $toshi @baseapp"</p>
                    </div>
                    <video controls class="tweet-media">
                        <source src="https://video.twimg.com/tweet_video/G_H8qiGXgAACZpp.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                    <button class="btn-buy text-sm self-end">View on X</button>
                </a>
                <!-- Tweet 4 -->
                <a href="https://x.com/NekoTheSamurai/status/2013667665399668882" target="_blank" class="tweet-card card p-6 flex flex-col gap-4">
                    <div class="flex items-center gap-2">
                        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="spinner-logo w-8 h-8 rounded-full animate-spin-slow border-2 border-yellow-500" loading="lazy">
                        <p class="text-gray-300 italic">"'Fate whispers to Neko, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'' You can find $neko on @toshimart 0x28973c4ef9ae754b076a024996350d3b16a38453"</p>
                    </div>
                    <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Tweet Media" class="tweet-media" loading="lazy">
                    <button class="btn-buy text-sm self-end">View on X</button>
                </a>
                <!-- Tweet 5 -->
                <a href="https://x.com/NekoTheSamurai/status/2013666263554498876" target="_blank" class="tweet-card card p-6 flex flex-col gap-4">
                    <div class="flex items-center gap-2">
                        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="spinner-logo w-8 h-8 rounded-full animate-spin-slow border-2 border-yellow-500" loading="lazy">
                        <p class="text-gray-300 italic">"GM! Slow mornings are always the best! Neko always stops to enjoy the small things in life. 0x28973c4ef9ae754b076a024996350d3b16a38453 Join us on @toshimart"</p>
                    </div>
                    <video controls class="tweet-media">
                        <source src="https://video.twimg.com/amplify_video/2013665903586484224/vid/avc1/464x688/3jkq97b-iiBAga0l.mp4?tag=23" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                    <button class="btn-buy text-sm self-end">View on X</button>
                </a>
            </div>
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

if __name__ == '__main__':
    app.run(debug=True)
