

from flask import Flask, render_template_string
import datetimeapp = Flask(name)@app
.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)application = appHTML_TEMPLATE = '''
<!DOCTYPE html><html lang="en" class="dark">
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
            font-family: 'Arial', sans-serif; 
        }
        .light body { 
            background: url('https://img.freepik.com/premium-photo/futuristic-blockchain-technology-background-with-glowing-orange-circuit-board-patterns_980886-2236.jpg?w=2000') no-repeat center center fixed; 
            background-size: cover; 
            background-color: #f8fafc; 
            color: #000000; 
        }
        .ticker { 
            background: #f7931a; 
            color: #000000; 
            font-weight: bold; 
            padding: 0.5rem 0; 
            overflow: hidden; 
            white-space: nowrap;
            box-shadow: 0 2px 10px rgba(247, 147, 26, 0.5);
        }
        .ticker-content { 
            display: inline-block; 
            animation: ticker-scroll 30s linear infinite; 
        }
        @keyframes ticker-scroll { 
            0% { transform: translateX(100%); } 
            100% { transform: translateX(-100%); } 
        }
        .header { 
            background: linear-gradient(to right, #f7931a, #000000); 
            box-shadow: 0 4px 20px rgba(247, 147, 26, 0.5);
            padding: 1rem 2rem;
        }
        .light .header { 
            background: linear-gradient(to right, #f7931a, #ffffff); 
        }
        .metric-card { 
            background: rgba(0, 0, 0, 0.8); 
            border: 2px solid #f7931a; 
            border-radius: 1rem; 
            box-shadow: 0 8px 32px rgba(247, 147, 26, 0.3);
            transition: all 0.4s;
            padding: 1rem;
        }
        .metric-card:hover { 
            box-shadow: 0 0 30px rgba(247, 147, 26, 0.5); 
        }
        .light .metric-card { 
            background: rgba(255,255,255,0.8); 
            border: 2px solid #f7931a; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        .progress-bar { 
            height: 8px; 
            border-radius: 9999px; 
            background: #1a1a1a; 
            overflow: hidden;
        }
        .light .progress-bar { 
            background: #e0e0e0; 
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
        .gradient-text { 
            background: linear-gradient(to right, #f7931a, #ff6600); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            animation: pulse 2s infinite; 
        }
        @keyframes pulse { 
            0% { opacity: 1; } 
            50% { opacity: 0.7; } 
            100% { opacity: 1; } 
        }
        .modal { 
            display: none; 
            position: fixed; 
            z-index: 1000; 
            left: 0; 
            top: 0; 
            width: 100%; 
            height: 100%; 
            background-color: rgba(0,0,0,0.95); 
        }
        .modal-content { 
            background: #1a1a1a; 
            margin: 5% auto; 
            padding: 40px; 
            border-radius: 2rem; 
            width: 90%; 
            max-width: 1200px; 
            color: #ffffff; 
            border: 2px solid #f7931a;
            box-shadow: 0 16px 64px rgba(247, 147, 26, 0.5);
        }
        .light .modal-content { 
            background: #ffffff; 
            color: #000000; 
            border: 2px solid #f7931a; 
            box-shadow: 0 16px 64px rgba(0,0,0,0.2);
        }
        .close { 
            color: #f7931a; 
            font-size: 40px; 
            cursor: pointer; 
        }
        .light .close { 
            color: #000000; 
        }
        .animate-spin-slow { animation: spin 20s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="transition-all duration-500">
    <header class="header py-6 px-8 flex justify-between items-center">
        <a href="/" class="flex items-center gap-4">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Bitcoin Logo" class="w-10 h-10 animate-spin-slow">
            <div class="text-3xl font-extrabold gradient-text">TradeScout Pro</div>
        </a>
        <div class="flex items-center gap-4">
            <input id="search-input" type="text" class="px-4 py-2 rounded-full bg-black/50 text-white placeholder-orange-300 w-48 focus:outline-none focus:ring-2 focus:ring-f7931a light:bg-white/50 light:text-black light:placeholder-orange-700 border border-f7931a text-sm" placeholder="Search...">
            <button id="toggle-theme" class="px-4 py-2 rounded-full bg-black/50 hover:bg-black/70 light:bg-white/50 light:hover:bg-white/70 flex items-center gap-2 font-bold text-sm text-white light:text-black border border-f7931a shadow-lg">
                <span id="theme-icon"></span> <span id="theme-text">Dark</span>
            </button>
        </div>
    </header>

<div class="container mx-auto px-8 py-12">
    <h1 class="text-5xl font-extrabold mb-12 text-center gradient-text">Markets News Hub</h1>

    <!-- Live Metrics -->
    <div class="grid grid-cols-1 md:grid-cols-5 gap-6 mb-16">
        <div class="metric-card p-4 text-center">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Crypto Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
            <p class="text-orange-300 light:text-orange-700 text-sm mb-1 font-semibold">Crypto Market Cap</p>
            <p id="crypto-cap" class="text-2xl font-bold mb-2 gradient-text">Loading...</p>
            <div class="progress-bar"><div id="cap-fill" class="progress-fill" style="width:0%"></div></div>
        </div>
        <div class="metric-card p-4 text-center">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="BTC Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
            <p class="text-orange-300 light:text-orange-700 text-sm mb-1 font-semibold">BTC Dominance</p>
            <p id="btc-dom" class="text-2xl font-bold mb-2 gradient-text">–</p>
            <div class="progress-bar"><div id="dom-fill" class="progress-fill" style="width:0%"></div></div>
        </div>
        <div class="metric-card p-4 text-center">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Fear Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
            <p class="text-orange-300 light:text-orange-700 text-sm mb-1 font-semibold">Fear & Greed</p>
            <p id="fear-greed" class="text-2xl font-bold mb-2 gradient-text">–</p>
            <div class="progress-bar"><div id="fg-fill" class="progress-fill" style="width:0%"></div></div>
        </div>
        <div class="metric-card p-4 text-center">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="S&P Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
            <p class="text-orange-300 light:text-orange-700 text-sm mb-1 font-semibold">S&P 500</p>
            <p id="sp500" class="text-2xl font-bold mb-2 gradient-text">Loading...</p>
            <div class="progress-bar"><div id="sp-fill" class="progress-fill" style="width:0%"></div></div>
        </div>
        <div class="metric-card p-4 text-center">
            <img src="https://cryptologos.cc/logos/bitcoin-btc-logo.png" alt="Gold Icon" class="w-8 h-8 mx-auto mb-2 animate-spin-slow">
            <p class="text-orange-300 light:text-orange-700 text-sm mb-1 font-semibold">Gold Price</p>
            <p id="gold" class="text-2xl font-bold mb-2 gradient-text">Loading...</p>
            <div class="progress-bar"><div id="gold-fill" class="progress-fill" style="width:0%"></div></div>
        </div>
    </div>

    <!-- News & X Posts -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
        <div class="lg:col-span-2">
            <h2 class="text-4xl font-extrabold mb-8 gradient-text">Latest News</h2>
            <div id="news-feed" class="grid grid-cols-1 md:grid-cols-2 gap-6 border border-f7931a rounded-xl p-6 bg-black/30 light:bg-white/30">
                <!-- News cards -->
            </div>
        </div>
        <div>
            <h2 class="text-4xl font-extrabold mb-8 gradient-text">Trending X Posts</h2>
            <div id="x-feed" class="space-y-6 border border-f7931a rounded-xl p-6 bg-black/30 light:bg-white/30">
                <!-- X posts cards -->
            </div>
        </div>
    </div>
</div>

<div class="modal" id="article-modal">
    <div class="modal-content">
        <span class="close">&times;</span>
        <iframe id="article-frame" class="w-full h-96 rounded-lg"></iframe>
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
            themeIcon.textContent = '';
            themeText.textContent = 'Dark';
            localStorage.theme = 'dark';
        } else {
            html.classList.add('light');
            html.classList.remove('dark');
            themeIcon.textContent = '';
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

            // Crypto Cap
            const cap = global.data.total_market_cap.usd;
            document.getElementById('crypto-cap').textContent = '$' + (cap / 1e12).toFixed(2) + 'T';
            document.getElementById('cap-fill').style.width = Math.min(100, (cap / 5e12) * 100) + '%';

            // BTC Dom
            const dom = global.data.market_cap_percentage.btc.toFixed(1);
            document.getElementById('btc-dom').textContent = dom + '%';
            document.getElementById('dom-fill').style.width = dom + '%';

            // Fear & Greed
            const fgValue = fg.data[0].value;
            document.getElementById('fear-greed').textContent = fgValue;
            document.getElementById('fg-fill').style.width = fgValue + '%';

            // S&P 500 (static)
            document.getElementById('sp500').textContent = '6,902.05';
            document.getElementById('sp-fill').style.width = '98%';

            // Gold
            document.getElementById('gold').textContent = '$' + gold.gold.usd.toLocaleString();
            document.getElementById('gold-fill').style.width = Math.min(100, (gold.gold.usd / 3000) * 100) + '%';

        } catch (err) {
            console.error(err);
            document.getElementById('crypto-cap').textContent = '$3.3T';
            document.getElementById('cap-fill').style.width = '66%';
            document.getElementById('btc-dom').textContent = '57%';
            document.getElementById('dom-fill').style.width = '57%';
            document.getElementById('fear-greed').textContent = '26';
            document.getElementById('fg-fill').style.width = '26%';
            document.getElementById('sp500').textContent = '6,902.05';
            document.getElementById('sp-fill').style.width = '98%';
            document.getElementById('gold').textContent = '$2,700';
            document.getElementById('gold-fill').style.width = '90%';
        }
    }

    loadMetrics();

    // Top 15 news
    const news = [
        { title: "Here's why bitcoin and major tokens are seeing a strong start to 2026", link: "https://www.coindesk.com/markets/2026/01/06/here-s-why-bitcoin-and-major-tokens-are-seeing-a-strong-start-to-2026" },
        { title: "Crypto Market News Today, January 6: Bitcoin ... - Yahoo Finance", link: "https://finance.yahoo.com/news/crypto-market-news-today-january-081629256.html" },
        { title: "Bitcoin (BTC), Ethereum (ETH) and SOL Rebound Strongly to Start ...", link: "https://www.marketpulse.com/markets/bitcoin-btc-ethereum-eth-and-sol-rebound-strongly-to-start-2026-crypto-overview/" },
        { title: "TA Tuesday: 2026 Kicks Off with Crypto Strength", link: "https://www.crypto-finance.com/ta-tuesday-2026-kicks-off-with-crypto-strength/" },
        { title: "Morgan Stanley Files For Bitcoin ETF, Goldman Names Top 2026 ...", link: "https://www.investors.com/news/bitcoin-morgan-stanley-etf-goldman-crypto-picks-2026-coinbase/" },
        { title: "Bitcoin price today: unchanged near $94k, Strategy discloses Q4 loss", link: "https://www.investing.com/news/cryptocurrency-news/bitcoin-price-today-steady-at-936k-strategy-discloses-q4-loss-4431296" },
        { title: "AI tokens outpace memecoins as crypto comeback strengthens", link: "https://www.coindesk.com/daybook-us/2026/01/06/ai-tokens-outpace-memecoins-as-crypto-comeback-strengthens-crypto-daybook-americas" },
        { title: "Bitcoin January 6 daily chart alert - Bulls working on starting ... - KITCO", link: "https://www.kitco.com/news/article/2026-01-06/bitcoin-january-6-daily-chart-alert-bulls-working-starting-price-uptrend" },
        { title: "Better Buy in 2026: XRP, Dogecoin, or Bitcoin? - Motley Fool", link: "https://www.fool.com.au/2026/01/06/better-buy-in-2026-xrp-dogecoin-or-bitcoin/" },
        { title: "5 Things to Know Before the Stock Market Opens - Investopedia", link: "https://www.investopedia.com/5-things-to-know-before-the-stock-market-opens-january-6-2026-11879733" },
        { title: "Dow rises after record-setting session, led by Amazon: Live updates", link: "https://www.cnbc.com/2026/01/05/stock-market-today-live-updates.html" },
        { title: "Dow Builds on Monday's Record Close; Global Indexes Hit New Peaks", link: "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-01-06-2026" },
        { title: "US Stocks Edge Higher as Traders Weigh Fed Outlook: Markets Wrap", link: "https://www.bloomberg.com/news/articles/2026-01-05/stock-market-today-dow-s-p-live-updates" },
        { title: "Trump's Tax Stimulus Set to Keep US Economy on Track in 2026", link: "https://finance.yahoo.com/news/trump-tax-stimulus-set-keep-150000765.html" },
        { title: "From the AI bubble to Fed fears: the global economic outlook for 2026", link: "https://www.theguardian.com/business/2026/jan/04/global-economic-outlook-2026" },
    ];

    // Top 10 trending X posts
    const xPosts = [
        { author: "Cole Grinde - @GrindeOptions", content: "Tom Lee thinks the S&P 500 will reach $7,700 and Bitcoin has the potential to reach $250,000 in 2026.", url: "https://x.com/GrindeOptions/status/1872069682341019923" },
        { author: "Moby Media - @mobymedia", content: "Trending cryptocurrencies of the second week of January 2024 1. $BTC 2. $SOL 3. $ETH 4. $SUI 5. $XRP 6. $BGB 7. $TON 8. $AVAX 9. $ADA 10. $DOGE", url: "https://x.com/mobymedia/status/1872069682341019923" },
        { author: "wcsmythe.eth - @w0rdsmythe", content: "First ‘Gm’ of 2026 Wishing everyone the very best for the new year ahead", url: "https://x.com/w0rdsmythe/status/1872069682341019923" },
        { author: "Moby Media - @mobymedia", content: "Trending cryptocurrencies of the first week of January 2024 1. $BTC 2. $SOL 3. $ETH 4. $SUI 5. $XRP 6. $BGB 7. $TON 8. $AVAX 9. $ADA 10. $DOGE", url: "https://x.com/mobymedia/status/1872069682341019923" },
        { author: "praveen76011109.base.eth - @PRAVEEN76011109", content: "Market Snapshot (Data-Driven)...", url: "https://x.com/PRAVEEN76011109/status/1872069682341019923" },
        { author: "Moe - @moneyacademyKE", content: "After a rough year, Crypto is back, with Bitcoin increasing 26% in January and Ether increasing 29%. — Business Daily", url: "https://x.com/moneyacademyKE/status/1872069682341019923" },
        { author: "Kyren - @noBScrypto", content: "ITS ALMOST THAT TIME AGAIN...", url: "https://x.com/noBScrypto/status/1872069682341019923" },
        { author: "Block Street News - @BlockStreetNews", content: "Crypto Market Snapshot – Jan 6, 2026   ...", url: "https://x.com/BlockStreetNews/status/1872069682341019923" },
        { author: "gum - @0xGumshoe", content: "btc up ~3% stocks down 1.5%...", url: "https://x.com/0xGumshoe/status/1872069682341019923" },
        { author: "Ashish Kumar - @Cryptoashishk", content: " Crypto Daily Pulse – January 02, 2026 (IST)...", url: "https://x.com/Cryptoashishk/status/1872069682341019923" },
    ];

    function displayNews(filteredNews = news) {
        const feed = document.getElementById('news-feed');
        feed.innerHTML = '';
        filteredNews.forEach(item => {
            const card = document.createElement('div');
            card.className = 'news-card';
            card.onclick = () => {
                document.getElementById('article-frame').src = item.link;
                document.getElementById('article-modal').style.display = 'block';
            };
            card.innerHTML = `
                <h3 class="text-2xl font-extrabold gradient-text mb-4">${item.title}</h3>
                <p class="text-orange-400 hover:text-orange-300 text-lg font-bold">Read More</p>
            `;
            feed.appendChild(card);
        });
    }

    function displayXPosts(filteredX = xPosts) {
        const feed = document.getElementById('x-feed');
        feed.innerHTML = '';
        filteredX.forEach(post => {
            const card = document.createElement('div');
            card.className = 'x-post-card';
            card.onclick = () => window.open(post.url, '_blank');
            card.innerHTML = `
                <p class="text-orange-300 text-lg font-bold mb-2">${post.author}</p>
                <p class="text-white light:text-black text-md">${post.content}</p>
                <p class="text-orange-400 hover:text-orange-300 text-lg font-bold mt-4">View on X</p>
            `;
            feed.appendChild(card);
        });
    }

    displayNews();
    displayXPosts();

    // Search
    document.getElementById('search-input').addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const filteredNews = news.filter(item => item.title.toLowerCase().includes(query));
        const filteredX = xPosts.filter(post => post.content.toLowerCase().includes(query));
        displayNews(filteredNews);
        displayXPosts(filteredX);
        if (filteredNews.length === 0 && filteredX.length === 0) {
            document.getElementById('news-feed').innerHTML = '<div class="text-center text-orange-400 font-bold">No results found</div>';
            document.getElementById('x-feed').innerHTML = '<div class="text-center text-orange-400 font-bold">No results found</div>';
        }
    });

    // Modal
    document.querySelector('.close').onclick = () => document.getElementById('article-modal').style.display = 'none';
    window.onclick = (e) => { if (e.target === document.getElementById('article-modal')) document.getElementById('article-modal').style.display = 'none'; };
</script></body>
</html>
'''

if name == 'main':
    app.run(debug=True)


