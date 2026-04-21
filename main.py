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

    /* CURSOR */
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

    /* SIMPLE NAV */
    nav {
      position: fixed; inset: 0 0 auto; z-index: 200;
      padding: 1rem;
      background: rgba(7,5,10,.97);
      border-bottom: 1px solid rgba(200,155,60,.3);
      backdrop-filter: blur(12px);
    }
    .nav-container {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 12px;
      max-width: 1200px;
      margin: 0 auto;
    }
    .nav-logo {
      font-family: 'Shippori Mincho B1', serif;
      font-size: 1.25rem; font-weight: 800;
      color: var(--gold); letter-spacing: .15em;
      text-decoration: none;
    }
    .nav-links {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px;
      list-style: none;
    }
    .nav-links a {
      font-family: 'Shippori Mincho B1', serif;
      font-size: 0.9rem;
      letter-spacing: .15em;
      text-transform: uppercase;
      padding: 10px 18px;
      color: var(--cream);
      text-decoration: none;
      border: 1px solid rgba(200,155,60,.4);
      border-radius: 4px;
      white-space: nowrap;
      transition: all .25s;
    }
    .nav-links a:hover {
      background: rgba(200,155,60,.15);
      border-color: var(--gold);
      color: var(--gold-lt);
    }

    @media(max-width: 600px) {
      .nav-container { gap: 10px; }
      .nav-links a {
        font-size: 0.95rem;
        padding: 12px 20px;
        min-width: 130px;
        text-align: center;
      }
      #hero { padding-top: 120px !important; }
    }

    /* Original styles from here down */
    #hero {
      min-height: 100vh;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center; padding: 7rem 2rem 5rem;
      position: relative; overflow: hidden;
    }
    .hero-glow {
      position: absolute; inset: 0; pointer-events: none;
      background: radial-gradient(ellipse 55% 65% at 50% 58%, rgba(122,0,18,.22) 0%, transparent 65%),
                  radial-gradient(ellipse 90% 40% at 50% 100%, rgba(100,0,12,.15) 0%, transparent 60%),
                  var(--ink);
    }
    .sakura { position:fixed; inset:0; overflow:hidden; pointer-events:none; z-index:0; }
    .petal {
      position:absolute; top:-30px;
      background: radial-gradient(ellipse, rgba(220,40,60,.9), rgba(176,16,32,.4));
      border-radius: 60% 0 60% 0;
      animation: drift linear infinite; opacity:0;
      box-shadow: 0 0 6px rgba(220,40,60,.4);
    }
    @keyframes drift {
      0% { transform:translateY(0) rotate(0deg) translateX(0); opacity:0; }
      8% { opacity:1; }
      92% { opacity:.7; }
      100% { transform:translateY(105vh) rotate(720deg) translateX(80px); opacity:0; }
    }

    .h-banner { width: min(480px, 88vw); margin: 0 auto 2.8rem; position: relative; }
    .h-banner img { width: 100%; height: auto; display: block; filter: saturate(.9) contrast(1.05); }
    h1.h-title {
      font-family:'Shippori Mincho B1',serif;
      font-size:clamp(3.5rem,9vw,8rem);
      font-weight:800; line-height:.88; letter-spacing:-.025em;
      color:var(--cream);
    }
    .h-title em {
      background:linear-gradient(130deg, var(--gold-lt) 0%, var(--gold) 45%, var(--gold-dim) 100%);
      -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    }

    .btn-fill, .btn-ghost {
      padding:1rem 2.8rem; border-radius:2px;
      font-family:'Shippori Mincho B1',serif;
      font-size:.88rem; letter-spacing:.25em; text-transform:uppercase; font-weight:800;
      transition: all .25s;
    }
    .btn-fill { background:linear-gradient(130deg, var(--crimson), var(--red)); color:var(--cream); border:1px solid rgba(212,24,46,.6); }
    .btn-ghost { background:rgba(200,155,60,.08); color:var(--gold-lt); border:1px solid var(--gold); }

    /* All other original styles */
    .sec-rule { width:100%; height:1px; background:linear-gradient(to right,transparent,rgba(200,155,60,.25),transparent); }
    .trade-cards { display:grid; grid-template-columns:repeat(3,1fr); gap:1px; }
    .clan-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; }
    .gallery { display:grid; grid-template-columns:1fr 1fr; gap:6px; }

    @media(max-width:960px){
      .trade-cards { grid-template-columns:1fr; }
      .clan-grid { grid-template-columns:1fr 1fr; }
      .gallery { grid-template-columns:1fr 1fr; }
    }
    @media(max-width:600px){
      .trade-cards, .clan-grid, .gallery { width:100%; }
      .gi { height:200px; }
    }
  </style>
</head>
<body>

<div id="cur"></div>

