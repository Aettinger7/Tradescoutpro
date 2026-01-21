from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

@app.route('/art')
def art():
    images = [
        "https://i.ibb.co/23RRSb0m/Gemini-Generated-Image-su90ubsu90ubsu90.png",
        "https://i.ibb.co/pjvzgzXH/Gemini-Generated-Image-2gwj062gwj062gwj.png",
        "https://i.ibb.co/3m5Qd14L/Gemini-Generated-Image-sqgje0sqgje0sqgj.png",
        "https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png",
        "https://i.ibb.co/9HzF9yZ1/Gemini-Generated-Image-zx03uzx03uzx03uz.png"
    ]

    # Build the gallery HTML safely
    gallery_items = ""
    for img in images:
        gallery_items += f'''
        <div class="art-item" onclick="openModal('{img}')">
            <img src="{img}" alt="Neko Artwork" class="art-img" loading="lazy">
        </div>
        '''

    art_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Neko Art Gallery - Zenshin Clan</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ 
                margin: 0; padding: 0; overflow-x: hidden;
                background: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), 
                            url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed; 
                background-size: cover; background-attachment: fixed; 
                color: #fff; min-height: 100vh; font-family: sans-serif;
            }}
            header {{ 
                background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.9)); 
                backdrop-filter: blur(10px); position: fixed; top: 0; width: 100%; z-index: 50;
            }}
            .gallery {{ 
                display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); 
                gap: 2rem; max-width: 1600px; margin: 0 auto; padding: 8rem 1.5rem 4rem;
            }}
            .art-item {{ 
                cursor: pointer; transition: transform 0.3s;
            }}
            .art-item:hover {{ transform: scale(1.02); }}
            .art-img {{ 
                width: 100%; height: auto; display: block; 
                border-radius: 16px; box-shadow: 0 10px 30px rgba(255,215,0,0.3);
            }}
            #modal {{ 
                display: none; position: fixed; inset: 0; z-index: 1000; 
                background: rgba(0,0,0,0.96); align-items: center; justify-content: center;
            }}
            #modal.active {{ display: flex; }}
            #modal-img {{ 
                max-width: 95vw; max-height: 95vh; object-fit: contain; 
                border: 5px solid #FFD700; border-radius: 12px; 
                box-shadow: 0 0 60px rgba(255,255,255,0.4);
            }}
            .close {{ 
                position: absolute; top: 1.5rem; right: 2rem; 
                color: white; font-size: 4.5rem; font-weight: bold; cursor: pointer; 
            }}
        </style>
    </head>
    <body>
        <header class="py-4 px-6 flex justify-between items-center">
            <a href="/" class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-full overflow-hidden border-4 border-yellow-500 flex-shrink-0">
                    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                         alt="Neko Logo" class="w-full h-full object-cover animate-spin-slow">
                </div>
                <div class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">
                    Neko the Samurai Cat
                </div>
            </a>
            <a href="/" class="bg-red-600 hover:bg-yellow-500 text-white hover:text-black px-6 py-2 rounded-full font-bold transition-all">
                Back to Home
            </a>
        </header>

        <main class="pt-24">
            <h1 class="text-5xl md:text-6xl font-extrabold text-center mb-10 text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">
                Neko Art Gallery
            </h1>
            <div class="gallery">
                {gallery_items}
            </div>
            <p class="text-center text-gray-400 mt-12 text-lg">
                Click any image to view full high-resolution version • Right-click or long-press to save
            </p>
        </main>

        <div id="modal" onclick="if(event.target === this) closeModal()">
            <span class="close" onclick="closeModal()">×</span>
            <img id="modal-img" src="" alt="Full Resolution Neko Art">
        </div>

        <script>
            function openModal(src) {{
                document.getElementById('modal-img').src = src;
                document.getElementById('modal').classList.add('active');
                document.getElementById('modal').style.display = 'flex';
            }}
            function closeModal() {{
                document.getElementById('modal').classList.remove('active');
                document.getElementById('modal').style.display = 'none';
            }}
        </script>
    </body>
    </html>
    '''
    return art_html

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
            font-size: 2.5rem;
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
            font-size: 3rem;
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
            width: 18rem; 
            height: 18rem; 
            object-fit: cover;
            filter: drop-shadow(0 0 25px rgba(255,215,0,0.6)); 
        }
        iframe { border: none; width: 100%; height: 500px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #FF0000; }
        th { background: rgba(0,0,0,0.6); color: #FFD700; font-weight: bold; }
        tr:hover { background: rgba(255,0,0,0.1); }
    </style>
</head>
<body>
    <header class="header py-6 px-8 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-14 h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover"
                 onerror="this.src='https://via.placeholder.com/56/FFD700/000?text=Neko';">
            <div class="logo-text">Neko the Samurai Cat</div>
        </a>
        <div class="flex gap-4">
            <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-lg">Buy $NEKO Now</a>
            <a href="/art" class="btn-buy text-lg">Art</a>
            <a href="/lore" class="btn-buy text-lg">Lore</a>
        </div>
    </header>

    <div class="container mx-auto px-6 pt-32 pb-20 max-w-7xl">
        <section class="text-center mb-20">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="hero-img mx-auto mb-8 rounded-full animate-spin-slow border-8 border-yellow-500 object-cover"
                 loading="lazy"
                 onerror="this.src='https://via.placeholder.com/300/FFD700/000?text=Neko+Hero'; this.alt='Fallback Neko Image';">
            <h1 class="text-6xl md:text-7xl font-extrabold mb-6 section-title">Zenshin Clan</h1>
            <p class="text-2xl mb-8">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/60 inline-block px-8 py-4 rounded-xl mb-6 font-mono text-lg">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <br>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('Contract Address Copied!')" 
                    class="mt-4 px-8 py-4 bg-yellow-600 text-black rounded-full font-bold hover:bg-yellow-500 text-lg">
                Copy CA
            </button>
        </section>

        <section class="mb-20">
            <h2 class="text-5xl font-extrabold mb-10 section-title text-center">Live on Toshimart (Bonding Curve)</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4 text-yellow-400">Price / Stats</h3>
                    <p class="text-3xl font-bold mb-2">Check Live</p>
                    <p class="text-gray-300 mb-4">Bonding curve – price rises as more buy</p>
                    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy inline-block mt-4">View on Toshimart</a>
                </div>
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4 text-yellow-400">Market Cap / Liquidity</h3>
                    <p class="text-gray-300">Dynamic via bonding curve. Early holders get best entry.</p>
                    <p class="text-sm mt-4 text-gray-400">No Dexscreener yet – coming soon after curve completes</p>
                </div>
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4 text-yellow-400">Holders / Volume</h3>
                    <p class="text-gray-300">Growing clan – join before migration.</p>
                    <p class="text-sm mt-4 text-gray-400">Trade with ETH on Toshimart</p>
                </div>
            </div>
        </section>

        <section class="mb-20">
            <h2 class="text-5xl font-extrabold mb-10 section-title text-center">$NEKO Chart & Trade</h2>
            <div class="card p-6" style="min-height: 520px;">
                <iframe src="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" title="Toshimart Neko Chart" loading="lazy" style="height: 500px;"></iframe>
                <p class="text-center mt-4 text-gray-400">If the embed doesn't load, click <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="text-yellow-400 underline">here</a> to open directly.</p>
            </div>
        </section>

        <section class="mb-20">
            <h2 class="text-5xl font-extrabold mb-10 section-title text-center">Join the Zenshin Clan</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4">X</h3>
                    <a href="https://x.com/NekoTheSamurai" target="_blank" class="text-yellow-400 hover:underline text-xl">Follow @NekoTheSamurai</a>
                </div>
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4">Telegram</h3>
                    <a href="https://t.me/toshimart" target="_blank" class="text-yellow-400 hover:underline text-xl">Toshimart TG</a>
                </div>
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4">Discord</h3>
                    <a href="https://discord.com/invite/toshibase" target="_blank" class="text-yellow-400 hover:underline text-xl">Toshi Base</a>
                </div>
                <div class="card p-8 text-center">
                    <h3 class="text-2xl font-bold mb-4">Warpcast</h3>
                    <a href="https://warpcast.com/toshibase" target="_blank" class="text-yellow-400 hover:underline text-xl">Toshi Base</a>
                </div>
            </div>
        </section>

        <section class="mb-20">
            <h2 class="text-5xl font-extrabold mb-10 section-title text-center">Trending Base Coins</h2>
            <div class="card p-6 overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-black/60">
                            <th class="p-4 font-bold text-yellow-400">Rank</th>
                            <th class="p-4 font-bold text-yellow-400">Ticker</th>
                            <th class="p-4 font-bold text-yellow-400">Buy / Trade</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-red-800">
                            <td class="p-4">1</td>
                            <td class="p-4 font-bold">$TOSHI</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/0x4b0aaf3ebb163dd45f663b38b6d93f6093ebc2d3" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">2</td>
                            <td class="p-4 font-bold">$DOGINME</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/0xade9bcd4b968ee26bed102dd43a55f6a8c2416df" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">3</td>
                            <td class="p-4 font-bold">$YUKI</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/0x438760f167ab00d268a8d83ae8949dd65e57309d" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">4</td>
                            <td class="p-4 font-bold">$MOTO</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/0x904b015aa1088a795e35335b079758455ac8efb5" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">5</td>
                            <td class="p-4 font-bold">$NEKO</td>
                            <td class="p-4"><a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="text-yellow-400 hover:underline">Buy on Toshimart</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">6</td>
                            <td class="p-4 font-bold">$BRETT</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/brett" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">7</td>
                            <td class="p-4 font-bold">$BOOMER</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/boomer" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">8</td>
                            <td class="p-4 font-bold">$PYSOPS</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/pysops" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr class="border-b border-red-800">
                            <td class="p-4">9</td>
                            <td class="p-4 font-bold">$ROLL</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/roll" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                        <tr>
                            <td class="p-4">10</td>
                            <td class="p-4 font-bold">$BASEGUY</td>
                            <td class="p-4"><a href="https://dexscreener.com/base/baseguy" target="_blank" class="text-yellow-400 hover:underline">Buy on DEXScreener</a></td>
                        </tr>
                    </tbody>
                </table>
                <p class="text-center text-gray-400 mt-6 text-sm">Prices and rankings change frequently – always DYOR. Links lead to trusted DEXs/launchpads on Base chain.</p>
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
