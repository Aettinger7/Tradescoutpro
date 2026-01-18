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
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko the Samurai Cat - Official Memecoin Site</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        body { 
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://pbs.twimg.com/media/G-9Z6XQXMAA7ln4.jpg') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #000000; 
            color: #ffffff; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
        }
        .hero-bg {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://pbs.twimg.com/media/G-9XeOXWQAACCmG.jpg') no-repeat center/cover;
        }
        .light body { 
            background: linear-gradient(rgba(255,255,255,0.3), rgba(255,255,255,0.3)), url('https://pbs.twimg.com/media/G-9Z6XQXMAA7ln4.jpg') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #f8fafc; 
            color: #000000; 
        }
        .header { 
            background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.8)); 
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(255, 0, 0, 0.4);
        }
        .light .header { 
            background: linear-gradient(to right, #FF0000, rgba(255,255,255,0.8)); 
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
        .metric-card { 
            background: rgba(0, 0, 0, 0.8); 
            border: 2px solid #FF0000; 
            border-radius: 1rem; 
            box-shadow: 0 8px 32px rgba(255, 0, 0, 0.3);
            transition: all 0.4s;
        }
        .metric-card:hover { 
            box-shadow: 0 0 35px rgba(255, 0, 0, 0.6);
        }
        .light .metric-card { 
            background: rgba(255,255,255,0.9); 
            border: 2px solid #FF0000; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        .progress-bar { 
            height: 10px; 
            border-radius: 9999px; 
            background: #1a1a1a; 
            overflow: hidden;
        }
        .light .progress-bar { 
            background: #e2e8f0; 
        }
        .progress-fill { 
            height: 100%; 
            border-radius: 9999px; 
            background: linear-gradient(to right, #FFD700, #FF0000);
            transition: width 2s ease-in-out;
        }
        .lore-card, .community-card { 
            background: rgba(0, 0, 0, 0.85); 
            border: 2px solid #FF0000; 
            border-radius: 1rem; 
            transition: all 0.4s;
            box-shadow: 0 8px 32px rgba(255, 0, 0, 0.2);
            padding: 1.5rem; 
        }
        .lore-card:hover, .community-card:hover { 
            box-shadow: 0 0 40px rgba(255, 0, 0, 0.5);
            transform: translateY(-5px);
        }
        .light .lore-card, .light .community-card { 
            background: rgba(255,255,255,0.85); 
            border: 2px solid #FF0000; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        }
        .section-title {
            font-family: 'Cinzel', serif;
            font-size: 3.5rem;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
        }
        .animate-spin-slow { animation: spin 30s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .hero-img { filter: drop-shadow(0 0 20px rgba(255,215,0,0.5)); }
    </style>
</head>
<body class="transition-all duration-500">
    <header class="header py-6 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://pbs.twimg.com/profile_images/2011108570171834368/79u2WeSG.jpg" alt="Neko Logo" class="w-12 h-12 rounded-full animate-spin-slow border-2 border-gold-500">
            <div class="logo-text">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-4">
            <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="px-6 py-3 rounded-full bg-red-600 hover:bg-red-700 text-white font-bold text-base shadow-lg">Buy $NEKO Now</a>
            <button id="toggle-theme" class="px-5 py-2 rounded-full bg-black/50 hover:bg-black/70 light:bg-white/50 light:hover:bg-white/70 flex items-center gap-2 font-bold text-sm text-white light:text-black border border-red-600 shadow-lg">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <section class="hero-bg text-center py-20 rounded-2xl mb-16 shadow-2xl">
            <img src="https://pbs.twimg.com/media/G-9XeOXWQAACCmG.jpg" alt="Neko in Battle" class="w-64 h-64 mx-auto mb-6 rounded-full hero-img border-4 border-gold-500">
            <h1 class="text-6xl font-extrabold mb-6 section-title">Zenshin Clan: Forward Progress</h1>
            <p class="text-xl mb-8 max-w-2xl mx-auto">"It is better to be a warrior in a garden than a gardener in a war." – Neko leads with courage on Base.</p>
            <p class="text-lg mb-6 font-mono bg-black/50 inline-block px-6 py-3 rounded-lg">CA: 0x28973c4ef9ae754b076a024996350d3b16a38453</p>
            <br>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('CA Copied!')" class="px-6 py-3 bg-gold-600 text-black rounded-full font-bold hover:bg-gold-500">Copy CA</button>
        </section>

        <!-- Token Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-8 mb-20">
            <div class="metric-card p-6 text-center">
                <img src="https://pbs.twimg.com/media/G-9d_siWwAACEEY.jpg" alt="Neko Claws" class="w-12 h-12 mx-auto mb-3 rounded-full animate-spin-slow">
                <p class="text-red-300 light:text-red-700 text-sm mb-2 font-semibold">Price (USD)</p>
                <p id="neko-price" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="price-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <!-- Repeat similar for other metrics, using different images like G-9Z6XQXMAA7ln4.jpg, G-jrFGLbQAMHOk0.jpg etc. -->
            <div class="metric-card p-6 text-center">
                <img src="https://pbs.twimg.com/media/G-9Z6XQXMAA7ln4.jpg" alt="Neko Zen" class="w-12 h-12 mx-auto mb-3 rounded-full animate-spin-slow">
                <p class="text-red-300 light:text-red-700 text-sm mb-2 font-semibold">Market Cap</p>
                <p id="neko-mc" class="text-3xl font-extrabold mb-4 text-white light:text-black">–</p>
                <div class="progress-bar"><div id="mc-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <!-- ... add the rest similarly ... -->
        </div>

        <!-- Rest of the sections (chart, lore, community, X timeline) remain similar to previous version -->

        <footer class="mt-20 text-center text-sm text-gray-400">
            <p>Powered by Toshimart on Base | DYOR - Not Financial Advice | Last Update: {{ last_update }}</p>
        </footer>
    </div>

    <!-- Keep the JS from previous version for theme, metrics fetch, lore display -->
    <script>
        // ... (paste the full <script> block from the previous code here, including loadNekoMetrics, displayLore, theme toggle) ...
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)