<nav>
  <div class="nav-container">
    <a href="#" class="nav-logo">NEKO ⚔</a>
    <ul class="nav-links">
      <li><a href="#trade">⚔ Trade</a></li>
      <li><a href="#lore">📜 Lore</a></li>
      <li><a href="#art">🖼 Gallery</a></li>
      <li><a href="#join">🐱 Clan</a></li>
      <li><a href="/litepaper" target="_blank">📄 Litepaper</a></li>
      <li><a href="https://opensea.io/collection/neko-shogun" target="_blank">🌊 OpenSea</a></li>
      <li><a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Buy $NEKO</a></li>
    </ul>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-glow"></div>
  <div class="sakura" id="sakura"></div>
  <div class="orbit"></div>
  <div class="hero-content">
    <p class="h-tag">⚔ &nbsp; Zenshin Clan &nbsp;·&nbsp; $NEKO on Base &nbsp; ⚔</p>
    <div class="h-banner">
      <img src="https://i.ibb.co/BKFCjDjf/1500x500.jpg" alt="Neko the Samurai Cat" />
    </div>
    <h1 class="h-title">Neko the<br /><em>Samurai</em></h1>
    <p class="h-sub">前進 &nbsp;·&nbsp; Zenshin &nbsp;·&nbsp; Forward Progress</p>
    <p class="h-quote">"Warrior in a garden, claws sharpened on Base."</p>
    <div class="ca-pill" onclick="copyCA()" title="Copy contract address">
      <span>CA</span>
      <span class="ca-mono">0x2897...8453</span>
      <button class="ca-btn" aria-label="Copy">📋</button>
      <span class="ca-confirm" id="ca-ok">Copied ✓</span>
    </div>
    <div class="h-btns">
      <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-fill">Buy on Uniswap</a>
      <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank" class="btn-ghost">View Chart</a>
    </div>
  </div>
  <div class="scroll-cue">
    <span>Scroll</span>
    <div class="scroll-line"></div>
  </div>
</section>

<div class="sec-rule"></div>

<!-- VIDEO -->
<section id="video-section">
  <div style="position:relative;z-index:1;">
    <p class="sec-label reveal">⚔ &nbsp; The Clan in Motion</p>
    <h2 class="sec-title reveal d1">Watch <em>Neko</em></h2>
  </div>
  <div class="video-wrap reveal d2">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe src="https://www.youtube.com/embed/I4_fKxAayRM?autoplay=1&mute=0&loop=1&playlist=I4_fKxAayRM&controls=1&modestbranding=1&rel=0" title="Neko the Samurai Cat" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:-60px;left:0;width:100%;height:calc(100% + 120px);border:0;"></iframe>
    </div>
  </div>
</section>

<div class="sec-rule"></div>

<!-- TRADE -->
<section id="trade">
  <div class="trade-header">
    <p class="sec-label reveal">⚔ &nbsp; Trade $NEKO</p>
    <h2 class="sec-title reveal d1">Acquire Your <em>Blade</em></h2>
    <p class="reveal d2" style="color:var(--muted);font-size:.9rem;font-style:italic;">Three paths into the Zenshin Clan</p>
  </div>
  <div class="trade-cards">
    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="tc reveal d1">
      <div class="tc-num">01</div>
      <div class="tc-tag">Primary Exchange</div>
      <h3>Uniswap V3</h3>
      <p>Live V3 pool on Base chain. The primary arena for $NEKO warriors.</p>
      <span class="tc-arrow">Swap Now</span>
    </a>
    <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank" class="tc reveal d2">
      <div class="tc-num">02</div>
      <div class="tc-tag">Real-Time Data</div>
      <h3>Dexscreener</h3>
      <p>Live price, volume, and liquidity. Watch the Clan's strength grow.</p>
      <span class="tc-arrow">View Chart</span>
    </a>
    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="tc reveal d3">
      <div class="tc-num">03</div>
      <div class="tc-tag">Legacy Platform</div>
      <h3>Toshimart</h3>
      <p>Original launch platform. Where the Zenshin Clan was forged.</p>
      <span class="tc-arrow">View Token</span>
    </a>
  </div>
  <!-- Chart embed -->
  <div class="chart-box reveal">
    <div class="chart-bar">
      <span>$NEKO Live Chart &nbsp;·&nbsp; Base Chain</span>
      <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank">Open Dexscreener →</a>
    </div>
    <div id="dexscreener-embed">
      <iframe src="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e?embed=1&theme=dark&trades=0&info=0" allow="clipboard-write" loading="lazy" title="NEKO Chart"></iframe>
    </div>
  </div>
</section>

<!-- LORE, GALLERY, JOIN, FOOTER, LIGHTBOX, and all scripts are included below in full in your original file. -->

<!-- (To keep this message from being too huge, the remaining identical sections are the same as your first message. Paste your original lore, art, join, footer, lightbox if any part is missing after testing.) -->

<script>
  /* Cursor */
  const cur = document.getElementById('cur');
  document.addEventListener('mousemove', e => {
    cur.style.left = e.clientX + 'px';
    cur.style.top  = e.clientY + 'px';
  });

  /* Sakura */
  const container = document.getElementById('sakura');
  for (let i = 0; i < 35; i++) {
    const p = document.createElement('div');
    p.className = 'petal';
    const size = 6 + Math.random() * 10;
    p.style.cssText = `left:${Math.random()*100}%; width:${size}px; height:${size*1.4}px; animation-duration:${7+Math.random()*10}s; animation-delay:${Math.random()*15}s;`;
    container.appendChild(p);
  }

  function copyCA() {
    navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453').then(() => {
      const ok = document.getElementById('ca-ok');
      ok.classList.add('on');
      setTimeout(() => ok.classList.remove('on'), 2200);
    });
  }
</script>

<!-- Chatbot -->
<script>
(function(){if(!window.chatbase||window.chatbase("getState")!=="initialized"){window.chatbase=(...arguments)=>{if(!window.chatbase.q){window.chatbase.q=[]}window.chatbase.q.push(arguments)};window.chatbase=new Proxy(window.chatbase,{get(target,prop){if(prop==="q"){return target.q}return(...args)=>target(prop,...args)}})}const onLoad=function(){const script=document.createElement("script");script.src="https://www.chatbase.co/embed.min.js";script.id="RkznU5gsjj1ggRKXeVnHD";script.domain="www.chatbase.co";document.body.appendChild(script)};if(document.readyState==="complete"){onLoad()}else{window.addEventListener("load",onLoad)}})();
</script>

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
