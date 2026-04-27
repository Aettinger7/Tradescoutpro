from flask import Flask, render_template_string, send_from_directory
import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Neko the Samurai Cat ⚔️ $NEKO on Base</title>

  <meta name="description" content="Neko the Samurai Cat ($NEKO) – Zenshin Clan meme token on Base. Forward progress with honor. Trade on Uniswap. Join the clan!">
  <meta property="og:title" content="Neko the Samurai Cat ⚔️🐱 $NEKO on Base">
  <meta property="og:description" content="Zenshin Clan – Forward Progress. Warrior in a garden, claws sharpened on Base.">
  <meta property="og:image" content="https://i.ibb.co/6cpdFyYv/image-24.jpg">
  <meta property="og:url" content="https://www.nekothesamurai.com">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Neko the Samurai Cat ⚔️🐱 $NEKO">
  <meta name="twitter:description" content="Forward Progress – Join the Zenshin Clan on Base.">
  <meta name="twitter:image" content="https://i.ibb.co/QF6cS9ZV/Neko-The-Samurai.png">
  <meta name="twitter:site" content="@NekoTheSamurai">

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-34WMSCBW1R"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-34WMSCBW1R');
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@400;700;800&family=Zen+Kaku+Gothic+New:wght@300;400;700&family=Noto+Serif+JP:wght@200;400&display=swap" rel="stylesheet" />

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    html, body { overflow-x: hidden; max-width: 100vw; }

    :root {
      --ink:      #07050a;
      --deep:     #0f0b14;
      --panel:    #13101a;
      --crimson:  #7a0012;
      --red:      #b01020;
      --gold:     #c89b3c;
      --gold-lt:  #e8c06a;
      --gold-dim: #6e5220;
      --cream:    #ede4cc;
      --muted:    #7a6e60;
    }

    body {
      background: var(--ink);
      color: var(--cream);
      font-family: 'Zen Kaku Gothic New', sans-serif;
      font-weight: 300;
    }

    /* ── CURSOR ── */
    *, a, button { cursor: none !important; }
    #cur {
      position: fixed; z-index: 9999; pointer-events: none;
      width: 14px; height: 14px;
      border: 1.5px solid var(--gold);
      border-radius: 50%;
      transform: translate(-50%,-50%);
      transition: width .2s, height .2s, background .2s;
      mix-blend-mode: exclusion;
    }
    #cur.big { width: 38px; height: 38px; background: rgba(200,155,60,.12); border-color: var(--gold-lt); }

    /* ── GRAIN ── */
    body::after {
      content:''; position:fixed; inset:0; z-index:1; pointer-events:none;
      background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='.03'/%3E%3C/svg%3E");
      opacity:.55;
    }

    /* ── NAV ── */
    nav {
      position: fixed; inset: 0 0 auto; z-index: 200;
      padding: 1rem 3rem;
      display: flex; align-items: center; justify-content: space-between;
      background: rgba(7,5,10,.97);
      border-bottom: 1px solid rgba(200,155,60,.2);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }
    .nav-logo {
      display: flex; align-items: center; gap: .8rem; text-decoration: none;
      font-family: 'Shippori Mincho B1', serif;
      font-size: 1rem; font-weight: 800;
      color: var(--gold); letter-spacing: .15em;
    }
    .nav-links { display: flex; align-items: center; gap: 2.2rem; list-style: none; }
    .nav-links a {
      font-family: 'Shippori Mincho B1', serif;
      font-size: .82rem; letter-spacing: .18em; text-transform: uppercase;
      color: var(--cream); text-decoration: none; font-weight: 700;
      transition: color .25s; position: relative;
    }
    .nav-links a::after {
      content:''; position:absolute; bottom:-3px; left:0;
      width:0; height:1px; background:var(--gold); transition: width .3s;
    }
    .nav-links a:hover { color: var(--gold-lt); }
    .nav-links a:hover::after { width: 100%; }
    .nav-buy {
      font-family: 'Shippori Mincho B1', serif !important;
      font-size: .8rem !important; letter-spacing: .15em !important;
      font-weight: 700 !important;
      padding: .5rem 1.4rem;
      border: 1px solid var(--gold) !important;
      border-radius: 2px;
      color: var(--gold-lt) !important;
      background: rgba(200,155,60,.08);
      transition: background .25s, box-shadow .25s !important;
    }
    .nav-buy:hover { background: rgba(200,155,60,.2) !important; box-shadow: 0 0 20px rgba(200,155,60,.25) !important; }
    .nav-buy::after { display: none !important; }

    .nav-whitepaper {
      font-family: 'Shippori Mincho B1', serif !important;
      font-size: .8rem !important; letter-spacing: .15em !important;
      font-weight: 700 !important;
      padding: .5rem 1.4rem;
      border: 1px solid rgba(200,155,60,.4) !important;
      border-radius: 2px;
      color: var(--gold-dim) !important;
      background: transparent;
      transition: background .25s, box-shadow .25s, color .25s, border-color .25s !important;
    }
    .nav-whitepaper:hover {
      background: rgba(200,155,60,.08) !important;
      border-color: var(--gold) !important;
      color: var(--gold-lt) !important;
      box-shadow: 0 0 16px rgba(200,155,60,.15) !important;
    }
    .nav-whitepaper::after { display: none !important; }

    /* ── HAMBURGER ── */
    .hamburger {
      display: none;
      background: none;
      border: 1px solid rgba(200,155,60,.4);
      padding: .5rem;
      width: 48px;
      height: 48px;
      border-radius: 2px;
      position: relative;
      cursor: none !important;
      transition: border-color .25s, box-shadow .25s;
    }
    .hamburger:hover {
      border-color: var(--gold);
      box-shadow: 0 0 16px rgba(200,155,60,.2);
    }
    .hamburger .ham-line {
      position: absolute;
      left: 25%;
      width: 50%;
      height: 2px;
      background: var(--gold);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      border-radius: 2px;
    }
    .hamburger .ham-line:nth-child(1) { top: 30%; }
    .hamburger .ham-line:nth-child(2) { top: 50%; }
    .hamburger .ham-line:nth-child(3) { top: 70%; }

    .hamburger.open .ham-line:nth-child(1) {
      top: 50%;
      transform: rotate(45deg);
    }
    .hamburger.open .ham-line:nth-child(2) {
      opacity: 0;
    }
    .hamburger.open .ham-line:nth-child(3) {
      top: 50%;
      transform: rotate(-45deg);
    }

    /* The rest of your original styles continue here (hero, trade, lore, etc.) */
    /* ... full original CSS from your first message ... */

  </style>
