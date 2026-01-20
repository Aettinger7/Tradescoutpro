from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

@app.route('/art')
def art():
    art_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Neko Art Gallery - Zenshin Clan</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
        <style>
            body {
                margin: 0;
                background: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), 
                            url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed;
                background-size: cover;
                background-attachment: fixed;
                color: white;
                min-height: 100vh;
                font-family: 'Helvetica Neue', Arial, sans-serif;
            }
            .gallery-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1.5rem;
                max-width: 1400px;
                margin: 0 auto;
                padding: 2rem 1rem;
            }
            .art-card {
                background: rgba(0,0,0,0.6);
                border: 2px solid #FF0000;
                border-radius: 1rem;
                overflow: hidden;
                box-shadow: 0 8px 32px rgba(255,0,0,0.3);
                transition: all 0.3s;
            }
            .art-card:hover {
                transform: scale(1.03);
                box-shadow: 0 12px 48px rgba(255,215,0,0.5);
            }
            .art-img {
                width: 100%;
                height: auto;
                display: block;
            }
        </style>
    </head>
    <body>
        <header class="bg-gradient-to-r from-red-900 to-black backdrop-blur-md py-4 px-6 flex justify-between items-center fixed w-full top-0 z-50 shadow-lg">
            <a href="/" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full overflow-hidden border-4 border-yellow-500 flex-shrink-0">
                    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                         alt="Neko Logo" 
                         class="w-full h-full object-cover">
                </div>
                <span class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">Neko the Samurai Cat</span>
            </a>
            <div class="flex items-center gap-4">
                <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" 
                   target="_blank" 
                   class="bg-red-600 hover:bg-yellow-500 text-white hover:text-black px-5 py-2.5 rounded-full font-bold transition-all duration-300 shadow-md">
                    Buy $NEKO Now
                </a>
                <a href="/" 
                   class="bg-red-600 hover:bg-yellow-500 text-white hover:text-black px-5 py-2.5 rounded-full font-bold transition-all duration-300 shadow-md">
                    Back to Home
                </a>
            </div>
        </header>

        <main class="pt-24">
            <h1 class="text-4xl md:text-6xl font-extrabold text-center my-12 text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">
                Neko Art Gallery
            </h1>
            <div class="gallery-grid">
                <div class="art-card">
                    <img src="https://i.ibb.co/HTDz0zgc/Neko-art-1.jpg" alt="Neko Samurai Art 1" class="art-img">
                </div>
                <div class="art-card">
                    <img src="https://i.ibb.co/jZV1HGs9/Neko-art-2.jpg" alt="Neko Samurai Art 2" class="art-img">
                </div>
                <div class="art-card">
                    <img src="https://i.ibb.co/rGvcbx3h/Neko-art-3.jpg" alt="Neko Samurai Art 3" class="art-img">
                </div>
                <div class="art-card">
                    <img src="https://i.ibb.co/23mD7cZC/Neko-art-4.jpg" alt="Neko Samurai Art 4" class="art-img">
                </div>
            </div>
            <p class="text-center text-gray-400 mt-12 mb-8 text-lg">
                More epic Neko artwork coming soon • Follow @NekoTheSamurai for updates
            </p>
        </main>
    </body>
    </html>
    '''
    return art_html

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
        html, body { margin: 0; overflow-x: hidden; min-height: 100vh; }
        body { 
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                        url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed;
            background-size: cover;
            background-attachment: fixed;
            background-color: #111111;
            color: #ffffff;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }
        .header { 
            background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.9)); 
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(255, 0, 0, 0.5);
        }
        .logo-container {
            width: 2.5rem;
            height: 2.5rem;
            border-radius: 9999px;
            overflow: hidden;
            border: 3px solid #FFD700;
            flex-shrink: 0;
        }
        .logo-img { width: 100%; height: 100%; object-fit: cover; }
        .btn { 
            background: #FF0000;
            color: white;
            padding: 0.5rem 1.25rem;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.3s;
            text-decoration: none;
            font-size: 0.875rem;
        }
        .btn:hover { 
            background: #FFD700;
            color: black;
            transform: scale(1.05);
        }
        .section-title {
            font-family: 'Cinzel', serif;
            font-size: 2.5rem;
            font-weight: 900;
            background: linear-gradient(to right, #FFD700, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        @media (min-width: 640px) {
            .btn { font-size: 1rem; padding: 0.625rem 1.5rem; }
            .logo-container { width: 3.5rem; height: 3.5rem; }
        }
    </style>
</head>
<body>
    <header class="header py-3 px-4 sm:py-4 sm:px-6 flex justify-between items-center fixed w-full top-0 z-50">
        <a href="/" class="flex items-center gap-3">
            <div class="logo-container">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko Logo" 
                     class="logo-img animate-spin-slow">
            </div>
            <div class="text-xl sm:text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">
                Neko the Samurai Cat
            </div>
        </a>
        <div class="flex items-center gap-3 sm:gap-4">
            <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" 
               target="_blank" 
               class="btn">Buy $NEKO Now</a>
            <a href="/art" 
               class="btn">Art</a>
        </div>
    </header>

    <div class="container mx-auto px-4 sm:px-6 pt-20 sm:pt-24 pb-20 max-w-7xl">
        <section class="text-center mb-16">
            <div class="w-32 h-32 sm:w-48 sm:h-48 mx-auto mb-8 rounded-full overflow-hidden border-8 border-yellow-500 animate-spin-slow">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" 
                     alt="Neko Hero" 
                     class="w-full h-full object-cover">
            </div>
            <h1 class="text-5xl sm:text-7xl font-extrabold mb-6 section-title">Zenshin Clan</h1>
            <p class="text-xl sm:text-2xl mb-8">"Forward Progress" – Warrior in a garden, claws sharpened on Base.</p>
            <div class="bg-black/60 inline-block px-6 py-4 rounded-xl mb-6 font-mono text-lg">
                CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
            </div>
            <br>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('Copied!')" 
                    class="mt-4 px-8 py-4 bg-yellow-600 text-black rounded-full font-bold hover:bg-yellow-500">
                Copy CA
            </button>
        </section>

        <!-- Add your other sections here (Live on Toshimart, Chart, Join Clan, Recent Updates, Footer) -->
        <!-- You can copy them from your previous working version -->

        <footer class="text-center text-gray-400 py-10 border-t border-red-800 mt-16">
            <p>Powered by Toshimart on Base • DYOR – Not financial advice • © 2026 Neko on Base</p>
            <p class="mt-2">Last Update: {{ last_update }}</p>
        </footer>
    </div>

    <script>
        window.addEventListener('load', function() {
            setTimeout(() => window.scrollTo({ top: 0, left: 0, behavior: 'instant' }), 100);
        });
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
