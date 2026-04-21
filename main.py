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

    /* NAV - Desktop original */
    nav {
      position: fixed; inset: 0 0 auto; z-index: 200;
      padding: 1rem 3rem;
      display: flex; align-items: center; justify-content: space-between;
      background: rgba(7,5,10,.97);
      border-bottom: 1px solid rgba(200,155,60,.2);
      backdrop-filter: blur(12px);
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

    .nav-buy, .nav-whitepaper {
      font-family: 'Shippori Mincho B1', serif !important;
      font-size: .8rem !important; letter-spacing: .15em !important;
      font-weight: 700 !important;
      padding: .5rem 1.4rem;
      border-radius: 2px;
      transition: all .25s !important;
    }
    .nav-buy {
      border: 1px solid var(--gold) !important;
      color: var(--gold-lt) !important;
      background: rgba(200,155,60,.08);
    }
    .nav-whitepaper {
      border: 1px solid rgba(200,155,60,.4) !important;
      color: var(--gold-dim) !important;
    }

    /* MOBILE SIMPLE BUTTONS */
    .mobile-nav {
      display: none;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      padding: 1rem;
      background: rgba(7,5,10,.97);
      border-bottom: 1px solid rgba(200,155,60,.3);
    }
    .mobile-nav a {
      font-family: 'Shippori Mincho B1', serif;
      font-size: 0.95rem;
      padding: 12px 20px;
      color: var(--cream);
      text-decoration: none;
      border: 1px solid rgba(200,155,60,.4);
      border-radius: 4px;
      text-align: center;
      min-width: 130px;
    }
    .mobile-nav a:hover {
      background: rgba(200,155,60,.15);
      border-color: var(--gold);
      color: var(--gold-lt);
    }

    /* Hide hamburger on mobile, show simple buttons */
    .hamburger { display: none; }

    /* RESPONSIVE */
    @media(max-width: 600px) {
      nav { display: none; } /* Hide original nav on mobile */
      .mobile-nav { display: flex; }
      #hero { padding-top: 160px; }
      .h-title { font-size:2.8rem; }
    }

    /* === ALL YOUR ORIGINAL STYLES === */
    #hero {
      min-height: 100vh;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center; padding: 7rem 2rem 5rem;
      position: relative; overflow: hidden;
    }
    .hero-glow {
      position: absolute; inset: 0; pointer-events: none;
      background:
        radial-gradient(ellipse 55% 65% at 50% 58%, rgba(122,0,18,.22) 0%, transparent 65%),
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
      0%   { transform:translateY(0) rotate(0deg) translateX(0); opacity:0; }
      8%   { opacity:1; }
      92%  { opacity:.7; }
      100% { transform:translateY(105vh) rotate(720deg) translateX(80px); opacity:0; }
    }

    .h-banner {
      width: min(480px, 88vw);
      margin: 0 auto 2.8rem;
      position: relative;
    }
    .h-banner img {
      width: 100%;
      height: auto;
      display: block;
      filter: saturate(.9) contrast(1.05);
      box-shadow: 0 0 80px rgba(176,16,32,.4), 0 0 160px rgba(122,0,18,.2);
    }

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
    .btn-fill { background:linear-gradient(130deg, var(--crimson), var(--red)); color:var(--cream); }
    .btn-ghost { background:rgba(200,155,60,.08); color:var(--gold-lt); border:1px solid var(--gold); }

    .sec-rule { width:100%; height:1px; background:linear-gradient(to right,transparent,rgba(200,155,60,.25),transparent); }
    #video-section { padding:4rem 4rem; text-align:center; background:var(--deep); }
    #trade { padding:8rem 4rem; position:relative; }
    #lore { padding:8rem 4rem; background:var(--deep); }
    #art { padding:8rem 4rem; background:var(--deep); }
    #join { padding:8rem 4rem; text-align:center; }
    footer { padding:3rem 4rem; border-top:1px solid rgba(200,155,60,.1); display:flex; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; gap:1.5rem; }

    @media(max-width:960px){
      nav { padding:1rem 1.5rem; }
      #trade,#lore,#join,#art,#video-section { padding:5rem 1.5rem; }
      .trade-cards { grid-template-columns:1fr; }
      .lore-inner { grid-template-columns:1fr; gap:3rem; }
      .clan-grid { grid-template-columns:1fr 1fr; }
      .gallery { grid-template-columns:1fr 1fr; }
      footer { flex-direction:column; text-align:center; }
    }
    @media(max-width:600px){
      #trade,#lore,#join,#art,#video-section { padding:4rem 1rem; }
      .gi { height:200px; }
    }
  </style>
