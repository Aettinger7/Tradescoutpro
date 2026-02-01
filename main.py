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
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            background: linear-gradient(to bottom, #000000, #0a0f1a);
            color: #d0d0d8;
            font-family: 'Segoe UI', Arial, sans-serif;
            scroll-behavior: smooth;
            overflow-x: hidden;
        }
        .header {
            background: rgba(10, 15, 30, 0.92);
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(0, 212, 255, 0.25);
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            border-bottom: 1px solid rgba(189, 195, 199, 0.2);
        }
        .btn-trade {
            background: linear-gradient(135deg, #00d4ff, #0099cc);
            color: #000;
            padding: 0.8rem 1.8rem;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.35s ease;
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.4);
            border: 2px solid #bdc3c7;
            position: relative;
            overflow: hidden;
        }
        .btn-trade:hover {
            background: linear-gradient(135deg, #ffd700, #ffaa00);
            color: #000;
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 12px 40px rgba(255, 215, 0, 0.6);
            border-color: #ffd700;
        }
        /* Slash effect on hover */
        .btn-trade::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -100%;
            width: 200%;
            height: 200%;
            background: url('https://pnglove.com/data/img/2485_hVRZ.jpg') center/contain no-repeat; /* blue slash PNG */
            opacity: 0;
            transform: rotate(-45deg) scale(0.5);
            transition: all 0.6s ease;
            pointer-events: none;
        }
        .btn-trade:hover::after {
            opacity: 0.7;
            left: 50%;
            transform: rotate(-45deg) scale(1.2);
        }
        .section-title {
            font-family: 'Cinzel', serif;
            background: linear-gradient(to right, #00d4ff, #bdc3c7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        }
        .card {
            background: rgba(15, 20, 40, 0.85);
            border: 1px solid #bdc3c7;
            border-radius: 1.25rem;
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.15);
            transition: all 0.4s ease;
        }
        .card:hover {
            box-shadow: 0 15px 50px rgba(0, 212, 255, 0.35);
            transform: translateY(-6px);
            border-color: #ffd700;
        }
        .accent-blue { color: #00d4ff; }
        .accent-silver { color: #bdc3c7; }
        .accent-gold { color: #ffd700; }
        .animate-spin-slow {
            animation: spin 35s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .glow-blue { box-shadow: 0 0 25px rgba(0, 212, 255, 0.6); }
        /* Page-load slash in hero */
        .hero-slash {
            position: absolute;
            top: 20%;
            left: -20%;
            width: 140%;
            height: 60%;
            background: url('https://www.shutterstock.com/shutterstock/photos/2671545117/display_1500/stock-vector-blue-glowing-slash-effect-with-curved-motion-trails-on-transparent-background-used-in-combat-2671545117.jpg') center/contain no-repeat;
            opacity: 0;
            transform: rotate(-30deg) translateX(-100%);
            animation: slashReveal 4s ease-out forwards;
            pointer-events: none;
            z-index: -1;
        }
        @keyframes slashReveal {
            0% { opacity: 0; transform: rotate(-30deg) translateX(-100%); }
            20% { opacity: 0.8; transform: rotate(-30deg) translateX(20%); }
            40% { opacity: 0.6; transform: rotate(-30deg) translateX(60%); }
            100% { opacity: 0; transform: rotate(-30deg) translateX(150%); }
        }
    </style>
</head>
<body>
    <header class="header py-4 px-6 flex justify-between items-center">
        <a href="#" class="flex items-center gap-4 relative">
            <!-- Katana image on left of logo -->
            <img src="https://katana-sword.com/cdn/shop/files/katana-yoru8_800x.jpg" 
                 alt="Katana" 
                 class="h-16 w-auto object-contain opacity-80">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-12 h-12 sm:w-16 sm:h-16 rounded-full border-4 border-[#00d4ff] animate-spin-slow glow-blue">
            <div class="logo-text text-2xl sm:text-3xl accent-gold font-bold">Neko the Samurai Cat</div>
        </a>
        <nav class="flex gap-3 sm:gap-6 flex-wrap">
            <a href="#trade" class="btn-trade">Trade</a>
            <a href="#join" class="btn-trade">Join</a>
            <a href="#lore" class="btn-trade">Lore</a>
            <a href="#art" class="btn-trade">Art</a>
        </nav>
    </header>

    <main class="pt-28 px-4 sm:px-6 lg:px-10 max-w-7xl mx-auto relative">
        <!-- Hero with animated slash -->
        <section id="hero" class="text-center py-16 sm:py-24 relative overflow-hidden">
            <div class="hero-slash"></div> <!-- Animated slash container -->
            <img src="https://katana-sword.com/cdn/shop/files/katana-yoru14_800x.jpg" 
                 alt="Katana Background" 
                 class="absolute inset-0 w-full h-full object-cover opacity-10 pointer-events-none">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="mx-auto mb-8 rounded-full border-8 border-[#00d4ff] w-48 sm:w-64 md:w-80 h-48 sm:h-64 md:h-80 animate-spin-slow glow-blue relative z-10">
            <h1 class="text-5xl sm:text-7xl md:text-8xl font-extrabold section-title mb-6 relative z-10">Zenshin Clan</h1>
            <p class="text-xl sm:text-2xl md:text-3xl mb-8 accent-silver relative z-10">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/70 inline-block px-8 py-5 rounded-2xl font-mono text-base sm:text-lg mb-8 shadow-lg border border-[#bdc3c7] relative z-10">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <div class="flex flex-col sm:flex-row gap-4 justify-center relative z-10">
                <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-trade text-lg">Buy on Uniswap</a>
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-trade text-lg">Buy on Toshimart</a>
            </div>
        </section>

        <!-- Rest of your sections remain the same - just update colors as before -->
        <!-- ... paste your existing trade, chart, join, lore, art, trending, footer here ... -->

        <footer class="text-center text-gray-500 py-12 border-t border-[#bdc3c7]/30 mt-12">
            <p>Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-4">Last Update: {{ last_update }}</p>
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

