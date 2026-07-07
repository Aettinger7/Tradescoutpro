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

    /* ── ADDED FOR FIXED BACKGROUND ── */
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      min-height: 100vh;
      overflow-x: hidden;
    }

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

    /* ── BACKGROUND IMAGE ── */
#bg-img {
  position: fixed;           /* This should stay */
  inset: 0;                  /* Covers full viewport */
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;             /* Important */
  background-image: url('/neko-bg.jpg');
  background-size: 75%;      /* You can change to 'cover' if you want it bigger */
  background-repeat: no-repeat;
  background-position: center center;
  opacity: 0.35;
  mix-blend-mode: luminosity;
  pointer-events: none;
  z-index: -1;               /* Better to use -1 so it's behind everything */
  overflow: hidden;
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

    /* ── HERO ── */
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
    .hero-glow::before {
      content:''; position:absolute; inset:0;
      background: radial-gradient(ellipse 35% 35% at 50% 52%, rgba(176,16,32,.08) 0%, transparent 70%);
      animation: breathe 5s ease-in-out infinite;
    }
    @keyframes breathe { 0%,100%{opacity:.4;transform:scale(1)} 50%{opacity:1;transform:scale(1.08)} }

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

    .orbit {
      position:absolute; top:50%; left:50%;
      transform:translate(-50%,-50%);
      width:min(800px,90vw); height:min(800px,90vw);
      border-radius:50%; border:1px solid rgba(200,155,60,.05);
      animation:spin 50s linear infinite; pointer-events:none;
    }
    .orbit::before { content:''; position:absolute; inset:28px; border-radius:50%; border:1px solid rgba(200,155,60,.03); }
    @keyframes spin { to { transform:translate(-50%,-50%) rotate(360deg); } }

    .hero-content { position:relative; z-index:2; }
    .h-tag {
      font-family:'Shippori Mincho B1',serif;
      font-size:.82rem; letter-spacing:.35em; text-transform:uppercase;
      color:var(--gold); margin-bottom:2rem; font-weight:700;
      opacity:0; animation:rise .8s .15s forwards;
    }

    .h-banner {
      width: min(480px, 88vw);
      margin: 0 auto 2.8rem;
      position: relative;
      opacity: 0;
      animation: rise .9s .35s forwards;
    }
    .h-banner::before {
      content: '';
      position: absolute;
      inset: -1px;
      border: 1px solid rgba(200,155,60,.35);
      pointer-events: none;
      z-index: 1;
    }
    .h-banner::after {
      content: '';
      position: absolute;
      inset: -8px;
      border: 1px solid rgba(200,155,60,.12);
      pointer-events: none;
    }
    .h-banner img {
      width: 100%;
      height: auto;
      display: block;
      object-fit: cover;
      filter: saturate(.9) contrast(1.05);
      box-shadow: 0 0 80px rgba(176,16,32,.4), 0 0 160px rgba(122,0,18,.2);
    }

    h1.h-title {
      font-family:'Shippori Mincho B1',serif;
      font-size:clamp(3.5rem,9vw,8rem);
      font-weight:800; line-height:.88; letter-spacing:-.025em;
      color:var(--cream); margin-bottom:.55rem;
      opacity:0; animation:rise .9s .55s forwards;
    }
    h1.h-title em {
      font-style:normal;
      background:linear-gradient(130deg, var(--gold-lt) 0%, var(--gold) 45%, var(--gold-dim) 100%);
      -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    }
    .h-sub {
      font-family:'Shippori Mincho B1',serif; font-weight:700;
      font-size:clamp(.85rem,1.6vw,1.05rem); letter-spacing:.4em; text-transform:uppercase;
      color:var(--gold-lt); margin-bottom:.9rem;
      opacity:0; animation:rise .9s .7s forwards;
    }
    .h-quote {
      font-family:'Noto Serif JP',serif; font-size:clamp(1rem,1.9vw,1.2rem);
      font-style:italic; color:rgba(237,228,204,.75); margin-bottom:2.8rem; font-weight:400;
      opacity:0; animation:rise .9s .82s forwards;
    }
    .ca-pill {
      display:inline-flex; align-items:center; gap:.7rem;
      border:1px solid rgba(200,155,60,.18); background:rgba(255,255,255,.02);
      border-radius:3px; padding:.55rem 1.3rem;
      font-size:.68rem; letter-spacing:.1em; color:var(--muted);
      margin-bottom:2.6rem; transition:border-color .25s, color .25s;
      opacity:0; animation:rise .9s .95s forwards;
    }
    .ca-pill:hover { border-color:var(--gold); color:var(--gold-lt); }
    .ca-mono { font-family:monospace; font-size:.62rem; }
    .ca-btn { background:none; border:none; padding:0; font-size:.8rem; color:var(--gold-dim); transition:color .2s; }
    .ca-btn:hover { color:var(--gold); }
    .ca-confirm { font-size:.62rem; color:var(--gold); opacity:0; transition:opacity .3s; }
    .ca-confirm.on { opacity:1; }
    .h-btns {
      display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;
      opacity:0; animation:rise .9s 1.05s forwards;
    }
    .btn-fill {
      background:linear-gradient(130deg, var(--crimson), var(--red));
      color:var(--cream); text-decoration:none;
      padding:1rem 2.8rem; border-radius:2px;
      font-family:'Shippori Mincho B1',serif;
      font-size:.88rem; letter-spacing:.25em; text-transform:uppercase; font-weight:800;
      box-shadow:0 4px 32px rgba(176,16,32,.5), inset 0 1px 0 rgba(255,255,255,.1);
      border:1px solid rgba(212,24,46,.6);
      position:relative; overflow:hidden; transition:box-shadow .3s, transform .2s;
    }
    .btn-fill::before { content:''; position:absolute; inset:0; background:linear-gradient(130deg,rgba(255,255,255,.1),transparent); opacity:0; transition:opacity .25s; }
    .btn-fill:hover { box-shadow:0 8px 48px rgba(176,16,32,.7); transform:translateY(-3px); }
    .btn-fill:hover::before { opacity:1; }
    .btn-ghost {
      background:rgba(200,155,60,.08); color:var(--gold-lt); text-decoration:none;
      padding:1rem 2.8rem; border-radius:2px;
      font-family:'Shippori Mincho B1',serif;
      border:1px solid var(--gold);
      font-size:.88rem; letter-spacing:.25em; text-transform:uppercase; font-weight:800;
      box-shadow:0 0 20px rgba(200,155,60,.15);
      transition:background .25s, box-shadow .25s, transform .2s;
    }
    .btn-ghost:hover { background:rgba(200,155,60,.18); box-shadow:0 0 40px rgba(200,155,60,.3); transform:translateY(-3px); }

    .scroll-cue {
      position:absolute; bottom:2rem; left:50%; transform:translateX(-50%);
      display:flex; flex-direction:column; align-items:center; gap:.5rem;
      opacity:0; animation:rise 1s 1.6s forwards; z-index:2;
    }
    .scroll-cue span { font-size:.58rem; letter-spacing:.35em; text-transform:uppercase; color:var(--gold-dim); }
    .scroll-line { width:1px; height:38px; background:linear-gradient(to bottom,var(--gold-dim),transparent); animation:pulse-line 2.2s ease-in-out infinite; }
    @keyframes pulse-line { 0%,100%{opacity:.3} 50%{opacity:1} }
    @keyframes rise { from{opacity:0;transform:translateY(24px)} to{opacity:1;transform:translateY(0)} }

    /* ── SHARED ── */
    .sec-rule { width:100%; height:1px; background:linear-gradient(to right,transparent,rgba(200,155,60,.25),transparent); }
    .sec-label {
      font-family:'Shippori Mincho B1',serif;
      font-size:.78rem; letter-spacing:.35em; text-transform:uppercase;
      color:var(--gold); margin-bottom:1rem; font-weight:700;
    }
    h2.sec-title {
      font-family:'Shippori Mincho B1',serif;
      font-size:clamp(2.6rem,5.5vw,4.5rem);
      font-weight:800; color:var(--cream); letter-spacing:-.01em; margin-bottom:.5rem;
    }
    h2.sec-title em { font-style:normal; color:var(--gold); }
    .reveal { opacity:0; transform:translateY(40px); transition:opacity .9s cubic-bezier(.16,1,.3,1), transform .9s cubic-bezier(.16,1,.3,1); }
    .reveal.in { opacity:1; transform:translateY(0); }
    .reveal-left { opacity:0; transform:translateX(-60px); transition:opacity .9s cubic-bezier(.16,1,.3,1), transform .9s cubic-bezier(.16,1,.3,1); }
    .reveal-left.in { opacity:1; transform:translateX(0); }
    .reveal-right { opacity:0; transform:translateX(60px); transition:opacity .9s cubic-bezier(.16,1,.3,1), transform .9s cubic-bezier(.16,1,.3,1); }
    .reveal-right.in { opacity:1; transform:translateX(0); }
    .reveal-scale { opacity:0; transform:scale(.88); transition:opacity .9s cubic-bezier(.16,1,.3,1), transform .9s cubic-bezier(.16,1,.3,1); }
    .reveal-scale.in { opacity:1; transform:scale(1); }
    .d1{transition-delay:.08s} .d2{transition-delay:.18s} .d3{transition-delay:.28s} .d4{transition-delay:.38s} .d5{transition-delay:.48s}

    /* ── VIDEO ── */
    #video-section { padding:4rem 4rem; text-align:center; background:var(--deep); position:relative; }
    #video-section::before {
      content:''; position:absolute; inset:0;
      background:radial-gradient(ellipse 60% 70% at 50% 50%, rgba(122,0,18,.13) 0%,transparent 70%);
      pointer-events:none;
    }
    .video-wrap {
      max-width:680px; margin:2rem auto 0; position:relative;
      border:1px solid rgba(200,155,60,.18);
      box-shadow:0 0 60px rgba(122,0,18,.2), 0 0 120px rgba(122,0,18,.08);
    }
    .video-wrap::before {
      content:''; position:absolute; top:-1px; left:0; right:0; height:2px;
      background:linear-gradient(to right, transparent, var(--gold), transparent);
    }
    .video-wrap::after {
      content:''; position:absolute; bottom:-1px; left:0; right:0; height:2px;
      background:linear-gradient(to right, transparent, var(--crimson), transparent);
    }

    /* ── TRADE ── */
    #trade { padding:8rem 4rem; position:relative; }
    #trade::after {
      content:''; position:absolute; top:0; right:0;
      width:500px; height:500px;
      background:radial-gradient(ellipse,rgba(122,0,18,.09) 0%,transparent 70%);
      pointer-events:none;
    }
    .trade-header { text-align:center; margin-bottom:4rem; }
    .trade-cards {
      display:grid; grid-template-columns:repeat(3,1fr);
      max-width:1000px; margin:0 auto;
      gap:1px; background:rgba(200,155,60,.1);
      border:1px solid rgba(200,155,60,.1);
    }
    .tc {
      background:var(--panel); padding:2.8rem 2.2rem;
      text-decoration:none; display:block;
      position:relative; overflow:hidden;
      transition:background .3s, box-shadow .3s;
    }
    .tc::before {
      content:''; position:absolute; top:0; left:0; right:0; height:3px;
      background:linear-gradient(to right, var(--crimson), var(--gold));
      opacity:0; transition:opacity .3s;
    }
    .tc::after {
      content:''; position:absolute; inset:0;
      background:radial-gradient(ellipse 80% 60% at 50% 100%, rgba(122,0,18,.12) 0%, transparent 70%);
      opacity:0; transition:opacity .4s;
    }
    .tc:hover { background:rgba(122,0,18,.15); box-shadow:inset 0 0 60px rgba(122,0,18,.15); }
    .tc:hover::before { opacity:1; }
    .tc:hover::after { opacity:1; }
    .tc-num { font-family:'Shippori Mincho B1',serif; font-size:3rem; font-weight:800; color:rgba(200,155,60,.12); line-height:1; margin-bottom:.4rem; }
    .tc-tag { font-family:'Shippori Mincho B1',serif; font-size:.72rem; letter-spacing:.28em; text-transform:uppercase; color:var(--gold); margin-bottom:.5rem; font-weight:700; }
    .tc h3 { font-family:'Shippori Mincho B1',serif; font-size:1.45rem; font-weight:800; color:var(--cream); margin-bottom:.5rem; }
    .tc p { font-size:.88rem; color:rgba(237,228,204,.7); line-height:1.7; margin-bottom:1.6rem; }
    .tc-arrow { font-family:'Shippori Mincho B1',serif; font-size:.78rem; letter-spacing:.22em; text-transform:uppercase; color:var(--gold); font-weight:700; }
    .tc-arrow::after { content:' →'; display:inline-block; transition:margin .2s; }
    .tc:hover .tc-arrow::after { margin-left:5px; }
    .chart-box { max-width:1000px; margin:2.5rem auto 0; border:1px solid rgba(200,155,60,.1); background:var(--panel); overflow:hidden; }
    .chart-bar { padding:.9rem 1.4rem; border-bottom:1px solid rgba(200,155,60,.08); display:flex; align-items:center; justify-content:space-between; }
    .chart-bar span { font-family:'Shippori Mincho B1',serif; font-size:.65rem; letter-spacing:.22em; text-transform:uppercase; color:var(--gold-dim); font-weight:700; }
    .chart-bar a { font-size:.65rem; color:var(--gold); text-decoration:none; }
    .chart-bar a:hover { color:var(--gold-lt); }
    #dexscreener-embed { position:relative; padding-bottom:56.25%; }
    #dexscreener-embed iframe { position:absolute; inset:0; width:100%; height:100%; border:0; }

    /* ── LORE ── */
    #lore { padding:8rem 4rem; background:var(--deep); }
    #lore::before {
      content:''; position:absolute; inset:0;
      background:radial-gradient(ellipse 65% 55% at 15% 50%, rgba(122,0,18,.1) 0%,transparent 65%);
      pointer-events:none;
    }
    .lore-inner { max-width:1120px; margin:0 auto; display:grid; grid-template-columns:1fr 1fr; gap:5rem; align-items:center; position:relative; z-index:1; }
    .lore-img { position:relative; }
    .lore-frame { position:relative; width:100%; aspect-ratio:3/4; overflow:hidden; }
    .lore-frame::after { content:''; position:absolute; inset:0; background:linear-gradient(to top,rgba(15,11,20,.85) 0%,transparent 55%); }
    .lore-frame img { width:100%; height:100%; object-fit:cover; display:block; filter:saturate(.65) contrast(1.1); transition:transform 7s ease, filter .5s; }
    .lore-frame:hover img { transform:scale(1.05); filter:saturate(.9) contrast(1.1); }
    .lore-accent { position:absolute; bottom:0; left:0; right:0; height:3px; background:linear-gradient(to right, var(--crimson), var(--gold-dim)); }
    .lore-shadow { position:absolute; top:18px; left:18px; right:-18px; bottom:-18px; border:1px solid rgba(200,155,60,.12); z-index:-1; }
    .lore-kanji { font-family:'Noto Serif JP',serif; font-weight:200; font-size:5.5rem; color:rgba(200,155,60,.1); line-height:1; margin-bottom:-1.4rem; display:block; }
    .lore-hr { width:56px; height:1px; background:linear-gradient(to right,var(--crimson),var(--gold-dim)); margin:1.5rem 0; }
    .lore-p { font-size:.95rem; line-height:2; color:rgba(237,228,204,.8); margin-bottom:1.2rem; }
    .lore-p:first-of-type { color:var(--cream); font-size:1rem; }

    /* ── GALLERY ── */
    #art { padding:8rem 4rem; background:var(--deep); }
    #art::after {
      content:''; position:absolute; bottom:0; left:0;
      width:500px; height:350px;
      background:radial-gradient(ellipse,rgba(122,0,18,.08) 0%,transparent 70%);
      pointer-events:none;
    }
    .gallery { display:grid; grid-template-columns:1fr 1fr; gap:6px; max-width:1120px; margin:0 auto; }
    .gi { overflow:hidden; position:relative; background:var(--panel); height:380px; }
    .gi img { width:100%; height:100%; object-fit:cover; display:block; filter:saturate(.7) contrast(1.05); transition:transform .7s ease, filter .4s; }
    .gi:hover img { transform:scale(1.06); filter:saturate(1) contrast(1.05); }
    .gi-veil { position:absolute; inset:0; background:linear-gradient(to top,rgba(7,5,10,.65) 0%,transparent 55%); opacity:0; transition:opacity .4s; }
    .gi:hover .gi-veil { opacity:1; }

    /* ── COMMUNITY ── */
    #join { padding:8rem 4rem; text-align:center; }
    .clan-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:rgba(200,155,60,.09); max-width:920px; margin:0 auto; }
    .clan-card {
      background:var(--ink); padding:2.8rem 1.5rem;
      text-decoration:none; display:flex; flex-direction:column; align-items:center; gap:1.1rem;
      position:relative; overflow:hidden;
      transition:background .3s, box-shadow .3s;
      border:1px solid rgba(200,155,60,.1);
    }
    .clan-card::after { content:''; position:absolute; bottom:0; left:0; right:0; height:3px; background:linear-gradient(to right, var(--crimson), var(--gold)); transform:scaleX(0); transition:transform .35s; }
    .clan-card:hover { background:rgba(200,155,60,.06); box-shadow:0 0 40px rgba(200,155,60,.1); }
    .clan-card:hover::after { transform:scaleX(1); }
    .clan-icon { width:60px; height:60px; border-radius:50%; border:1px solid rgba(200,155,60,.3); display:flex; align-items:center; justify-content:center; font-size:1.6rem; background:rgba(200,155,60,.05); transition:border-color .3s, box-shadow .3s, transform .3s; }
    .clan-card:hover .clan-icon { border-color:var(--gold); box-shadow:0 0 30px rgba(200,155,60,.3); transform:scale(1.1); }
    .clan-name { font-family:'Shippori Mincho B1',serif; font-size:1.1rem; font-weight:800; color:var(--cream); }
    .clan-handle { font-family:'Shippori Mincho B1',serif; font-size:.78rem; color:var(--gold); font-weight:700; letter-spacing:.08em; }

    /* ── FOOTER ── */
    footer { padding:3rem 4rem; border-top:1px solid rgba(200,155,60,.1); display:flex; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; gap:1.5rem; }
    .ft-brand { font-family:'Shippori Mincho B1',serif; font-size:1.2rem; font-weight:800; color:var(--gold); }
    .ft-meta { font-family:'Shippori Mincho B1',serif; font-size:.8rem; color:var(--cream); line-height:1.8; font-weight:700; }
    .ft-meta a { color:var(--gold); text-decoration:none; }
    .ft-meta a:hover { color:var(--gold-lt); }
    .ft-disclaimer { font-size:.72rem; color:rgba(200,155,60,.5); max-width:480px; line-height:1.7; font-family:'Zen Kaku Gothic New',sans-serif; }

    /* RESPONSIVE */
    @media(max-width:960px){
      nav { padding:1rem 1.5rem; }
      #trade,#lore,#join,#art,#video-section { padding:5rem 1.5rem; }
      .trade-cards { grid-template-columns:1fr; }
      .lore-inner { grid-template-columns:1fr; gap:3rem; }
      .lore-img { max-width:380px; margin:0 auto; }
      .lore-shadow { display:none; }
      .clan-grid { grid-template-columns:1fr 1fr; }
      .gallery { grid-template-columns:1fr 1fr; }
      footer { flex-direction:column; text-align:center; }
      .ft-disclaimer { max-width:100%; }
      #trade::after, #art::after { display:none; }
    }
    @media(max-width:600px){
      html, body { overflow-x:hidden !important; }
      * { max-width: 100%; }
      nav { padding:.9rem 1rem; }
      .nav-links {
        display: none;
        flex-direction: column;
        position: fixed;
        top: 62px; left: 0; right: 0;
        background: rgba(7,5,10,.98);
        padding: 1.5rem 2rem;
        gap: 0;
        z-index: 199;
        border-bottom: 1px solid rgba(200,155,60,.2);
        list-style: none;
      }
      .nav-links.open { display: flex; }
      .nav-links li { width: 100%; }
      .nav-links a {
        display: block;
        font-size: .9rem !important;
        letter-spacing: .12em !important;
        padding: .9rem 0 !important;
        border-bottom: 1px solid rgba(200,155,60,.08) !important;
        color: var(--cream) !important;
      }
      .nav-links li:last-child a { border-bottom: none !important; }
      .hamburger { display: flex !important; }
      #cur { display: none; }
      h1.h-title { font-size:2.8rem; }
      .h-banner { width: min(320px, 92vw); }
      .h-btns { flex-direction:column; align-items:center; }
      .btn-fill, .btn-ghost { width:100%; max-width:280px; text-align:center; }
      #trade,#lore,#join,#art,#video-section { padding:4rem 1rem; }
      .tc { padding:2rem 1.5rem; }
      .lore-inner { gap:2rem; }
      .lore-kanji { font-size:3.5rem; }
      .lore-shadow { display:none; }
      .clan-grid { grid-template-columns:1fr 1fr; gap:1px; width:100%; }
      .clan-card { padding:2rem 1rem; }
      .clan-icon { width:48px; height:48px; font-size:1.3rem; }
      .gallery { grid-template-columns:1fr 1fr; gap:4px; width:100%; }
      .gi { height:200px; }
      #dexscreener-embed { padding-bottom:75%; }
      .trade-cards, .chart-box { width:100%; }
      footer { padding:2rem 1rem; }
      .ca-pill { max-width:90vw; overflow:hidden; }
      .ca-mono { font-size:.55rem; }
      #trade::after, #art::after { display:none; }
    }
    @media(max-width:380px){
      h1.h-title { font-size:2.4rem; }
    }
  </style>