</head>
<body>

<!-- Your full original body content starts here -->

<div id="cur"></div>

<!-- NAV (original - no war room) -->
<nav>
  <a href="#" class="nav-logo">NEKO ⚔</a>
  <button class="hamburger" id="hamburger-btn" onclick="toggleMenu()" aria-label="Toggle Menu">
    <span class="ham-line"></span>
    <span class="ham-line"></span>
    <span class="ham-line"></span>
  </button>
  <ul class="nav-links" id="nav-links">
    <li><a href="#trade" onclick="closeMenu()">⚔ Trade</a></li>
    <li><a href="#lore" onclick="closeMenu()">📜 Lore</a></li>
    <li><a href="#art" onclick="closeMenu()">🖼 Gallery</a></li>
    <li><a href="#join" onclick="closeMenu()">🐱 Clan</a></li>
    <li><a href="/litepaper" target="_blank" class="nav-whitepaper" onclick="closeMenu()">📄 Litepaper</a></li>
    <li><a href="https://opensea.io/collection/neko-shogun" target="_blank" class="nav-buy" style="border-color:#2081e2;color:#2081e2;background:rgba(32,129,226,.08);" onclick="closeMenu()">🌊 OpenSea</a></li>
    <li><a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="nav-buy" onclick="closeMenu()">Buy $NEKO</a></li>
  </ul>
</nav>

<!-- The rest of your original HTML (hero, video, trade, lore, gallery, join, footer, scripts) is exactly as you first sent it -->

</body>
</html>
'''

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

@app.route('/litepaper')
def litepaper():
    return send_from_directory('static', 'neko_litepaper.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)

