from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# Define shared parts FIRST
SHARED_HEAD = '''
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko the Samurai Cat</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
                        url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed;
            background-size: cover;
            background-attachment: fixed;
            background-color: #0a0a0a;
            color: #ffffff;
            font-family: Arial, sans-serif;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(to right, #c8102e, #000);
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(200,16,46,0.5);
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 50;
        }
        .logo-text {
            font-family: 'Cinzel', serif;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF4500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .btn-red {
            background: #c8102e;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.3s;
        }
        .btn-red:hover {
            background: #FFD700;
            color: black;
            transform: scale(1.05);
        }
    </style>
</head>
'''

HEADER_SNIPPET = '''
<header class="header py-4 px-4 sm:py-6 sm:px-8 flex justify-between items-center">
    <a href="/" class="flex items-center gap-3">
        <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
             alt="Neko Logo" 
             class="w-10 h-10 sm:w-14 sm:h-14 rounded-full border-4 border-yellow-500">
        <div class="logo-text text-xl sm:text-3xl">Neko the Samurai Cat</div>
    </a>
    <div class="flex gap-3 flex-wrap">
        <a href="/lore" class="btn-red">Lore</a>
        <a href="/art" class="btn-red">Art</a>
        <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-red">Buy on Uniswap</a>
    </div>
</header>
'''

HTML_TEMPLATE = SHARED_HEAD + '''
<body>
    ''' + HEADER_SNIPPET + '''
    <div class="pt-20 p-4 max-w-7xl mx-auto">
        <section class="text-center mb-12">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                 alt="Neko" 
                 class="w-48 h-48 sm:w-64 sm:h-64 mx-auto mb-6 rounded-full border-8 border-yellow-500">
            <h1 class="text-5xl sm:text-7xl font-bold mb-4">Zenshin Clan</h1>
            <p class="text-xl sm:text-2xl mb-6">"Forward Progress" – Warrior in a garden</p>
            <div class="bg-black/60 p-4 rounded-xl inline-block font-mono text-sm sm:text-base mb-6">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <br>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('Copied!')" 
                    class="bg-yellow-600 text-black px-8 py-4 rounded-full font-bold hover:bg-yellow-500">
                Copy CA
            </button>
        </section>

        <section class="mb-12">
            <h2 class="text-4xl font-bold mb-6 text-center">Lore</h2>
            <div class="bg-black/80 p-8 rounded-2xl">
                <p class="text-lg mb-4">Neko is the silent guardian: soft paws, sharp steel. Born under cherry blossoms, forged in shadow. Walks the path of Zenshin – forward progress without haste, honor without pride.</p>
                <p class="text-lg mb-4">"I am the storm." Daily wisdom: enjoy slow mornings, sharpen the blade in silence, protect the light.</p>
                <p class="text-lg">Join the clan. Zenshin.</p>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-4xl font-bold mb-6 text-center">Art Gallery</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Portrait" class="rounded-xl shadow-2xl">
                <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Blossoms" class="rounded-xl shadow-2xl">
                <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Clan Art" class="rounded-xl shadow-2xl">
            </div>
        </section>

        <footer class="text-center text-gray-400 py-10 border-t border-red-800">
            <p>© 2026 Neko on Base • DYOR</p>
            <p>Last Update: {{ last_update }}</p>
        </footer>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
