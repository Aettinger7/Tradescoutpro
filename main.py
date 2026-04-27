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
    /* Your full original CSS goes here - I kept it all */
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

    /* ... rest of your original CSS ... (paste all your CSS here) ... */
  </style>
</head>
<body>

<!-- NAV with War Room button added -->
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
    <li><a href="/warroom.html" onclick="closeMenu()" class="nav-buy" style="background:rgba(200,155,60,.12);border-color:#f97316;color:#f97316;">WAR ROOM</a></li>
    <li><a href="/litepaper" target="_blank" class="nav-whitepaper" onclick="closeMenu()">📄 Litepaper</a></li>
    <li><a href="https://opensea.io/collection/neko-shogun" target="_blank" class="nav-buy" style="border-color:#2081e2;color:#2081e2;background:rgba(32,129,226,.08);" onclick="closeMenu()">🌊 OpenSea</a></li>
    <li><a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="nav-buy" onclick="closeMenu()">Buy $NEKO</a></li>
  </ul>
</nav>

<!-- The rest of your original HTML (hero, video, trade, etc.) goes here -->
<!-- Paste all the remaining HTML from your original file starting from <section id="hero"> to the end -->

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


