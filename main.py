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
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://pbs.twimg.com/media/G-9Z6XQXMAA7ln4.jpg') no-repeat center center fixed; 
            background-size: cover; 
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
    </style>
    <script>
        if ('scrollRestoration' in history) {
            history.scrollRestoration = 'manual';
        }
    </script>
</head>
<body>
    <header class="header py-6 px-8 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-14 h-14 rounded-full animate-spin-slow border-4 border-yellow-500"
                 onerror="this.src='https://via.placeholder.com/56/FFD700/000?text=Neko';">
            <div class="logo-text">Neko the Samurai Cat</div>
        </a>
        <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-lg">Buy $NEKO Now</a>
    </header>

    <div class="container mx-auto px-6 pt-40 pb-20 max-w-7xl">  <!-- Increased to pt-40 to fully clear header -->
        <section class="text-center mb-20">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="hero-img mx-auto mb-8 mt-16 rounded-full animate-spin-slow border-8 border-yellow-500"  <!-- Added mt-16 for extra clearance -->
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

        <!-- All other sections remain unchanged – paste them here from your current code if needed -->

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

        <!-- Add your chart, join, updates, footer sections here as before -->

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
