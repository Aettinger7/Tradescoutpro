from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update, current_path='/')

@app.route('/lore')
def lore():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(LORE_TEMPLATE, last_update=last_update, current_path='/lore')

@app.route('/art')
def art():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(ART_TEMPLATE, last_update=last_update, current_path='/art')

application = app

SHARED_HEAD = '''
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko the Samurai Cat - Official Memecoin Site</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        body { 
            margin: 0;
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                        url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed !important;
            background-size: cover !important;
            background-attachment: fixed !important;
            background-color: #0a0a0a !important; 
            color: #ffffff; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
            min-height: 100vh;
        }
        .header { 
            background: linear-gradient(to right, #c8102e, rgba(0,0,0,0.92)); 
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 25px rgba(200, 16, 46, 0.6);
        }
        .logo-text {
            font-family: 'Cinzel', serif;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF4500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 15px rgba(255, 215, 0, 0.7);
        }
        .card { 
            background: rgba(10, 10, 10, 0.88); 
            border: 2px solid #c8102e; 
            border-radius: 1.25rem; 
            box-shadow: 0 10px 35px rgba(200, 16, 46, 0.35);
            transition: all 0.4s ease;
        }
        .card:hover { 
            box-shadow: 0 15px 50px rgba(200, 16, 46, 0.6);
            transform: translateY(-6px);
        }
        .section-title {
            font-family: 'Cinzel', serif;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF4500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(255, 69, 0, 0.6);
        }
        .btn-red {
            background: linear-gradient(135deg, #FF4500, #c8102e);
            color: white;
            padding: 0.75rem 1.25rem;
            border-radius: 9999px;
            font-weight: 700;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(200,16,46,0.5);
            border: 1px solid #FFD70040;
        }
        .btn-red:hover {
            background: linear-gradient(135deg, #FFD700, #FF8C00);
            color: black;
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 8px 25px rgba(255,215,0,0.6);
            border: 1px solid #FFD700;
        }
        .btn-active {
            background: #FFD700;
            color: black;
            padding: 0.75rem 1.25rem;
            border-radius: 9999px;
            font-weight: 700;
            box-shadow: 0 4px 12px rgba(255,215,0,0.5);
            cursor: default;
            border: 1px solid #FFD700;
        }
        @media (min-width: 640px) {
            .btn-red, .btn-active {
                padding: 0.85rem 1.75rem;
                font-size: 1rem;
            }
        }
        .animate-spin-slow { animation: spin 32s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
'''

HEADER_SNIPPET = '''
<header class="header py-5 sm:py-6 px-4 sm:px-6 fixed w-full top-0 z-50">
    <div class="flex justify-between items-center max-w-7xl mx-auto">
        <a href="/" class="flex items-center gap-3 sm:gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-10 h-10 sm:w-14 sm:h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover"/>
            <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-2 sm:gap-4 flex-wrap">
            {% if current_path != '/' %}
                <a href="/" class="btn-red">Home</a>
            {% endif %}
            {% if current_path == '/lore' %}
                <span class="btn-active">Lore</span>
            {% else %}
                <a href="/lore" class="btn-red">Lore</a>
            {% endif %}
            {% if current_path == '/art' %}
                <span class="btn-active">Art</span>
            {% else %}
                <a href="/art" class="btn-red">Art</a>
            {% endif %}
            <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red">Buy on Uniswap</a>
        </div>
    </div>
</header>
'''

HTML_TEMPLATE = SHARED_HEAD + '''
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-5 sm:px-6 lg:px-8 pt-28 sm:pt-32 md:pt-36 pb-20 md:pb-24 max-w-7xl">
        <section class="text-center mb-20 sm:mb-24 md:mb-28">
            <div class="space-y-6 sm:space-y-8 md:space-y-10">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko the Samurai Cat" 
                     class="hero-img mx-auto rounded-full animate-spin-slow border-8 border-yellow-500 w-40 sm:w-48 md:w-64 h-40 sm:h-48 md:h-64"
                     loading="lazy"/>
                <h1 class="text-4xl sm:text-5xl md:text-7xl font-extrabold section-title">Zenshin Clan</h1>
                <p class="text-lg sm:text-xl md:text-2xl">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
                <div class="bg-black/60 inline-block px-6 sm:px-8 py-5 sm:py-6 rounded-xl font-mono text-sm sm:text-base break-all">
                    Now Live on Uniswap • CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
                </div>
                <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('CA Copied!')" 
                        class="mt-4 px-8 sm:px-10 py-4 sm:py-5 bg-gradient-to-r from-yellow-600 to-yellow-700 text-white rounded-full font-bold hover:from-yellow-500 hover:to-yellow-600 text-base sm:text-lg shadow-md hover:shadow-lg transition-all">
                    Copy CA
                </button>
            </div>
        </section>

        <!-- Insert your current sections here (Trade Live, Chart, Join Clan, Top 10 Trending) -->

        <footer class="text-center text-gray-400 py-12 sm:py-16 border-t border-red-800 mt-12 sm:mt-16">
            <p>Now Live on Uniswap (Base) • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-3">Last Update: {{ last_update }}</p>
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

# LORE_TEMPLATE and ART_TEMPLATE use the same SHARED_HEAD + HEADER_SNIPPET + similar container
# Copy the structure from above and paste your content into the <div class="container..."> block

if __name__ == '__main__':
    app.run(debug=True)