</head>
<body>

<div id="bg-img"></div>
<div id="bg-overlay"></div>

<div id="cur"></div>

<!-- NAV -->
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
    <li><a href="https://neko-the-samurai-shop.fourthwall.com/" target="_blank" rel="noopener noreferrer" class="nav-buy" style="border-color:#c89b3c;color:#e8c06a;background:rgba(200,155,60,.08);" onclick="closeMenu()">🛍️ Merch</a></li>
</li>
    <li><a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="nav-buy" onclick="closeMenu()">Buy $NEKO</a></li>
  </ul>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-glow"></div>
  <div class="sakura" id="sakura"></div>
  <div class="orbit"></div>
  <div class="hero-content">
    <p class="h-tag">⚔ &nbsp; Zenshin Clan &nbsp;·&nbsp; $NEKO on Base &nbsp; ⚔</p>
    <div class="h-banner">
      <img src="https://i.ibb.co/wrgX2S3W/Gemini-Generated-Image-9hscr99hscr99hsc.png" alt="Neko the Samurai Cat" />
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
      <iframe
        src="https://www.youtube.com/embed/I4_fKxAayRM?autoplay=1&mute=0&loop=1&playlist=I4_fKxAayRM&controls=1&modestbranding=1&rel=0"
        title="Neko the Samurai Cat"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        style="position:absolute;top:-60px;left:0;width:100%;height:calc(100% + 120px);border:0;">
      </iframe>
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
    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="tc reveal-left d1">
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
    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="tc reveal-right d3">
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
    <div class="lore-img reveal-left">
      <div class="lore-frame">
        <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" />
        <div class="lore-accent"></div>
      </div>
      <div class="lore-shadow"></div>
    </div>
    <div class="reveal-right d2">
      <span class="lore-kanji">前進</span>
      <p class="sec-label">⚔ &nbsp; The Legend</p>
      <h2 class="sec-title">Neko <em>Lore</em></h2>
      <div class="lore-hr"></div>
      <p class="lore-p">In the shadowed valleys of the Base chain, where cherry blossoms drift across digital winds and the blockchain rivers flow with ancient power, a legend was forged.</p>