</head>
<body>

<div id="cur"></div>

<!-- DESKTOP NAV (original) -->
<nav>
  <a href="#" class="nav-logo">NEKO ⚔</a>
  <ul class="nav-links" id="nav-links">
    <li><a href="#trade">⚔ Trade</a></li>
    <li><a href="#lore">📜 Lore</a></li>
    <li><a href="#art">🖼 Gallery</a></li>
    <li><a href="#join">🐱 Clan</a></li>
    <li><a href="/litepaper" target="_blank" class="nav-whitepaper">📄 Litepaper</a></li>
    <li><a href="https://opensea.io/collection/neko-shogun" target="_blank" class="nav-buy" style="border-color:#2081e2;color:#2081e2">🌊 OpenSea</a></li>
    <li><a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="nav-buy">Buy $NEKO</a></li>
  </ul>
</nav>

<!-- MOBILE SIMPLE STACKED BUTTONS -->
<div class="mobile-nav">
  <a href="#trade">⚔ Trade</a>
  <a href="#lore">📜 Lore</a>
  <a href="#art">🖼 Gallery</a>
  <a href="#join">🐱 Clan</a>
  <a href="/litepaper" target="_blank">📄 Litepaper</a>
  <a href="https://opensea.io/collection/neko-shogun" target="_blank">🌊 OpenSea</a>
  <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Buy $NEKO</a>
</div>

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

<div class="sec-rule"></div>

<!-- LORE -->
<section id="lore">
  <div class="lore-inner">
    <div class="lore-img reveal">
      <div class="lore-frame">
        <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" />
        <div class="lore-accent"></div>
      </div>
      <div class="lore-shadow"></div>
    </div>
    <div class="reveal d2">
      <span class="lore-kanji">前進</span>
      <p class="sec-label">⚔ &nbsp; The Legend</p>
      <h2 class="sec-title">Neko <em>Lore</em></h2>
      <div class="lore-hr"></div>
      <p class="lore-p">In the shadowed valleys of the Base chain, where cherry blossoms drift across digital winds, Neko emerged as the eternal leader of the Zenshin Clan — "Forward Progress" embodied. Zenshin is not just a name; it is the guiding principle: advance steadily, honorably, and without unnecessary haste.</p>
      <p class="lore-p">The Zenshin Clan are samurai cats sworn to Toshi the Emperor. Their oath is unbreakable: defend Toshi, safeguard the holders, protect the ecosystem, and preserve harmony no matter the threat. Neko leads with quiet ferocity — his katana ever-ready, his vision clear.</p>
      <p class="lore-p">Hold $NEKO. Walk with Neko. Join the Zenshin Clan. Forward progress awaits those who stand ready. <em style="color:var(--gold-dim)">Zenshin.</em></p>
      <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="btn-fill" style="display:inline-block;margin-top:2rem;">Join the Clan</a>
    </div>
  </div>
</section>

<div class="sec-rule"></div>

<!-- GALLERY -->
<section id="art">
  <div style="text-align:center;margin-bottom:4rem;">
    <p class="sec-label reveal">⚔ &nbsp; Clan Artwork</p>
    <h2 class="sec-title reveal d1">The <em>Gallery</em></h2>
  </div>
  <div class="gallery">
    <div class="gi reveal" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal d1" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal d2" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Clan Art" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal d3" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Clan Art" />
      <div class="gi-veil"></div>
    </div>
  </div>
</section>

<div class="sec-rule"></div>

