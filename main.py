from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update, current_path='/')

@app.route('/whitepaper')
def whitepaper():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(WHITEPAPER_TEMPLATE, last_update=last_update, current_path='/whitepaper')

@app.route('/lore')
def lore():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(LORE_TEMPLATE, last_update=last_update, current_path='/lore')

@app.route('/art')
def art():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(ART_TEMPLATE, last_update=last_update, current_path='/art')

application = app

# Shared header snippet for consistency
HEADER_SNIPPET = '''
<header class="header py-5 sm:py-6 px-4 sm:px-6 fixed w-full top-0 z-50">
    <div class="flex justify-between items-center max-w-7xl mx-auto">
        <a href="/" class="flex items-center gap-3 sm:gap-4">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko Logo" 
                 class="w-10 h-10 sm:w-14 sm:h-14 rounded-full animate-spin-slow border-4 border-yellow-500 object-cover"
                 onerror="this.src='https://via.placeholder.com/56/FFD700/000?text=Neko';">
            <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-2 sm:gap-4 flex-wrap">
            {% if current_path != '/' %}
                <a href="/" class="btn-red text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Home</a>
            {% endif %}
            {% if current_path == '/whitepaper' %}
                <span class="btn-active text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Whitepaper</span>
            {% else %}
                <a href="/whitepaper" class="btn-red text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Whitepaper</a>
            {% endif %}
            {% if current_path == '/lore' %}
                <span class="btn-active text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Lore</span>
            {% else %}
                <a href="/lore" class="btn-red text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Lore</a>
            {% endif %}
            {% if current_path == '/art' %}
                <span class="btn-active text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Art</span>
            {% else %}
                <a href="/art" class="btn-red text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Art</a>
            {% endif %}
            <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red text-xs sm:text-sm md:text-base px-3 sm:px-4 md:px-5 py-2">Buy on Uniswap</a>
        </div>
    </div>
</header>
'''

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
        body { margin: 0; background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed; background-size: cover; background-attachment: fixed; background-color: #111111; color: #ffffff; font-family: 'Helvetica Neue', Arial, sans-serif; min-height: 100vh; }
        .header { background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.9)); backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(255, 0, 0, 0.5); }
        .logo-text { font-family: 'Cinzel', serif; font-weight: 900; background: linear-gradient(to right, #FFD700, #FF0000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 20px rgba(255, 215, 0, 0.8); }
        .card { background: rgba(0, 0, 0, 0.85); border: 2px solid #FF0000; border-radius: 1rem; box-shadow: 0 8px 32px rgba(255, 0, 0, 0.4); transition: all 0.3s; }
        .card:hover { box-shadow: 0 0 40px rgba(255, 0, 0, 0.7); transform: translateY(-4px); }
        .section-title { font-family: 'Cinzel', serif; font-weight: 900; background: linear-gradient(to right, #FFD700, #FF0000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 25px rgba(255, 215, 0, 0.7); }
        .btn-red { background: #FF0000; color: white; padding: 10px 20px; border-radius: 9999px; font-weight: bold; text-decoration: none; transition: all 0.3s; white-space: nowrap; }
        .btn-red:hover { background: #FFD700; color: black; transform: scale(1.05); }
        .btn-active { background: #FF0000; color: white; padding: 10px 20px; border-radius: 9999px; font-weight: bold; opacity: 0.8; cursor: default; }
        .animate-spin-slow { animation: spin 30s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .hero-img { object-fit: cover; filter: drop-shadow(0 0 25px rgba(255,215,0,0.6)); aspect-ratio: 1 / 1; }
        iframe { border: none; width: 100%; height: 500px; }
    </style>
</head>
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-5 sm:px-6 lg:px-8 pt-32 sm:pt-36 md:pt-40 pb-20 md:pb-24 max-w-7xl">
        <!-- Hero and other sections remain as in your last working version - hero, trade cards, chart, join clan, top 10 trending -->
        <!-- Paste your full main content here from the previous complete homepage template -->
        <section class="text-center mb-24 sm:mb-28 md:mb-32">
            <!-- ... hero content ... -->
        </section>
        <!-- ... rest of sections: trade, chart, join, trending ... -->
    </div>
</body>
</html>
'''

# WHITEPAPER_TEMPLATE, LORE_TEMPLATE, ART_TEMPLATE would use the same HEADER_SNIPPET and similar container styles
# For brevity, add this pattern to them:
# <body>
#     ''' + HEADER_SNIPPET + '''
#     <div class="container ...">
#         <!-- page content -->
#     </div>
# </body>

LORE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- same head as main -->
</head>
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-5 sm:px-6 lg:px-8 pt-32 sm:pt-36 md:pt-40 pb-20 md:pb-24 max-w-5xl">
        <section class="text-center mb-12">
            <h1 class="section-title text-5xl sm:text-7xl mb-6">Neko Lore</h1>
            <p class="text-xl text-gray-300">The Way of the Samurai Cat</p>
        </section>
        <div class="card p-8 sm:p-12">
            <p class="text-lg leading-relaxed mb-6">Neko is the silent guardian of the village: soft paws tread quietly in the dawn mist, yet claws are always ready to defend the light. Born under cherry blossoms and forged in shadow, Neko walks the path of Zenshin—forward progress without haste, honor without pride.</p>
            <p class="text-lg leading-relaxed mb-6">"Fate whispers, 'You cannot withstand the storm.' Neko whispers back, 'I am the storm.'" Daily meditations remind the clan: enjoy slow mornings, sharpen the blade in silence, protect what is precious.</p>
            <p class="text-lg leading-relaxed">Join the Zenshin Clan. Forward progress awaits.</p>
        </div>
        <div class="text-center mt-12">
            <a href="/" class="btn-red text-xl px-12 py-6 inline-block">Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

ART_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- same head -->
</head>
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="container mx-auto px-5 sm:px-6 lg:px-8 pt-32 sm:pt-36 md:pt-40 pb-20 md:pb-24 max-w-5xl">
        <section class="text-center mb-12">
            <h1 class="section-title text-5xl sm:text-7xl mb-6">Neko Art Gallery</h1>
            <p class="text-xl text-gray-300">Samurai Cat Visions</p>
        </section>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Add your image URLs here -->
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" class="rounded-xl shadow-2xl">
            <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" class="rounded-xl shadow-2xl">
            <!-- Add more Gemini or custom art URLs -->
            <!-- Placeholder for future gallery -->
            <div class="card p-8 text-center flex items-center justify-center h-64">
                <p class="text-gray-400">More art coming soon – Zenshin!</p>
            </div>
        </div>
        <div class="text-center mt-12">
            <a href="/" class="btn-red text-xl px-12 py-6 inline-block">Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