<p class="lore-p">From the mists of code and courage rose <strong>Neko the Samurai Cat</strong> — eternal leader of the Zenshin Clan. Zenshin is not just a name. It is the sacred principle: <strong>"Forward Progress"</strong> — advance steadily, honorably, and without unnecessary haste. With katana ever-ready and vision sharp as a blade’s edge, Neko moves like the wind: quiet, fierce, and unstoppable.</p>
<p class="lore-p">The Zenshin Clan are samurai cats sworn to <strong>Toshi the Emperor</strong>. Their oath is unbreakable:</p>
<ul class="lore-list">
  <li>Defend Toshi</li>
  <li>Safeguard the holders</li>
  <li>Protect the Base ecosystem</li>
  <li>Preserve harmony no matter the threat</li>
</ul>
<p class="lore-p"><strong>$NEKO</strong> is the living spirit of this legend. Born on the Base chain as a pure community memecoin, $NEKO is more than a token — it is the blade you wield to join the clan. Every holder becomes part of the saga. Every trade echoes the call of Zenshin. Every diamond hand strengthens the oath.</p>
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
    <div class="gi reveal-scale" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal-scale d1" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal-scale d2" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://i.ibb.co/6cpdFyYv/image-24.jpg" alt="Clan Art" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal-scale d3" onclick="openLightbox(this.querySelector('img').src)">
      <img src="https://i.ibb.co/QF6cS9ZV/Neko-The-Samurai.png" alt="Clan Art" />
      <div class="gi-veil"></div>
    </div>
  </div>
