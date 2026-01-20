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
        html, body {
            margin: 0;
            overflow-x: hidden;          /* Prevents horizontal scroll */
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
            font-size: 1.25rem sm:2rem md:2.5rem;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
            white-space: nowrap;
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
            font-size: 2rem sm:3rem md:4rem;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 25px rgba(255, 215, 0, 0.7);
        }
        .btn-buy {
            background: #FF0000;
            color: white;
            padding: 10px 20px;
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
            width: 10rem sm:14rem md:18rem; 
            height: 10rem sm:14rem md:18rem; 
            object-fit: cover;
            filter: drop-shadow(0 0 25px rgba(255,215,0,0.6)); 
        }
        iframe, .tweet-media { 
            max-width: 100%; 
            height: auto; 
            border-radius: 0.5rem; 
        }
        .tweet-card { cursor: pointer; }
        .spinner-logo { 
            width: 1.75rem; 
            height: 1.75rem; 
            object-fit: cover; 
            aspect-ratio: 1 / 1;
        }
        img.rounded-full { 
            object-fit: cover; 
            aspect-ratio: 1 / 1;
            flex-shrink: 0;
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
    <header class="header py-3 px-4 sm:py-5 sm:px-6 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-2 sm:gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-9 h-9 sm:w-12 sm:h-12 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover flex-shrink-0"
                 onerror="this.src='https://via.placeholder.com/56/FFD700/000?text=Neko';">
            <div class="logo-text">Neko the Samurai Cat</div>
        </a>
        <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-sm sm:text-base">Buy $NEKO Now</a>
    </header>

    <div class="container mx-auto px-4 sm:px-6 pt-20 sm:pt-28 pb-20 max-w-7xl">
        <section class="text-center mb-16 sm:mb-20">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="hero-img mx-auto mb-6 rounded-full animate-spin-slow border-8 border-yellow-500 object-cover"
                 loading="lazy"
                 onerror="this.src='https://via.placeholder.com/300/FFD700/000?text=Neko+Hero'; this.alt='Fallback Neko Image';">
            <h1 class="text-4xl sm:text-6xl md:text-7xl font-extrabold mb-6 section-title">Zenshin Clan</h1>
            <p class="text-lg sm:text-2xl mb-8">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/60 inline-block px-6 py-3 sm:px-8 sm:py-4 rounded-xl mb-6 font-mono text-base sm:text-lg">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <br>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('Contract Address Copied!')" 
                    class="mt-4 px-6 sm:px-8 py-3 bg-yellow-600 text-black rounded-full font-bold hover:bg-yellow-500 text-base sm:text-lg">
                Copy CA
            </button>
        </section>

        <!-- Rest of the sections remain the same as previous version for brevity – copy from your last working code if needed, but apply the same responsive padding reductions (e.g., p-6 → p-4 sm:p-6 on cards) -->

        <section class="mb-16 sm:mb-20">
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 section-title text-center">Live on Toshimart (Bonding Curve)</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Your card content here – keep as-is, but ensure p-6 sm:p-8 on cards -->
            </div>
        </section>

        <!-- Chart, Join Clan, Recent Updates sections – no major changes needed beyond existing responsive classes -->

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
