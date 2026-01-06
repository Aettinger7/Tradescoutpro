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
    <title>TradeScout Pro - Markets News Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { 
            background: url('https://img.freepik.com/premium-photo/futuristic-blockchain-technology-background-with-glowing-orange-circuit-board-patterns_980886-2236.jpg?w=2000') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #000000; 
            color: #ffffff; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
        }
        .light body { 
            background: url('https://img.freepik.com/premium-photo/futuristic-blockchain-technology-background-with-glowing-orange-circuit-board-patterns_980886-2236.jpg?w=2000') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #f8fafc; 
            color: #000000; 
        }
        .header { 
            background: linear-gradient(to right, #f7931a, rgba(0,0,0,0.8)); 
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(247, 147, 26, 0.4);
        }
        .light .header { 
            background: linear-gradient(to right, #f7931a, rgba(255,255,255,0.8)); 
        }
        .logo-text {
            font-weight: 900;
            font-size: 2.5rem;
            background: linear-gradient(to right, #f7931a, #ff6600);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(247, 147, 26, 0.8);
        }
        .metric-card { 
            background: rgba(0, 0, 0, 0.8); 
            border: 2px solid #f7931a; 
            border-radius: 1rem; 
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.3);
            transition: all 0.4s;
        }
        .metric-card:hover { 
            box-shadow: 0 0 35px rgba(247, 147, 26, 0.6);
        }
        .light .metric-card { 
            background: rgba(255,255,255,0.9); 
            border: 2px solid #f7931a; 
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
            background: linear-gradient(to right, #f7931a, #ff6600);
            transition: width 2s ease-in-out;
        }
        .news-card, .x-post-card { 
            background: rgba(0, 0, 0, 0.85); 
            border: 2px solid #f7931a; 
            border-radius: 1rem; 
            transition: all 0.4s;
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.2);
            padding: 1.5rem; 
        }
        .news-card:hover, .x-post-card:hover { 
            box-shadow: 0 0 40px rgba(247, 147, 26, 0.5);
            transform: translateY(-5px);
        }
        .light .news-card, .light .x-post-card { 
            background: rgba(255,255,255,0.85); 
            border: 2px solid #f7931a; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        }
        .section-title {
            font-size: 3.5rem;
            font-weight: 900;
            background: linear-gradient(to right, #f7931a, #ff6600);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(247, 147, 26, 0.6);
        }
        .animate-spin-slow { animation: spin 20s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="transition-all duration-500">
    <header class="header py-6 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Bitcoin Logo" class="w-10 h-10 animate-spin-slow">
            <div class="logo-text">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <input id="search-input" type="text" class="px-5 py-2 rounded-full bg-black/50 text-white placeholder-orange-300 w-60 focus:outline-none focus:ring-2 focus:ring-f7931a light:bg-white/50 light:text-black light:placeholder-orange-700 border border-f7931a text-sm" placeholder="Search crypto, economy...">
            <button id="toggle-theme" class="px-5 py-2 rounded-full bg-black/50 hover:bg-black/70 light:bg-white/50 light:hover:bg-white/70 flex items-center gap-2 font-bold text-sm text-white light:text-black border border-f7931a shadow-lg">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-8 py-12">
        <h1 class="text-5xl font-extrabold mb-16 text-center section-title">Markets News Hub</h1>

        <!-- Metrics -->
        <div class="grid grid-cols-1 md:grid-cols-5 gap-8 mb-20">
            <div class="metric-card p-6 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Crypto Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-2 font-semibold">Crypto Market Cap</p>
                <p id="crypto-cap" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="cap-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="BTC Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-2 font-semibold">BTC Dominance</p>
                <p id="btc-dom" class="text-3xl font-extrabold mb-4 text-white light:text-black">–</p>
                <div class="progress-bar"><div id="dom-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Fear Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-2 font-semibold">Fear & Greed</p>
                <p id="fear-greed" class="text-3xl font-extrabold mb-4 text-white light:text-black">–</p>
                <div class="progress-bar"><div id="fg-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="S&P Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-2 font-semibold">S&P 500</p>
                <p id="sp500" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="sp-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
            <div class="metric-card p-6 text-center">
                <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Gold Icon" class="w-10 h-10 mx-auto mb-3 animate-spin-slow">
                <p class="text-orange-300 light:text-orange-700 text-sm mb-2 font-semibold">Gold Price</p>
                <p id="gold" class="text-3xl font-extrabold mb-4 text-white light:text-black">Loading...</p>
                <div class="progress-bar"><div id="gold-fill" class="progress-fill" style="width:0%"></div></div>
            </div>
        </div>

        <!-- News & X -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
            <div class="lg:col-span-2">
                <h2 class="text-4xl font-extrabold mb-10 section-title">Latest News</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div id="news-feed"></div>
                </div>
            </div>
            <div>
                <h2 class="text-4xl font-extrabold mb-10 section-title">Trending X Posts</h2>
                <div class="grid grid-cols-1 gap-8">
                    <div id="x-feed"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const API_KEY = 'CG-AmnUtrzxMeYvcPeRsWejUaHu';

        // Theme toggle
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

        async function loadMetrics() {
            try {
                const [globalRes, fgRes, goldRes] = await Promise.all([
                    fetch(`https://api.coingecko.com/api/v3/global?x_cg_demo_api_key=${API_KEY}`),
                    fetch('https://api.alternative.me/fng/?limit=1'),
                    fetch(`https://api.coingecko.com/api/v3/simple/price?ids=gold&vs_currencies=usd&x_cg_demo_api_key=${API_KEY}`)
                ]);

                const global = await globalRes.json();
                const fg = await fgRes.json();
                const gold = await goldRes.json();

                const cap = global.data.total_market_cap.usd;
                document.getElementById('crypto-cap').textContent = '$' + (cap / 1e12).toFixed(2) + 'T';
                document.getElementById('cap-fill').style.width = Math.min(100, (cap / 5e12) * 100) + '%';

                const dom = global.data.market_cap_percentage.btc.toFixed(1);
                document.getElementById('btc-dom').textContent = dom + '%';
                document.getElementById('dom-fill').style.width = dom + '%';

                const fgValue = fg.data[0].value;
                document.getElementById('fear-greed').textContent = fgValue;
                document.getElementById('fg-fill').style.width = fgValue + '%';

                document.getElementById('sp500').textContent = '6,902.05';
                document.getElementById('sp-fill').style.width = '98%';

                const goldPrice = gold.gold.usd.toLocaleString();
                document.getElementById('gold').textContent = '$' + goldPrice;
                document.getElementById('gold-fill').style.width = Math.min(100, (gold.gold.usd / 5000) * 100) + '%';

            } catch (err) {
                console.error(err);
            }
        }

        loadMetrics();

        const news = [
            { title: "Bitcoin and major tokens strong start to 2026", link: "https://www.coindesk.com/markets/2026/01/06/here-s-why-bitcoin-and-major-tokens-are-seeing-a-strong-start-to-2026" },
            { title: "Morgan Stanley files for bitcoin, solana ETFs", link: "https://www.reuters.com/business/morgan-stanley-files-bitcoin-etf-2026-01-06/" },
            { title: "Tom Lee predicts Bitcoin new ATH in January", link: "https://seekingalpha.com/news/4536824-bitcoin-could-hit-new-record-in-january-fundstrats-tom-lee-predicts" },
            { title: "XRP rockets 11% as Ripple ETFs see high volumes", link: "https://www.coindesk.com/markets/2026/01/06/xrp-rockets-11-to-nearly-usd2-40-as-ripple-linked-etfs-see-highest-trading-volumes" },
            { title: "AI tokens outpace memecoins", link: "https://www.coindesk.com/daybook-us/2026/01/06/ai-tokens-outpace-memecoins-as-crypto-comeback-strengthens-crypto-daybook-americas" },
            { title: "Dow rises after record-setting session", link: "https://www.cnbc.com/2026/01/05/stock-market-today-live-updates.html" },
            { title: "Trump's Tax Stimulus Set to Keep US Economy on Track in 2026", link: "https://finance.yahoo.com/news/trump-tax-stimulus-set-keep-150000765.html" },
            { title: "Gold price hits $4,500 amid geopolitical tensions", link: "https://www.kitco.com/news/2026-01-06/Gold-price-hits-4500.html" },
            { title: "US Stocks Edge Higher as Traders Weigh Fed Outlook", link: "https://www.bloomberg.com/news/articles/2026-01-05/stock-market-today-dow-s-p-live-updates" },
            { title: "Bitcoin buyers target $100,000 by end of January", link: "https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/" },
            { title: "Real crypto regulation will generate excitement in 2026", link: "https://finance.yahoo.com/video/real-crypto-regulation-generate-lot-175000605.html" },
            { title: "3 Altcoins To Watch In The First Week of January 2026", link: "https://beincrypto.com/3-altcoins-to-watch-in-the-first-week-of-january-2026/" },
            { title: "Bitcoin January 6 daily chart alert - Bulls working on starting uptrend", link: "https://www.kitco.com/news/article/2026-01-06/bitcoin-january-6-daily-chart-alert-bulls-working-starting-price-uptrend" },
            { title: "5 Things to Know Before the Stock Market Opens", link: "https://www.investopedia.com/5-things-to-know-before-the-stock-market-opens-january-6-2026-11879733" },
            { title: "From the AI bubble to Fed fears: the global economic outlook for 2026", link: "https://www.theguardian.com/business/2026/jan/04/global-economic-outlook-2026" },
        ];

        const xPosts = [
            { author: "@Bullish__Degen", content: "United States Crypto Reserve Official USCR Airdrop - momentum driving innovation", url: "https://x.com/Bullish__Degen/status/187..." },
            { author: "@Bullish__Degen", content: "USCR Airdrop - growth opens new opportunities", url: "https://x.com/Bullish__Degen/status/187..." },
            { author: "@AyTanzania", content: "Wojak Coin Official Airdrop - momentum drives innovation", url: "https://x.com/AyTanzania/status/187..." },
            { author: "@aimeehall_eth", content: "$LIT points dashboard update - farm every day", url: "https://x.com/aimeehall_eth/status/187..." },
            { author: "@aimeehall_eth", content: "$ZEC hit 5 MILLION shielded supply - check eligibility", url: "https://x.com/aimeehall_eth/status/187..." },
            { author: "@solrewards", content: "If this gets 1,000 likes, giving away 1 SOL to 5 people", url: "https://x.com/solrewards/status/187..." },
            { author: "@yaranaka_sol", content: "2026 Airdrop Live - drop SOL address for $YARANAIKA", url: "https://x.com/yaranaka_sol/status/187..." },
            { author: "@solrewards", content: "Drop wallets - 99 minutes giveaway", url: "https://x.com/solrewards/status/187..." },
            { author: "@BlockStreetNews", content: "Crypto Market Snapshot – Jan 6, 2026", url: "https://x.com/BlockStreetNews/status/187..." },
            { author: "@0xGumshoe", content: "btc up ~3% stocks down 1.5%...", url: "https://x.com/0xGumshoe/status/187..." },
        ];

        function displayNews(filtered = news) {
            const feed = document.getElementById('news-feed');
            feed.innerHTML = '';
            filtered.forEach(item => {
                const card = document.createElement('div');
                card.className = 'news-card';
                card.onclick = () => window.open(item.link, '_blank');
                card.innerHTML = `
                    <h3 class="text-xl font-bold mb-3 text-white light:text-black">${item.title}</h3>
                    <p class="text-orange-400 hover:text-orange-300 text-sm font-bold cursor-pointer">Read More →</p>
                `;
                feed.appendChild(card);
            });
        }

        function displayXPosts(filtered = xPosts) {
            const feed = document.getElementById('x-feed');
            feed.innerHTML = '';
            filtered.forEach(post => {
                const card = document.createElement('div');
                card.className = 'x-post-card';
                card.onclick = () => window.open(post.url, '_blank');
                card.innerHTML = `
                    <p class="text-orange-300 text-lg font-bold mb-2">${post.author}</p>
                    <p class="text-white light:text-black text-sm mb-3">${post.content}</p>
                    <p class="text-orange-400 hover:text-orange-300 text-sm font-bold cursor-pointer">View on X →</p>
                `;
                feed.appendChild(card);
            });
        }

        displayNews();
        displayXPosts();

        document.getElementById('search-input').addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            const filteredNews = news.filter(item => item.title.toLowerCase().includes(query));
            const filteredX = xPosts.filter(post => post.content.toLowerCase().includes(query));
            displayNews(filteredNews);
            displayXPosts(filteredX);
        });
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)