</section>

<div class="sec-rule"></div>

<!-- COMMUNITY -->
<section id="join">
  <div style="text-align:center;margin-bottom:4rem;">
    <p class="sec-label reveal">⚔ &nbsp; The Community</p>
    <h2 class="sec-title reveal d1">Join the <em>Clan</em></h2>
  </div>
  <div class="clan-grid">
    <a href="https://x.com/NekoTheSamurai" target="_blank" class="clan-card reveal-scale d1">
      <div class="clan-icon">𝕏</div>
      <span class="clan-name">Follow on X</span>
      <span class="clan-handle">@NekoTheSamurai</span>
    </a>
    <a href="https://t.me/toshimart" target="_blank" class="clan-card reveal-scale d2">
      <div class="clan-icon">✈️</div>
      <span class="clan-name">Telegram</span>
      <span class="clan-handle">Toshimart TG</span>
    </a>
    <a href="https://discord.gg/yKreTaD6Ua" target="_blank" class="clan-card reveal-scale d3">
      <div class="clan-icon">🎮</div>
      <span class="clan-name">Discord</span>
      <span class="clan-handle">Neko Talk</span>
    </a>
    <a href="https://warpcast.com/toshibase" target="_blank" class="clan-card reveal-scale d4">
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
    p.style.cssText = `
      left:${Math.random()*100}%;
      width:${size}px;
      height:${size*1.4}px;
      animation-duration:${7+Math.random()*10}s;
      animation-delay:${Math.random()*15}s;
      opacity:0;
    `;
    container.appendChild(p);
  }

  /* SCROLL REVEAL */
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.1 });
  revealEls.forEach(el => obs.observe(el));

  /* PARALLAX */
  const bgImg = document.getElementById('bg-img');
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    bgImg.style.transform = `translateY(${scrollY * 0.25}px)`;
  }, { passive: true });

  /* COPY CA */
  function copyCA() {
    navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453').then(() => {
      const ok = document.getElementById('ca-ok');
      ok.classList.add('on');
      setTimeout(() => ok.classList.remove('on'), 2200);
    });
  }

  /* HAMBURGER MENU - FIXED */
  function toggleMenu() {
    const menu = document.getElementById('nav-links');
    const ham = document.getElementById('hamburger-btn');
    const isOpen = menu.classList.toggle('open');
    ham.classList.toggle('open', isOpen);
  }

  function closeMenu() {
    const menu = document.getElementById('nav-links');
    const ham = document.getElementById('hamburger-btn');
    menu.classList.remove('open');
    ham.classList.remove('open');
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
  document.addEventListener('keydown', e => { if(e.key === 'Escape') closeLightbox(); });
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

@app.route('/neko-bg.jpg')
def bg_image():
    return send_from_directory('.', 'neko-bg.jpg')

if __name__ == '__main__':
    app.run(debug=True)

