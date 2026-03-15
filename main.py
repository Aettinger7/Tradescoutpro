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

    <!-- SEO & Social Meta (unchanged) -->
    <meta name="description" content="Neko the Samurai Cat ($NEKO) – Zenshin Clan meme token on Base. Forward progress with honor. Trade on Uniswap. Join the clan!">
    <meta property="og:title" content="Neko the Samurai Cat ⚔️🐱 $NEKO on Base">
    <meta property="og:description" content="Zenshin Clan – 'Forward Progress'. Warrior in a garden, claws sharpened on Base. Join the samurai cat revolution. CA: 0x28973c4ef9ae754b076a024996350d3b16a38453">
    <meta property="og:image" content="https://i.ibb.co/6cpdFyYv/image-24.jpg">
    <meta property="og:url" content="https://www.nekothesamurai.com">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Neko the Samurai">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Neko the Samurai Cat ⚔️🐱 $NEKO">
    <meta name="twitter:description" content='"Forward Progress" – Join the Zenshin Clan on Base. Samurai cat meme token. Buy on Uniswap / Toshimart.'>
    <meta name="twitter:image" content="https://i.ibb.co/6cpdFyYv/image-24.jpg">
    <meta name="twitter:site" content="@NekoTheSamurai">

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-34WMSCBW1R"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-34WMSCBW1R');
    </script>

    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">

    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            background: linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.95)),
                        url('https://i.postimg.cc/1zn9gsLR/image(24).jpg') no-repeat center center fixed;
            background-size: cover;
            color: #ffebcc;                 /* brighter readable gold-offwhite */
            font-family: Arial, sans-serif;
            line-height: 1.6;
            min-height: calc(100vh);
            overflow-x: hidden;
        }
        header {
            background: rgba(10,10,15,0.96);
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 25px rgba(212,175,55,0.18);
            position: fixed;
            top: 0; left: 0; right: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(212,175,55,0.25);
            padding: 1rem 1.5rem;
        }
        .container { max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; }
        .flex { display: flex; }
        .flex-col { flex-direction: column; }
        .items-center { align-items: center; }
        .justify-between { justify-content: space-between; }
        .justify-center { justify-content: center; }
        .gap-4 { gap: 1rem; }
        .gap-6 { gap: 1.5rem; }
        .text-center { text-align: center; }
        .py-24 { padding-top: 6rem; padding-bottom: 6rem; }
        .pt-32 { padding-top: 8rem; }
        .text-4xl { font-size: 2.25rem; line-height: 2.5rem; }
        .text-6xl { font-size: 3.75rem; line-height: 1; }
        .font-extrabold { font-weight: 800; }
        .font-bold { font-weight: 700; }
        .rounded-full { border-radius: 9999px; }
        .border-4 { border-width: 4px; }
        .border-8 { border-width: 8px; }
        .animate-spin-slow { animation: spin 36s linear infinite; }
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        .glow-gold { box-shadow: 0 0 25px rgba(212,175,55,0.7); }
        .section-title {
            font-family: 'Cinzel', serif;
            background: linear-gradient(to right, #FFD700, #D4AF37, #B8860B);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 25px rgba(212,175,55,0.6);
        }
        .btn-buy {
            background: linear-gradient(135deg, #D4AF37, #B8860B);
            color: #0f0f0f;
            padding: 0.75rem 1.5rem;
            border-radius: 9999px;
            font-weight: bold;
            text-decoration: none;
            box-shadow: 0 6px 20px rgba(212,175,55,0.4);
            border: 2px solid #D4AF37;
            transition: all 0.35s ease;
            white-space: nowrap;
        }
        .btn-buy:hover {
            background: linear-gradient(135deg, #FFD700, #F5C842);
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 12px 40px rgba(255,215,0,0.6);
            border-color: #FFD700;
        }
        .card {
            background: rgba(20,20,30,0.92);
            border: 2px solid rgba(212,175,55,0.5);
            border-radius: 1.25rem;
            padding: 1.5rem;
            box-shadow: 0 10px 35px rgba(0,0,0,0.6);
            transition: all 0.4s ease;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 15px 50px rgba(212,175,55,0.35);
            border-color: #FFD700;
        }
        .grid {
            display: grid;
            gap: 1.5rem;
        }
        @media (min-width: 640px) { .sm\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
        @media (min-width: 1024px) { .lg\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } .lg\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); } }
        img { max-width: 100%; height: auto; display: block; object-fit: cover; }
        main { padding-top: 10rem; }
        .hidden-on-fail { min-height: 300px; background: #111; border-radius: 1rem; } /* placeholder if img fails */
    </style>
</head>
<body>

    <header class="flex flex-col sm:flex-row justify-between items-center gap-4">
        <a href="#" class="flex items-center gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" class="w-16 h-16 rounded-full border-4 border-[#D4AF37] animate-spin-slow glow-gold">
            <div class="text-3xl font-bold text-[#FFD700]">Neko the Samurai Cat</div>
        </a>
        <nav class="flex gap-4 flex-wrap justify-center">
            <a href="#trade" class="btn-buy">Trade</a>
            <a href="#join" class="btn-buy">Join</a>
            <a href="#lore" class="btn-buy">Lore</a>
            <a href="#art" class="btn-buy">Art</a>
        </nav>
    </header>

    <main class="container">
        <!-- Hero -->
        <section id="hero" class="text-center py-24">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko" class="mx-auto mb-6 rounded-full border-8 border-[#D4AF37] w-64 h-64 animate-spin-slow glow-gold">
            <h1 class="text-6xl font-extrabold section-title mb-4">Zenshin Clan</h1>
            <p class="text-2xl mb-6">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            
            <div class="inline-flex items-center px-6 py-4 rounded-2xl bg-black/70 border border-[#D4AF37] font-mono text-lg shadow-lg max-w-full overflow-hidden">
                <span class="mr-4">CA: 0x28973c4ef9ae754b076a024996350d3b16a38453</span>
                <button onclick="copyCA()" class="bg-[#FFD700] hover:bg-[#F5C842] text-black px-5 py-2 rounded-xl font-bold flex items-center gap-2 transition-all hover:scale-110">
                    📋 Copy
                </button>
            </div>

            <div class="flex flex-col sm:flex-row gap-4 justify-center mt-8">
                <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-lg">Buy on Uniswap</a>
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-lg">Buy on Toshimart</a>
            </div>
        </section>

        <!-- Add back your other sections here with similar inline style classes -->
        <!-- For brevity I kept only hero + header; copy-paste your original sections (trade, chart, join, lore, art, trending, footer) -->
        <!-- Replace Tailwind classes with equivalents like grid grid-cols-1 sm:grid-cols-2 etc. using the style shortcuts above -->

        <footer class="text-center text-gray-400 py-12 border-t border-[#D4AF37]/30 mt-12">
            <p>Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-4">Last Update: {{ last_update }}</p>
        </footer>
    </main>

    <script>
        function copyCA() {
            navigator.clipboard.writeText("0x28973c4ef9ae754b076a024996350d3b16a38453")
                .then(() => alert("CA Copied! ⚔️🐱"));
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

if __name__ == '__main__':
    app.run(debug=True)