<!-- JOIN -->
<section id="join">
  <div style="text-align:center;margin-bottom:4rem;">
    <p class="sec-label reveal">⚔ &nbsp; The Community</p>
    <h2 class="sec-title reveal d1">Join the <em>Clan</em></h2>
  </div>
  <div class="clan-grid">
    <a href="https://x.com/NekoTheSamurai" target="_blank" class="clan-card reveal d1">
      <div class="clan-icon">𝕏</div>
      <span class="clan-name">Follow on X</span>
      <span class="clan-handle">@NekoTheSamurai</span>
    </a>
    <a href="https://t.me/toshimart" target="_blank" class="clan-card reveal d2">
      <div class="clan-icon">✈️</div>
      <span class="clan-name">Telegram</span>
      <span class="clan-handle">Toshimart TG</span>
    </a>
    <a href="https://discord.gg/yKreTaD6Ua" target="_blank" class="clan-card reveal d3">
      <div class="clan-icon">🎮</div>
      <span class="clan-name">Discord</span>
      <span class="clan-handle">Neko Talk</span>
    </a>
    <a href="https://warpcast.com/toshibase" target="_blank" class="clan-card reveal d4">
      <div class="clan-icon">🟣</div>
      <span class="clan-name">Warpcast</span>
      <span class="clan-handle">Toshi Base</span>
    </a>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <span class="ft-brand">Neko ⚔ $NEKO</span>
  <div class="ft-meta">
    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Uniswap</a>
    &nbsp;·&nbsp;
    <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank" style="color:var(--gold-dim);">Dexscreener</a>
    &nbsp;·&nbsp;
    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" style="color:var(--gold-dim);">Toshimart</a>
    &nbsp;·&nbsp;
    <a href="/litepaper" target="_blank" style="color:var(--gold-dim);">Litepaper</a>
    <br />© 2026 Neko on Base &nbsp;·&nbsp; Last Update: {{ last_update }}
  </div>
  <p class="ft-disclaimer">$NEKO is a meme coin created for entertainment purposes only. It has no intrinsic value, makes no promises of financial return, and should not be considered an investment. Cryptocurrency trading involves significant risk. Always do your own research (DYOR) before making any financial decisions. Not financial advice.</p>
</footer>

<!-- LIGHTBOX -->
<div id="lightbox" onclick="closeLightbox()" style="display:none;position:fixed;inset:0;z-index:9998;background:rgba(7,5,10,.95);align-items:center;justify-content:center;cursor:none;">
  <div style="position:relative;max-width:90vw;max-height:90vh;">
    <img id="lightbox-img" src="" style="max-width:90vw;max-height:85vh;object-fit:contain;border:1px solid rgba(200,155,60,.3);box-shadow:0 0 80px rgba(122,0,18,.4);" />
    <a id="lightbox-save" download="neko-art.jpg" style="display:block;margin-top:1rem;text-align:center;font-family:'Shippori Mincho B1',serif;font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);text-decoration:none;">⬇ Save Image</a>
    <p style="text-align:center;font-size:.7rem;color:var(--muted);margin-top:.5rem;font-family:'Shippori Mincho B1',serif;letter-spacing:.15em;">Click anywhere to close</p>
  </div>
</div>

<script>
  /* CURSOR */
  const cur = document.getElementById('cur');
  document.addEventListener('mousemove', e => {
    cur.style.left = e.clientX + 'px';
    cur.style.top  = e.clientY + 'px';
  });
  document.querySelectorAll('a,button,.ca-pill,.tc,.clan-card,.gi').forEach(el => {
    el.addEventListener('mouseenter', () => cur.classList.add('big'));
    el.addEventListener('mouseleave', () => cur.classList.remove('big'));
  });

  /* SAKURA */
  const container = document.getElementById('sakura');
  for (let i = 0; i < 35; i++) {
    const p = document.createElement('div');
    p.className = 'petal';
    const size = 6 + Math.random() * 10;
    p.style.cssText = `left:${Math.random()*100}%; width:${size}px; height:${size*1.4}px; animation-duration:${7+Math.random()*10}s; animation-delay:${Math.random()*15}s;`;
    container.appendChild(p);
  }

  /* COPY CA */
  function copyCA() {
    navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453').then(() => {
      const ok = document.getElementById('ca-ok');
      ok.classList.add('on');
      setTimeout(() => ok.classList.remove('on'), 2200);
    });
  }

  /* LIGHTBOX */
  function openLightbox(src) {
    const lb = document.getElementById('lightbox');
    const img = document.getElementById('lightbox-img');
    const save = document.getElementById('lightbox-save');
    img.src = src;
    save.href = src;
    lb.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox() {
    document.getElementById('lightbox').style.display = 'none';
    document.body.style.overflow = '';
  }
</script>

<!-- CHATBOT -->
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
