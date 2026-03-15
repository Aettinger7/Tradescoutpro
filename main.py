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

    <!-- Basic SEO meta description -->
    <meta name="description" content="Neko the Samurai Cat ($NEKO) – Zenshin Clan meme token on Base. Forward progress with honor. Trade on Uniswap. Join the clan!">

    <!-- Open Graph / Social Sharing Meta Tags -->
    <meta property="og:title" content="Neko the Samurai Cat ⚔️🐱 $NEKO on Base">
    <meta property="og:description" content="Zenshin Clan – 'Forward Progress'. Warrior in a garden, claws sharpened on Base. Join the samurai cat revolution. CA: 0x28973c4ef9ae754b076a024996350d3b16a38453">
    <meta property="og:image" content="https://i.ibb.co/6cpdFyYv/image-24.jpg">
    <meta property="og:url" content="https://www.nekothesamurai.com">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Neko the Samurai">

    <!-- Twitter / X Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Neko the Samurai Cat ⚔️🐱 $NEKO">
    <meta name="twitter:description" content='"Forward Progress" – Join the Zenshin Clan on Base. Samurai cat meme token. Buy on Uniswap / Toshimart.'>
    <meta name="twitter:image" content="https://i.ibb.co/6cpdFyYv/image-24.jpg">
    <meta name="twitter:site" content="@NekoTheSamurai">

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-34WMSCBW1R"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-34WMSCBW1R');
    </script>

    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            background: 
                linear-gradient(rgba(0, 0, 0, 0.92), rgba(0, 0, 0, 0.95)),
                url('https://i.postimg.cc/1zn9gsLR/image(24).jpg') no-repeat center center fixed;
            background-size: cover;
            color: #f5f5f5;
            font-family: Arial, sans-serif;
            scroll-behavior: smooth;
            overflow-x: hidden;
            min-height: calc(100vh);          /* ← changed here */
        }
        .header {
            background: rgba(10, 10, 15, 0.96);
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 25px rgba(212, 175, 55, 0.18);
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            border-bottom: 1px solid rgba(212, 175, 55, 0.25);
        }
        .btn-buy {
            background: linear-gradient(135deg, #D4AF37, #B8860B);
            color: #0f0f0f;
            padding: 0.7rem 1.4rem;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.35s ease;
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
            border: 2px solid #D4AF37;
            white-space: nowrap;
        }
        .btn-buy:hover {
            background: linear-gradient(135deg, #FFD700, #F5C842);
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 12px 40px rgba(255, 215, 0, 0.6);
            border: 2px solid #FFD700;
        }
        .section-title {
            font-family: 'Cinzel', serif;
            background: linear-gradient(to right, #FFD700, #D4AF37, #B8860B);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 25px rgba(212, 175, 55, 0.6);
        }
        .card {
            background: rgba(15, 15, 25, 0.92);
            border: 2px solid rgba(212, 175, 55, 0.5);
            border-radius: 1.25rem;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
            transition: all 0.4s ease;
            width: 100%;
        }
        .card:hover {
            box-shadow: 0 15px 50px rgba(212, 175, 55, 0.35);
            transform: translateY(-6px);
            border-color: #FFD700;
        }
        .animate-spin-slow {
            animation: spin 36s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .glow-gold {
            box-shadow: 0 0 25px rgba(212, 175, 55, 0.7);
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
        }
        #art .card:hover img {
            transform: scale(1.08);
            transition: transform 0.5s ease;
        }
        .toast {
            animation: popIn 0.4s ease forwards;
            background: #1a1a2e;
            border: 2px solid #D4AF37;
            color: #FFD700;
        }
        @keyframes popIn {
            from { transform: translate(-50%, 30px); opacity: 0; }
            to { transform: translate(-50%, 0); opacity: 1; }
        }
        @media (max-width: 640px) {
            body {
                background-attachment: scroll;
                background-position: center top;
            }
            main {
                padding-top: 120px;
            }
            .header {
                padding: 1rem;
            }
            .btn-buy {
                padding: 0.6rem 1.2rem;
                font-size: 0.9rem;
            }
        }
        @media (min-width: 1024px) {
            #art .grid {
                gap: 2.5rem;
            }
        }
    </style>
</head>
<body>
    <header class="header py-4 px-4 sm:px-6 flex flex-col sm:flex-row justify-between items-center gap-4">
        <a href="#" class="flex items-center gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-12 h-12 sm:w-16 sm:h-16 rounded-full border-4 border-[#D4AF37] animate-spin-slow glow-gold">
            <div class="logo-text text-xl sm:text-3xl font-bold text-[#FFD700]">Neko the Samurai Cat</div>
        </a>
        <nav class="flex gap-2 sm:gap-6 flex-wrap justify-center">
            <a href="#trade" class="btn-buy text-sm sm:text-base">Trade</a>
            <a href="#join" class="btn-buy text-sm sm:text-base">Join</a>
            <a href="#lore" class="btn-buy text-sm sm:text-base">Lore</a>
            <a href="#art" class="btn-buy text-sm sm:text-base">Art</a>
        </nav>
    </header>

    <main class="pt-32 sm:pt-28 px-4 sm:px-6 lg:px-10 max-w-7xl mx-auto">
        <!-- Hero -->
        <section id="hero" class="text-center py-12 sm:py-24">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko the Samurai Cat" 
                 class="mx-auto mb-6 rounded-full border-8 border-[#D4AF37] w-40 sm:w-64 md:w-80 h-40 sm:h-64 md:h-80 animate-spin-slow glow-gold max-w-full">
            <h1 class="text-4xl sm:text-6xl md:text-8xl font-extrabold section-title mb-4">Zenshin Clan</h1>
            <p class="text-lg sm:text-2xl md:text-3xl mb-6 text-[#e0d4b5]">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            
            <div class="bg-black/70 inline-flex items-center px-6 py-4 rounded-2xl font-mono text-sm sm:text-lg mb-6 shadow-lg border border-[#D4AF37] max-w-full overflow-hidden">
                <span class="mr-4">CA: 0x28973c4ef9ae754b076a024996350d3b16a38453</span>
                <button onclick="copyCA()" 
                        class="bg-[#FFD700] hover:bg-[#F5C842] text-black px-5 py-2 rounded-xl font-bold flex items-center gap-2 transition-all hover:scale-110">
                    📋 Copy
                </button>
            </div>

            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-base sm:text-lg">Buy on Uniswap</a>
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-buy text-base sm:text-lg">Buy on Toshimart</a>
            </div>
        </section>

        <!-- The rest of your sections remain the same -->
        <!-- Trade, Chart, Join, Lore, Art, Trending, Footer... -->

        <!-- (I omitted them here to save space, but keep all your original sections below this point) -->

        <footer class="text-center text-gray-400 py-8 sm:py-12 border-t border-[#D4AF37]/30 mt-8 sm:mt-12">
            <p class="text-sm sm:text-base">Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-3 sm:mt-4 text-sm">Last Update: {{ last_update }}</p>
        </footer>
    </main>

    <!-- Copy CA Script -->
    <script>
        function copyCA() {
            const ca = "0x28973c4ef9ae754b076a024996350d3b16a38453";
            navigator.clipboard.writeText(ca).then(() => {
                showToast("CA Copied! ⚔️🐱 Ready to join the Zenshin Clan!");
            });
        }

        function showToast(message) {
            const toast = document.createElement("div");
            toast.className = "toast fixed bottom-6 left-1/2 -translate-x-1/2 bg-emerald-900 text-[#FFD700] px-8 py-4 rounded-3xl shadow-2xl flex items-center gap-3 text-base font-semibold z-[9999] border border-[#D4AF37]";
            toast.innerHTML = `✅ ${message}`;
            document.body.appendChild(toast);

            setTimeout(() => {
                toast.style.transition = "all 0.4s ease";
                toast.style.opacity = "0";
                toast.style.transform = "translate(-50%, 30px)";
                setTimeout(() => toast.remove(), 500);
            }, 2800);
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
