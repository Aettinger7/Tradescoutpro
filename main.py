from flask import Flask, render_template_string
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/')
def index():
    # Using modern timezone-aware UTC for 2026
    last_update = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

application = app

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko the Samurai Cat - $NEKO</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Quicksand:wght@300;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --glow-amber: rgba(255, 191, 0, 0.6);
            --deep-red: #c8102e;
        }
        body {
            margin: 0;
            background: #0a0a0a;
            /* Using a high-quality atmospheric background */
            background-image: 
                linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)),
                url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png');
            background-size: cover;
            background-attachment: fixed;
            color: #e5e5e5;
            font-family: 'Quicksand', sans-serif;
            scroll-behavior: smooth;
        }
        .cinzel { font-family: 'Cinzel', serif; }

        /* Glassmorphism Navigation */
        .header {
            background: rgba(10, 10, 10, 0.75);
            backdrop-filter: blur(15px);
            border-bottom: 1px solid rgba(255, 191, 0, 0.2);
            position: fixed;
            top: 0; width: 100%; z-index: 1000;
        }

        /* Glowing Amber Buttons */
        .btn-action {
            background: rgba(255, 191, 0, 0.1);
            border: 1px solid #ffbf00;
            color: #ffbf00;
            padding: 0.6rem 1.4rem;
            border-radius: 8px;
            transition: all 0.3s ease;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 1px;
        }
        .btn-action:hover {
            background: #ffbf00;
            color: #000;
            box-shadow: 0 0 20px var(--glow-amber);
            transform: translateY(-2px);
        }

        /* Hero Image - Circular Border & Glow */
        .hero-img {
            border: 4px solid #ffbf00;
            box-shadow: 0 0 40px rgba(255, 191, 0, 0.3);
            transition: transform 0.5s ease;
        }
        .hero-img:hover { transform: scale(1.02); }

        /* Transparent Glass Cards */
        .glass-card {
            background: rgba(20, 20, 20, 0.6);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .glass-card:hover {
            border-color: #ffbf00;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transform: translateY(-5px);
        }

        /* Gradient Text */
        .text-gold {
            background: linear-gradient(135deg, #ffed4a 0%, #ffbf00 50%, #e6ac00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
</head>
<body class="pb-12">
    <header class="header py-4 px-8 flex justify-between items-center">
        <div class="flex items-center gap-3">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" class="w-10 h-10 rounded-full border border-yellow-500">
            <span class="cinzel text-xl font-bold tracking-widest text-gold hidden sm:block">NEKO SAMURAI</span>
        </div>
        <nav class="flex gap-4">
            <a href="#trade" class="text-sm font-bold hover:text-yellow-500 transition">TRADE</a>
            <a href="#lore" class="text-sm font-bold hover:text-yellow-500 transition">LORE</a>
            <a href="#art" class="text-sm font-bold hover:text-yellow-500 transition">ART</a>
        </nav>
    </header>

    <main class="pt-32 px-4 max-w-6xl mx-auto">
        <section class="text-center mb-24">
            <div class="relative inline-block mb-10">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko" class="hero-img w-48 h-48 sm:w-64 sm:h-64 rounded-full mx-auto object-cover">
            </div>
            <h1 class="cinzel text-6xl sm:text-8xl font-bold mb-4 text-gold">Zenshin Clan</h1>
            <p class="text-xl sm:text-2xl font-light text-gray-300 italic mb-8">
                "Forward Progress — Warrior in a garden, claws sharpened on Base."
            </p>
            <div class="glass-card inline-block px-6 py-3 mb-10 border-yellow-900/50">
                <code class="text-yellow-500 text-sm sm:text-base">CA: 0x28973c4ef9ae754b076a024996350d3b16a38453</code>
            </div>
            <div class="flex flex-wrap justify-center gap-4">
                <a href="#" class="btn-action">Swap Now</a>
                <a href="#" class="btn-action">Buy on Toshimart</a>
            </div>
        </section>

        <section id="trade" class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-24">
            <div class="space-y-6">
                <h2 class="cinzel text-3xl text-gold mb-8">Trade $NEKO Live</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="glass-card p-6 border-l-4 border-l-yellow-600">
                        <h3 class="font-bold text-lg mb-2">Uniswap</h3>
                        <p class="text-sm text-gray-400 mb-4">Live V3 pool on Base</p>
                        <a href="#" class="text-xs font-bold text-yellow-500 underline">SWAP NOW</a>
                    </div>
                    <div class="glass-card p-6">
                        <h3 class="font-bold text-lg mb-2">Dexscreener</h3>
                        <p class="text-sm text-gray-400 mb-4">Real-time analytics</p>
                        <a href="#" class="text-xs font-bold text-yellow-500 underline">VIEW CHART</a>
                    </div>
                </div>
            </div>
            
            <div class="glass-card p-2 overflow-hidden h-[400px]">
                <iframe src="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570?embed=1&theme=dark&trades=0&info=0" 
                        style="width: 100%; height: 100%; border: 0;"></iframe>
            </div>
        </section>

        <section id="lore" class="mb-24">
            <div class="glass-card p-8 sm:p-12 relative overflow-hidden">
                <div class="absolute top-0 right-0 p-8 opacity-10">
                    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" class="w-64">
                </div>
                <h2 class="cinzel text-4xl text-gold mb-6">Neko Lore</h2>
                <div class="space-y-4 text-gray-300 leading-relaxed max-w-3xl">
                    <p>Neko is the silent guardian: soft paws tread quietly in the dawn mist, yet claws are always ready. Born under cherry blossoms and forged in shadow, Neko walks the path of Zenshin—forward progress without haste.</p>
                    <p class="italic text-yellow-500/80">"Fate whispers to Neko, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'"</p>
                </div>
            </div>
        </section>

        <section class="mb-24">
            <h2 class="cinzel text-3xl text-center text-gold mb-12">Top 10 Trending Base Coins</h2>
            <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
                {% set coins = [
                    ('$TOSHI', '#1'), ('$DOGINME', '#2'), ('$YUKI', '#3'), ('$MOTO', '#4'), 
                    ('$NEKO', 'CLAN'), ('$BRETT', '#6'), ('$KEYCAT', '#7'), ('$MIGGLES', '#8'), 
                    ('$POPCAT', '#9'), ('$BENJI', '#10')
                ] %}
                {% for name, rank in coins %}
                <div class="glass-card p-4 text-center border-yellow-500/20">
                    <span class="block text-[10px] text-yellow-600 font-bold mb-1">{{ rank }}</span>
                    <span class="font-bold text-sm">{{ name }}</span>
                </div>
                {% endfor %}
            </div>
        </section>
    </main>

    <footer class="text-center py-12 border-t border-yellow-900/30">
        <p class="text-xs text-gray-500 tracking-widest uppercase mb-4">
            Now Live on Uniswap (Base) • DYOR • © 2026 Neko
        </p>
        <p class="text-[10px] text-gray-600">Last System Update: {{ last_update }}</p>
    </footer>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
