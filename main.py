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

    <!-- Meta tags unchanged -->
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

    <script async src="https://www.googletagmanager.com/gtag/js?id=G-34WMSCBW1R"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-34WMSCBW1R');
    </script>

    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.95)),
                        url('https://i.postimg.cc/1zn9gsLR/image(24).jpg') no-repeat center center fixed;
            background-size: cover;
            color: #ffebcc;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            min-height: 100vh;
        }
        header {
            background: rgba(10,10,15,0.96);
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 25px rgba(212,175,55,0.18);
            position: fixed;
            top: 0; left: 0; right: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(212,175,55,0.25);
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 0 1rem; }
        .flex { display: flex; align-items: center; }
        .flex-col { flex-direction: column; }
        .justify-between { justify-content: space-between; }
        .justify-center { justify-content: center; }
        .gap-4 { gap: 1rem; }
        .gap-6 { gap: 1.5rem; }
        .text-center { text-align: center; }
        .py-12 { padding: 3rem 0; }
        .py-24 { padding: 6rem 0; }
        .pt-28 { padding-top: 7rem; }
        .pt-32 { padding-top: 8rem; }
        .text-xl { font-size: 1.25rem; }
        .text-2xl { font-size: 1.5rem; }
        .text-3xl { font-size: 1.875rem; }
        .text-4xl { font-size: 2.25rem; }
        .text-5xl { font-size: 3rem; }
        .text-6xl { font-size: 3.75rem; }
        .font-bold { font-weight: bold; }
        .font-extrabold { font-weight: 800; }
        .rounded-full { border-radius: 9999px; }
        .border-4 { border: 4px solid; }
        .border-8 { border: 8px solid; }
        .animate-spin-slow { animation: spin 36s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .glow-gold { box-shadow: 0 0 25px rgba(212,175,55,0.7); }
        .section-title {
            font-family: 'Cinzel', serif;
            background: linear-gradient(to right, #FFD700, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(212,175,55,0.5);
        }
        .btn-buy {
            background: linear-gradient(135deg, #D4AF37, #B8860B);
            color: #111;
            padding: 0.75rem 1.5rem;
            border-radius: 9999px;
            font-weight: bold;
            text-decoration: none;
            border: 2px solid #D4AF37;
            box-shadow: 0 4px 12px rgba(212,175,55,0.3);
            transition: all 0.3s ease;
        }
        .btn-buy:hover {
            background: linear-gradient(135deg, #FFD700, #F5C842);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(255,215,0,0.5);
        }
        .card {
            background: rgba(20,20,30,0.9);
            border: 2px solid rgba(212,175,55,0.4);
            border-radius: 1rem;
            padding: 1.5rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5);
            transition: all 0.3s ease;
        }
        .card:hover { transform: translateY(-4px); border-color: #FFD700; box-shadow: 0 12px 32px rgba(212,175,55,0.3); }
        .grid { display: grid; gap: 1.5rem; }
        @media (min-width: 640px) {
            .sm\\:flex-row { flex-direction: row; }
            .sm\\:gap-6 { gap: 1.5rem; }
            .sm\\:grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
            .sm\\:pt-28 { padding-top: 7rem; }
            .sm\\:text-3xl { font-size: 1.875rem; }
        }
        @media (min-width: 768px) {
            .md\\:grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
        }
        @media (min-width: 1024px) {
            .lg\\:grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
            .lg\\:grid-cols-4 { grid-template-columns: repeat(4, 1fr); }
            .lg\\:px-10 { padding-left: 2.5rem; padding-right: 2.5rem; }
        }
        img { max-width: 100%; height: auto; display: block; }
        main { min-height: calc(100vh - 80px); } /* Adjust based on header height ~80px */
    </style>
</head>
<body>

    <header class="py-4 px-4 sm:px-6 flex flex-col sm:flex-row justify-between items-center gap-4">
        <a href="#" class="flex items-center gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" class="w-12 h-12 sm:w-16 sm:h-16 rounded-full border-4 border-[#D4AF37] animate-spin-slow glow-gold">
            <div class="text-xl sm:text-3xl font-bold text-[#FFD700]">Neko the Samurai Cat</div>
        </a>
        <nav class="flex gap-2 sm:gap-6 flex-wrap justify-center">
            <a href="#trade" class="btn-buy text-sm sm:text-base">Trade</a>
            <a href="#join" class="btn-buy text-sm sm:text-base">Join</a>
            <a href="#lore" class="btn-buy text-sm sm:text-base">Lore</a>
            <a href="#art" class="btn-buy text-sm sm:text-base">Art</a>
        </nav>
    </header>

    <main class="pt-32 sm:pt-28 container lg:px-10 max-w-7xl mx-auto">
        <!-- Hero -->
        <section id="hero" class="text-center py-12 sm:py-24">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" class="mx-auto mb-6 rounded-full border-8 border-[#D4AF37] w-40 sm:w-64 md:w-80 animate-spin-slow glow-gold">
            <h1 class="text-4xl sm:text-6xl md:text-8xl font-extrabold section-title mb-4">Zenshin Clan</h1>
            <p class="text-lg sm:text-2xl md:text-3xl mb-6">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            
            <div class="bg-black/70 inline-flex items-center px-6 py-4 rounded-2xl font-mono text-sm sm:text-lg mb-6 shadow-lg border border-[#D4AF37] max-w-full overflow-hidden mx-auto">
                <span class="mr-4">CA: 0x28973c4ef9ae754b076a024996350d3b16a38453</span>
                <button onclick="copyCA()" class="bg-[#FFD700] hover:bg-[#F5C842] text-black px-5 py-2 rounded-xl font-bold flex items-center gap-2 transition-all hover:scale-110">
                    📋 Copy
                </button>
            </div>

            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-base sm:text-lg">Buy on Uniswap</a>
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-base sm:text-lg">Buy on Toshimart</a>
            </div>
        </section>

        <!-- Paste your other sections here (trade, chart, join, lore, art, trending) from original code -->
        <!-- Use .grid, .card, .btn-buy etc. as defined above -->

        <footer class="text-center text-gray-400 py-8 sm:py-12 border-t border-[#D4AF37]/30 mt-8 sm:mt-12">
            <p class="text-sm sm:text-base">Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-3 sm:mt-4 text-sm">Last Update: {{ last_update }}</p>
        </footer>
    </main>

    <script>
        function copyCA() {
            navigator.clipboard.writeText("0x28973c4ef9ae754b076a024996350d3b16a38453").then(() => {
                alert("CA Copied! ⚔️🐱");
            });
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
