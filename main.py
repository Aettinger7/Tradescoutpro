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
            background: url('https://img.freepik.com/premium-photo/cyberpunk-samurai-japanese-garden-cherry-blossoms-glowing-neon-lights-combining-ancient-aesthetics-with-futuristic-elements_486608-6092.jpg') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #000000; 
            color: #ffffff; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
        }
        .light body { 
            background: url('https://img.freepik.com/premium-photo/cyberpunk-samurai-japanese-garden-cherry-blossoms-glowing-neon-lights-combining-ancient-aesthetics-with-futuristic-elements_486608-6092.jpg') no-repeat center center fixed; 
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
        .animate-spin-slow { animation: spin 20s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="transition-all duration-500">
    <header class="header py-6 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://thumbs.dreamstime.com/z/cute-samurai-cat-against-backdrop-blooming-sakura-watercolor-illustration-childrens-book-adorable-character-blossoms-kids-337508330.jpg" alt="Neko Logo" class="w-10 h-10 rounded-full animate-spin-slow">
            <div class="logo-text">Neko the Samurai Cat</div>
        </a>
        <div class="flex items-center gap-4">
            <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="px-5 py-2 rounded-full bg-red-600 hover:bg-red-700 text-white font-bold text-sm shadow-lg">Buy $NEKO</a>
            <button id="toggle-theme" class="px-5 py-2 rounded-full bg-black/50 hover:bg-black/70 light:bg-white/50 light:hover:bg-white/70 flex items-center gap-2 font-bold text-sm text-white light:text-black border border-red-600 shadow-lg">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <h1 class="text-5xl font-extrabold mb-16 text-center section-title">Zenshin Clan: Forward Progress</h1>

        <!-- Hero Section -->
        <div class="text-center mb-20">
            <img src="https://thumbs.dreamstime.com/z/cute-samurai-cat-against-backdrop-blooming-sakura-watercolor-illustration-childrens-book-adorable-character-blossoms-kids-337508330.jpg" alt="Neko Hero" class="w-48 h-48 mx-auto mb-6 rounded-full shadow-lg">
            <p class="text-xl mb-4">Contract Address (Base): 0x28973c4ef9ae754b076a024996350d3b16a38453</p>
            <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453')" class="px-4 py-2 bg-gold-600 text-black rounded-full font-bold">Copy CA</button>
        </div>

        <!-- Token Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-8 mb-20">
            <div class="metric-card p-6 text-center">
                <img src="https://thumbs.dreamstime.com/z/cute-samurai-cat-against-backdrop-blooming-sakura-watercolor-illustration-childrens-book-adorable-character-blossoms-kids-337508330.jpg" alt="Price Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-red-300 light:text-red-700 text-sm mb-2 font-semibold">Price (USD)</p>
                <p id="neko-price" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="price-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://thumbs.dreamstime.com/z/cute-samurai-cat-against-backdrop-blooming-sakura-watercolor-illustration-childrens-book-adorable-character-blossoms-kids-337508330.jpg" alt="MC Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-red-300 light:text-red-700 text-sm mb-2 font-semibold">Market Cap</p>
                <p id="neko-mc" class="text-3xl font-extrabold mb-4 text-white light:text-black">–</p>
                <div class="progress-bar"><div id="mc-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://thumbs.dreamstime.com/z/cute-samurai-cat-against-backdrop-blooming-sakura-watercolor-illustration-childrens-book-adorable-character-blossoms-kids-337508330.jpg" alt="Liq Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-red-300 light:text-red-700 text-sm mb-2 font-semibold">Liquidity</p>
                <p id="neko-liq" class="text-3xl font-extrabold mb-4 text-white light:text-black">–</p>
                <div class="progress-bar"><div id="liq-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://thumbs.dreamstime.com/z/cute-samurai-cat-against-backdrop-blooming-sakura-watercolor-illustration-childrens-book-adorable-character-blossoms-kids-337508330.jpg" alt="Vol Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-red-300 light:text-red-700 text-sm mb-2 font-semibold">24h Volume</p>
                <p id="neko-vol" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="vol-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://thumbs.dreamstime.com/z/cute-samurai-cat-against-backdrop-blooming-sakura-watercolor-illustration-childrens-book-adorable-character-blossoms-kids-337508330.jpg" alt="Holders Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-red-300 light:text-red-700 text-sm mb-2 font-semibold">Holders</p>
                <p id="neko-holders" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="holders-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
        </div>

        <!-- Chart -->
        <div class="mb-20">
            <h2 class="text-4xl font-extrabold mb-10 section-title text-center">$NEKO Chart</h2>
            <iframe src="https://dexscreener.com/base/0x28973c4ef9ae754b076a024996350d3b16a38453?embed=1&theme=dark&info=0" width="100%" height="400" frameborder="0"></iframe>
        </div>

        <!-- Lore & Community -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
            <div class="lg:col-span-2">
                <h2 class="text-4xl font-extrabold mb-10 section-title">Neko Lore & Quotes</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div id="lore-feed"></div>
                </div>
            </div>
            <div>
                <h2 class="text-4xl font-extrabold mb-10 section-title">Join the Clan</h2>
                <div class="grid grid-cols-1 gap-8">
                    <div class="community-card">
                        <p class="text-gold-300 text-lg font-bold mb-2">X (Twitter)</p>
                        <a href="https://x.com/NekoTheSamurai" target="_blank" class="text-white light:text-black text-sm mb-3 block">Follow @NekoTheSamurai</a>
                    </div>
                    <div class="community-card">
                        <p class="text-gold-300 text-lg font-bold mb-2">Telegram</p>
                        <a href="https://t.me/toshimart" target="_blank" class="text-white light:text-black text-sm mb-3 block">Toshimart TG</a>
                    </div>
                    <div class="community-card">
                        <p class="text-gold-300 text-lg font-bold mb-2">Discord</p>
                        <a href="https://discord.com/invite/toshibase" target="_blank" class="text-white light:text-black text-sm mb-3 block">Toshi Base Discord</a>
                    </div>
                    <div class="community-card">
                        <p class="text-gold-300 text-lg font-bold mb-2">Warpcast</p>
                        <a href="https://warpcast.com/toshibase" target="_blank" class="text-white light:text-black text-sm mb-3 block">Toshi Base Warpcast</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- X Timeline -->
        <div class="mt-20">
            <h2 class="text-4xl font-extrabold mb-10 section-title text-center">Recent Clan Updates</h2>
            <a class="twitter-timeline" data-theme="dark" href="https://twitter.com/NekoTheSamurai?ref_src=twsrc%5Etfw">Tweets by NekoTheSamurai</a> 
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        </div>

        <footer class="mt-20 text-center text-sm text-gray-400">
            <p>Powered by Toshimart on Base | DYOR - Not Financial Advice | Last Update: {{ last_update }}</p>
        </footer>
    </div>

    <script>
        // Theme toggle (kept from original)
        const html = document.documentElement;
        const toggleBtn = document.getElementById('toggle-theme');
        const themeIcon = document.getElementById('theme-icon');
        const themeText = document.getElementById('theme-text');

        function setTheme(isDark) {
            if (isDark) {
                html.classList.add('dark');
                html.classList.remove('light');
                themeIcon.textContent = '🌙';
                themeText.textContent = 'Dark';
                localStorage.theme = 'dark';
            } else {
                html.classList.add('light');
                html.classList.remove('dark');
                themeIcon.textContent = '☀️';
                themeText.textContent = 'Light';
                localStorage.theme = 'light';
            }
        }

        if (localStorage.theme === 'light') setTheme(false);
        else setTheme(true);

        toggleBtn.addEventListener('click', () => setTheme(!html.classList.contains('dark')));

        // Load Neko Metrics from Dexscreener
        async function loadNekoMetrics() {
            try {
                const res = await fetch('https://api.dexscreener.com/latest/dex/tokens/0x28973c4ef9ae754b076a024996350d3b16a38453');
                const data = await res.json();
                const pair = data.pairs[0]; // Assume first pair

                const price = parseFloat(pair.priceUsd).toFixed(6);
                document.getElementById('neko-price').textContent = '$' + price;
                document.getElementById('price-fill').style.width = Math.min(100, (price * 100000) ) + '%'; // Arbitrary scale

                const mc = (pair.fdv / 1e6).toFixed(2) + 'M'; // Assuming fdv is market cap
                document.getElementById('neko-mc').textContent = '$' + mc;
                document.getElementById('mc-fill').style.width = Math.min(100, (pair.fdv / 1e9) * 100) + '%';

                const liq = (pair.liquidity.usd / 1e3).toFixed(0) + 'K';
                document.getElementById('neko-liq').textContent = '$' + liq;
                document.getElementById('liq-fill').style.width = Math.min(100, (pair.liquidity.usd / 1e6) * 100) + '%';

                const vol = (pair.volume.h24 / 1e3).toFixed(0) + 'K';
                document.getElementById('neko-vol').textContent = '$' + vol;
                document.getElementById('vol-fill').style.width = Math.min(100, (pair.volume.h24 / 1e6) * 100) + '%';

                // Holders: Dexscreener doesn't provide, fallback to estimate or skip
                document.getElementById('neko-holders').textContent = 'TBD'; // Or fetch from Base explorer API if added
                document.getElementById('holders-fill').style.width = '50%'; // Placeholder

            } catch (err) {
                console.error(err);
                document.getElementById('neko-price').textContent = 'N/A';
            }
        }

        loadNekoMetrics();

        // Lore/Quotes (hardcoded from your X theme)
        const lore = [
            { title: "The Zenshin Way", content: "It is better to be a warrior in a garden than a gardener in a war. Neko leads the clan with courage and wisdom." },
            { title: "Forward Progress", content: "The path doesn’t need to be clear—only your courage to keep walking. Join Neko on Base." },
            { title: "Clan United", content: "Neko sharpens claws alongside Toshi, Doginme, and Yuki. United cats conquer the chain." },
            { title: "Battle Ready", content: "In the garden of peace, Neko prepares for battle. Zenshin: Always forward." },
            { title: "Samurai Spirit", content: "Courage in the face of adversity. Neko embodies the samurai code on Base." },
        ];

        function displayLore() {
            const feed = document.getElementById('lore-feed');
            feed.innerHTML = '';
            lore.forEach(item => {
                const card = document.createElement('div');
                card.className = 'lore-card';
                card.innerHTML = `
                    <h3 class="text-xl font-bold mb-3 text-white light:text-black">${item.title}</h3>
                    <p class="text-gold-400 text-sm">${item.content}</p>
                `;
                feed.appendChild(card);
            });
        }

        displayLore();
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)

