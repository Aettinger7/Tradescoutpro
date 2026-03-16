from flask import Flask, render_template_string
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
  <meta name="twitter:image" content="https://i.ibb.co/6cpdFyYv/image-24.jpg">
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
    /* ── RESET & BASE ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    :root {
      --ink:        #07050a;
      --deep:       #0f0b14;
      --panel:      #13101a;
      --crimson:    #7a0012;
      --red:        #b01020;
      --ember:      #d4182e;
      --gold:       #c89b3c;
      --gold-lt:    #e8c06a;
      --gold-dim:   #6e5220;
      --cream:      #ede4cc;
      --muted:      #7a6e60;
      --fog:        rgba(237,228,204,0.55);
    }

    body {
      background: var(--ink);
      color: var(--cream);
      font-family: 'Zen Kaku Gothic New', sans-serif;
      font-weight: 300;
      overflow-x: hidden;
    }

    /* ── CUSTOM CURSOR ── */
    *, a, button { cursor: none !important; }
    #cur {
      position: fixed; z-index: 9999; pointer-events: none;
      width: 14px; height: 14px;
      border: 1.5px solid var(--gold);
      border-radius: 50%;
      transform: translate(-50%,-50%);
      transition: width .2s, height .2s, background .2s, border-color .2s;
      mix-blend-mode: exclusion;
    }
    #cur.big {
      width: 38px; height: 38px;
      background: rgba(200,155,60,.12);
      border-color: var(--gold-lt);
    }

    /* ── NOISE GRAIN ── */
    body::after {
      content:''; position:fixed; inset:0; z-index:1; pointer-events:none;
      background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='.03'/%3E%3C/svg%3E");
      opacity:.55;
    }

    /* ── NAV ── */
    nav {
      position: fixed; inset: 0 0 auto; z-index: 200;
      padding: 1.6rem 4rem;
      display: flex; align-items: center; justify-content: space-between;
      background: linear-gradient(to bottom, rgba(7,5,10,.92) 0%, transparent 100%);
    }
    .nav-logo {
      display: flex; align-items: center; gap: .8rem;
      text-decoration: none;
    }
    .nav-logo img {
      width: 34px; height: 34px; border-radius: 50%;
      border: 1px solid var(--gold-dim);
      object-fit: cover;
    }
    .nav-logo-name {
      font-family: 'Shippori Mincho B1', serif;
      font-size: .95rem; font-weight: 700;
      color: var(--gold-lt); letter-spacing: .08em;
    }
    .nav-links {
      display: flex; align-items: center; gap: 2.6rem; list-style: none;
    }
    .nav-links a {
      font-size: .7rem; letter-spacing: .22em; text-transform: uppercase;
      color: var(--muted); text-decoration: none;
      transition: color .25s;
      position: relative;
    }
    .nav-links a::after {
      content:''; position:absolute; bottom:-3px; left:0;
      width:0; height:1px; background:var(--gold);
      transition: width .3s;
    }
    .nav-links a:hover { color: var(--gold-lt); }
    .nav-links a:hover::after { width: 100%; }
    .nav-buy {
      font-size: .7rem !important; letter-spacing: .18em !important;
      padding: .45rem 1.3rem;
      border: 1px solid var(--gold-dim);
      border-radius: 2px;
      color: var(--gold-lt) !important;
      transition: background .25s, border-color .25s !important;
    }
    .nav-buy:hover { background: rgba(200,155,60,.1) !important; border-color: var(--gold) !important; }
    .nav-buy::after { display: none !important; }

    /* ── HERO ── */
    #hero {
      min-height: 100vh;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center;
      padding: 7rem 2rem 5rem;
      position: relative; overflow: hidden;
    }

    /* layered radial glow background */
    .hero-glow {
      position: absolute; inset: 0; pointer-events: none;
      background:
        radial-gradient(ellipse 55% 65% at 50% 58%, rgba(122,0,18,.2) 0%, transparent 65%),
        radial-gradient(ellipse 90% 40% at 50% 100%, rgba(100,0,12,.15) 0%, transparent 60%),
        var(--ink);
    }
    .hero-glow::before {
      content: '';
      position: absolute; inset: 0;
      background: radial-gradient(ellipse 35% 35% at 50% 52%, rgba(176,16,32,.07) 0%, transparent 70%);
      animation: breathe 5s ease-in-out infinite;
    }
    @keyframes breathe {
      0%,100% { opacity:.4; transform:scale(1);   }
      50%      { opacity:1;  transform:scale(1.08); }
    }

    /* sakura petals */
    .sakura { position:absolute; inset:0; overflow:hidden; pointer-events:none; }
    .petal {
      position:absolute; top:-20px;
      width:5px; height:8px;
      background: radial-gradient(ellipse, rgba(176,16,32,.55), transparent);
      border-radius: 60% 0 60% 0;
      animation: drift linear infinite;
      opacity:0;
    }
    @keyframes drift {
      0%   { transform:translateY(0) rotate(0deg)   translateX(0);   opacity:0; }
      8%   { opacity:.65; }
      92%  { opacity:.3; }
      100% { transform:translateY(105vh) rotate(600deg) translateX(50px); opacity:0; }
    }

    /* large orbit ring */
    .orbit {
      position: absolute; top:50%; left:50%;
      transform: translate(-50%,-50%);
      width: min(800px,90vw); height: min(800px,90vw);
      border-radius: 50%;
      border: 1px solid rgba(200,155,60,.05);
      animation: spin 50s linear infinite;
      pointer-events: none;
    }
    .orbit::before {
      content:''; position:absolute; inset:28px;
      border-radius:50%; border:1px solid rgba(200,155,60,.03);
    }
    @keyframes spin { to { transform: translate(-50%,-50%) rotate(360deg); } }

    /* hero content stagger */
    .hero-content { position:relative; z-index:2; }
    .h-tag {
      font-size:.65rem; letter-spacing:.4em; text-transform:uppercase;
      color:var(--gold-dim); margin-bottom:2rem;
      opacity:0; animation: rise .8s .15s forwards;
    }
    .h-portrait {
      width:190px; height:190px; margin:0 auto 2.8rem;
      position:relative;
      opacity:0; animation:rise .9s .35s forwards;
    }
    .h-portrait::before,
    .h-portrait::after {
      content:''; position:absolute; border-radius:50%;
      border:1px solid rgba(200,155,60,.25);
      inset:-14px; animation: breathe 3.5s ease-in-out infinite;
    }
    .h-portrait::after {
      inset:-28px;
      border-color:rgba(200,155,60,.1);
      animation-delay:.5s;
    }
    .h-portrait img {
      width:100%; height:100%; border-radius:50%; object-fit:cover;
      border:2px solid rgba(200,155,60,.45);
      box-shadow: 0 0 70px rgba(176,16,32,.35), 0 0 140px rgba(122,0,18,.2);
    }

    h1.h-title {
      font-family:'Shippori Mincho B1', serif;
      font-size: clamp(3.5rem,9vw,8rem);
      font-weight:800; line-height:.88; letter-spacing:-.025em;
      color:var(--cream); margin-bottom:.55rem;
      opacity:0; animation:rise .9s .55s forwards;
    }
    h1.h-title em {
      font-style:normal;
      background:linear-gradient(130deg, var(--gold-lt) 0%, var(--gold) 45%, var(--gold-dim) 100%);
      -webkit-background-clip:text; -webkit-text-fill-color:transparent;
      background-clip:text;
    }

    .h-sub {
      font-family:'Noto Serif JP', serif; font-weight:200;
      font-size:clamp(.7rem,1.4vw,.88rem);
      letter-spacing:.5em; text-transform:uppercase;
      color:var(--muted); margin-bottom:.9rem;
      opacity:0; animation:rise .9s .7s forwards;
    }
    .h-quote {
      font-size:clamp(.9rem,1.7vw,1.05rem); font-style:italic;
      color:rgba(237,228,204,.5); margin-bottom:2.8rem;
      opacity:0; animation:rise .9s .82s forwards;
    }

    /* CA pill */
    .ca-pill {
      display:inline-flex; align-items:center; gap:.7rem;
      border:1px solid rgba(200,155,60,.18);
      background:rgba(255,255,255,.02);
      border-radius:3px; padding:.55rem 1.3rem;
      font-size:.68rem; letter-spacing:.1em;
      color:var(--muted); margin-bottom:2.6rem;
      transition:border-color .25s, color .25s;
      opacity:0; animation:rise .9s .95s forwards;
    }
    .ca-pill:hover { border-color:var(--gold); color:var(--gold-lt); }
    .ca-mono { font-family:monospace; font-size:.62rem; }
    .ca-btn {
      background:none; border:none; padding:0;
      font-size:.8rem; color:var(--gold-dim);
      transition:color .2s;
    }
    .ca-btn:hover { color:var(--gold); }
    .ca-confirm { font-size:.62rem; color:var(--gold); opacity:0; transition:opacity .3s; }
    .ca-confirm.on { opacity:1; }

    /* CTA buttons */
    .h-btns {
      display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;
      opacity:0; animation:rise .9s 1.05s forwards;
    }
    .btn-fill {
      background:linear-gradient(130deg, var(--crimson), var(--red));
      color:var(--cream); text-decoration:none;
      padding:.9rem 2.4rem; border-radius:2px;
      font-size:.74rem; letter-spacing:.22em; text-transform:uppercase;
      box-shadow: 0 4px 32px rgba(176,16,32,.38);
      position:relative; overflow:hidden;
      transition:box-shadow .3s, transform .2s;
    }
    .btn-fill::before {
      content:''; position:absolute; inset:0;
      background:linear-gradient(130deg,rgba(255,255,255,.08),transparent);
      opacity:0; transition:opacity .25s;
    }
    .btn-fill:hover { box-shadow:0 6px 48px rgba(176,16,32,.6); transform:translateY(-2px); }
    .btn-fill:hover::before { opacity:1; }
    .btn-ghost {
      background:transparent; color:var(--gold-lt); text-decoration:none;
      padding:.9rem 2.4rem; border-radius:2px;
      border:1px solid var(--gold-dim);
      font-size:.74rem; letter-spacing:.22em; text-transform:uppercase;
      transition:background .25s, border-color .25s, transform .2s;
    }
    .btn-ghost:hover { background:rgba(200,155,60,.08); border-color:var(--gold); transform:translateY(-2px); }

    /* scroll cue */
    .scroll-cue {
      position:absolute; bottom:2rem; left:50%; transform:translateX(-50%);
      display:flex; flex-direction:column; align-items:center; gap:.5rem;
      opacity:0; animation:rise 1s 1.6s forwards; z-index:2;
    }
    .scroll-cue span { font-size:.58rem; letter-spacing:.35em; text-transform:uppercase; color:var(--gold-dim); }
    .scroll-line { width:1px; height:38px; background:linear-gradient(to bottom,var(--gold-dim),transparent); animation:pulse-line 2.2s ease-in-out infinite; }
    @keyframes pulse-line { 0%,100%{opacity:.3} 50%{opacity:1} }

    @keyframes rise {
      from { opacity:0; transform:translateY(24px); }
      to   { opacity:1; transform:translateY(0); }
    }

    /* ── SHARED SECTION STYLES ── */
    section { position:relative; }
    .sec-rule { width:100%; height:1px; background:linear-gradient(to right,transparent,rgba(200,155,60,.25),transparent); }

    .sec-label {
      font-size:.6rem; letter-spacing:.4em; text-transform:uppercase;
      color:var(--gold-dim); margin-bottom:1rem;
    }
    h2.sec-title {
      font-family:'Shippori Mincho B1',serif;
      font-size:clamp(2.2rem,5vw,4rem);
      font-weight:700; color:var(--cream); letter-spacing:-.01em;
      margin-bottom:.5rem;
    }
    h2.sec-title em { font-style:normal; color:var(--gold); }

    /* reveal on scroll */
    .reveal { opacity:0; transform:translateY(28px); transition:opacity .85s ease, transform .85s ease; }
    .reveal.in { opacity:1; transform:translateY(0); }
    .d1{transition-delay:.1s} .d2{transition-delay:.2s} .d3{transition-delay:.3s} .d4{transition-delay:.4s}

    /* ── VIDEO ── */
    #video-section { padding:7rem 4rem; text-align:center; background:var(--deep); position:relative; }
    #video-section::before {
      content:''; position:absolute; inset:0;
      background:radial-gradient(ellipse 60% 70% at 50% 50%, rgba(122,0,18,.13) 0%,transparent 70%);
      pointer-events:none;
    }
    .video-wrap {
      max-width:900px; margin:3rem auto 0;
      position:relative;
      border:1px solid rgba(200,155,60,.18);
      box-shadow: 0 0 80px rgba(122,0,18,.25), 0 0 160px rgba(122,0,18,.1);
    }
    .video-wrap::before {
      content:''; position:absolute; top:-1px; left:0; right:0; height:2px;
      background:linear-gradient(to right, transparent, var(--gold), transparent);
    }
    .video-wrap::after {
      content:''; position:absolute; bottom:-1px; left:0; right:0; height:2px;
      background:linear-gradient(to right, transparent, var(--crimson), transparent);
    }
    .video-wrap video {
      width:100%; display:block;
      background:var(--ink);
    }

    /* ── TRADE ── */
    #trade { padding:8rem 4rem; }
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
      transition:background .3s;
    }
    .tc::before {
      content:''; position:absolute; top:0; left:0; right:0; height:2px;
      background:linear-gradient(to right,transparent,var(--crimson),transparent);
      opacity:0; transition:opacity .3s;
    }
    .tc:hover { background:rgba(122,0,18,.12); }
    .tc:hover::before { opacity:1; }
    .tc-num {
      font-family:'Shippori Mincho B1',serif;
      font-size:3rem; font-weight:800;
      color:rgba(200,155,60,.07); line-height:1; margin-bottom:.4rem;
    }
    .tc-tag { font-size:.58rem; letter-spacing:.3em; text-transform:uppercase; color:var(--gold-dim); margin-bottom:.5rem; }
    .tc h3 { font-family:'Shippori Mincho B1',serif; font-size:1.25rem; font-weight:700; color:var(--cream); margin-bottom:.5rem; }
    .tc p  { font-size:.82rem; color:var(--muted); line-height:1.7; margin-bottom:1.6rem; }
    .tc-arrow { font-size:.68rem; letter-spacing:.2em; text-transform:uppercase; color:var(--gold); }
    .tc-arrow::after { content:' →'; transition:margin .2s; display:inline-block; }
    .tc:hover .tc-arrow::after { margin-left:5px; }

    /* chart */
    .chart-box {
      max-width:1000px; margin:2.5rem auto 0;
      border:1px solid rgba(200,155,60,.1);
      background:var(--panel); overflow:hidden;
    }
    .chart-bar {
      padding:.9rem 1.4rem;
      border-bottom:1px solid rgba(200,155,60,.08);
      display:flex; align-items:center; justify-content:space-between;
    }
    .chart-bar span { font-size:.65rem; letter-spacing:.22em; text-transform:uppercase; color:var(--gold-dim); }
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
    .lore-inner {
      max-width:1120px; margin:0 auto;
      display:grid; grid-template-columns:1fr 1fr;
      gap:5rem; align-items:center; position:relative; z-index:1;
    }
    .lore-img { position:relative; }
    .lore-frame {
      position:relative; width:100%; aspect-ratio:3/4; overflow:hidden;
    }
    .lore-frame::after {
      content:''; position:absolute; inset:0;
      background:linear-gradient(to top,rgba(15,11,20,.85) 0%,transparent 55%);
    }
    .lore-frame img {
      width:100%; height:100%; object-fit:cover; display:block;
      filter:saturate(.65) contrast(1.1);
      transition:transform 7s ease, filter .5s;
    }
    .lore-frame:hover img { transform:scale(1.05); filter:saturate(.9) contrast(1.1); }
    .lore-accent {
      position:absolute; bottom:0; left:0; right:0; height:3px;
      background:linear-gradient(to right, var(--crimson), var(--gold-dim));
    }
    .lore-shadow {
      position:absolute; top:18px; left:18px; right:-18px; bottom:-18px;
      border:1px solid rgba(200,155,60,.12); z-index:-1;
    }
    .lore-text {}
    .lore-kanji {
      font-family:'Noto Serif JP',serif; font-weight:200;
      font-size:5.5rem; color:rgba(200,155,60,.1);
      line-height:1; margin-bottom:-1.4rem; display:block;
    }
    .lore-hr { width:56px; height:1px; background:linear-gradient(to right,var(--crimson),var(--gold-dim)); margin:1.5rem 0; }
    .lore-p {
      font-size:.88rem; line-height:2; color:var(--muted); margin-bottom:1.2rem;
    }
    .lore-p:first-of-type { color:rgba(237,228,204,.75); }
    .lore-p:last-of-type  { color:rgba(237,228,204,.6); }

    /* ── COMMUNITY ── */
    #join { padding:8rem 4rem; text-align:center; }
    .clan-grid {
      display:grid; grid-template-columns:repeat(4,1fr);
      gap:1px; background:rgba(200,155,60,.09);
      max-width:920px; margin:0 auto;
    }
    .clan-card {
      background:var(--ink); padding:2.8rem 1.5rem;
      text-decoration:none; display:flex; flex-direction:column; align-items:center; gap:1.1rem;
      position:relative; overflow:hidden;
      transition:background .3s;
    }
    .clan-card::after {
      content:''; position:absolute; bottom:0; left:0; right:0; height:2px;
      background:linear-gradient(to right,transparent,var(--gold),transparent);
      transform:scaleX(0); transition:transform .35s;
    }
    .clan-card:hover { background:rgba(200,155,60,.04); }
    .clan-card:hover::after { transform:scaleX(1); }
    .clan-icon {
      width:54px; height:54px; border-radius:50%;
      border:1px solid rgba(200,155,60,.18);
      display:flex; align-items:center; justify-content:center;
      font-size:1.5rem;
      transition:border-color .3s, box-shadow .3s;
    }
    .clan-card:hover .clan-icon { border-color:var(--gold); box-shadow:0 0 22px rgba(200,155,60,.22); }
    .clan-name { font-family:'Shippori Mincho B1',serif; font-size:1rem; font-weight:700; color:var(--cream); }
    .clan-handle { font-size:.7rem; color:var(--muted); }

    /* ── GALLERY ── */
    #art { padding:8rem 4rem; background:var(--deep); }
    #art::after {
      content:''; position:absolute; bottom:0; left:0;
      width:500px; height:350px;
      background:radial-gradient(ellipse,rgba(122,0,18,.08) 0%,transparent 70%);
      pointer-events:none;
    }
    .gallery {
      display:grid;
      grid-template-columns:2fr 1fr 1fr;
      grid-template-rows:auto auto;
      gap:4px; max-width:1120px; margin:0 auto;
    }
    .gi { overflow:hidden; position:relative; background:var(--panel); }
    .gi:first-child { grid-row:1/3; }
    .gi img {
      width:100%; height:100%; object-fit:cover; display:block; min-height:220px;
      filter:saturate(.7) contrast(1.05);
      transition:transform .7s ease, filter .4s;
    }
    .gi:first-child img { min-height:500px; }
    .gi:hover img { transform:scale(1.06); filter:saturate(1) contrast(1.05); }
    .gi-veil {
      position:absolute; inset:0;
      background:linear-gradient(to top,rgba(7,5,10,.65) 0%,transparent 55%);
      opacity:0; transition:opacity .4s;
    }
    .gi:hover .gi-veil { opacity:1; }

    /* ── FOOTER ── */
    footer {
      padding:3rem 4rem;
      border-top:1px solid rgba(200,155,60,.1);
      display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1.5rem;
    }
    .ft-brand { font-family:'Shippori Mincho B1',serif; font-size:1.1rem; font-weight:700; color:var(--gold); }
    .ft-meta { font-size:.7rem; color:var(--muted); line-height:1.8; }
    .ft-disclaimer { font-size:.62rem; color:rgba(122,110,96,.45); max-width:360px; line-height:1.6; }

    /* ── RESPONSIVE ── */
    @media(max-width:960px){
      nav { padding:1.2rem 1.8rem; }
      #trade,#lore,#join,#art,#video-section { padding:5.5rem 1.8rem; }
      .trade-cards { grid-template-columns:1fr; }
      .lore-inner { grid-template-columns:1fr; gap:3rem; }
      .lore-img { max-width:380px; margin:0 auto; }
      .clan-grid { grid-template-columns:1fr 1fr; }
      .gallery { grid-template-columns:1fr 1fr; }
      .gi:first-child { grid-row:auto; grid-column:1/3; }
      footer { flex-direction:column; text-align:center; }
    }
    @media(max-width:600px){
      nav { padding:1rem 1.2rem; }
      .nav-links { gap:1rem; }
      h1.h-title { font-size:3rem; }
      .clan-grid { grid-template-columns:1fr 1fr; }
      .gallery { grid-template-columns:1fr; }
      .gi:first-child { grid-column:auto; }
      #trade,#lore,#join,#art,#video-section { padding:4rem 1.2rem; }
    }
  </style>
</head>
<body>

<!-- CURSOR -->
<div id="cur"></div>

<!-- ── NAV ── -->
<nav>
  <a href="#" class="nav-logo">
    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko" />
    <span class="nav-logo-name">Neko ⚔</span>
  </a>
  <ul class="nav-links">
    <li><a href="#trade">Trade</a></li>
    <li><a href="#join">Clan</a></li>
    <li><a href="#lore">Lore</a></li>
    <li><a href="#art">Gallery</a></li>
    <li><a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" class="nav-buy">Buy $NEKO</a></li>
  </ul>
</nav>

<!-- ── HERO ── -->
<section id="hero">
  <div class="hero-glow"></div>
  <div class="sakura" id="sakura"></div>
  <div class="orbit"></div>

  <div class="hero-content">
    <p class="h-tag">⚔ &nbsp; Zenshin Clan &nbsp;·&nbsp; $NEKO on Base &nbsp; ⚔</p>

    <div class="h-portrait">
      <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko the Samurai Cat" />
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

<!-- ── VIDEO ── -->
<section id="video-section">
  <div style="position:relative;z-index:1;">
    <p class="sec-label reveal">⚔ &nbsp; The Clan in Motion</p>
    <h2 class="sec-title reveal d1">Watch <em>Neko</em></h2>
  </div>
  <div class="video-wrap reveal d2" style="position:relative;">
    <video
      id="neko-video"
      loop
      playsinline
      preload="auto"
      style="width:100%;display:block;background:var(--ink);"
    >
      <source src="/video" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
    <!-- Play button overlay -->
    <div id="play-overlay" onclick="playVideo()" style="
      position:absolute; inset:0;
      display:flex; flex-direction:column; align-items:center; justify-content:center;
      background:rgba(7,5,10,.55);
      cursor:none;
      transition:background .3s;
    ">
      <div style="
        width:72px; height:72px; border-radius:50%;
        border:2px solid rgba(200,155,60,.6);
        display:flex; align-items:center; justify-content:center;
        font-size:1.8rem;
        box-shadow:0 0 40px rgba(122,0,18,.4);
        transition:transform .2s, border-color .2s, box-shadow .2s;
        background:rgba(122,0,18,.3);
      " id="play-btn-circle">▶</div>
      <p style="margin-top:1rem;font-size:.68rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(200,155,60,.7);">Click to Watch</p>
    </div>
  </div>
</section>

<div class="sec-rule"></div>

<!-- ── TRADE ── -->
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

<!-- ── LORE ── -->
<section id="lore">
  <div class="lore-inner">
    <div class="lore-img reveal">
      <div class="lore-frame">
        <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" />
        <div class="lore-accent"></div>
      </div>
      <div class="lore-shadow"></div>
    </div>

    <div class="lore-text reveal d2">
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

<!-- ── COMMUNITY ── -->
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

<div class="sec-rule"></div>

<!-- ── GALLERY ── -->
<section id="art">
  <div style="text-align:center;margin-bottom:4rem;">
    <p class="sec-label reveal">⚔ &nbsp; Clan Artwork</p>
    <h2 class="sec-title reveal d1">The <em>Gallery</em></h2>
  </div>

  <div class="gallery">
    <div class="gi reveal">
      <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal d1">
      <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal d2">
      <img src="https://pbs.twimg.com/media/G_IEacWXUAAZVuE.jpg" alt="Clan Art" />
      <div class="gi-veil"></div>
    </div>
    <div class="gi reveal d3">
      <img src="https://pbs.twimg.com/media/G_H77YTXcAAv5dE.jpg" alt="Clan Art" />
      <div class="gi-veil"></div>
    </div>
  </div>
</section>

<!-- ── FOOTER ── -->
<footer>
  <span class="ft-brand">Neko ⚔ $NEKO</span>
  <div class="ft-meta">
    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" style="color:var(--gold);text-decoration:none;">Uniswap</a>
    &nbsp;·&nbsp;
    <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank" style="color:var(--gold-dim);text-decoration:none;">Dexscreener</a>
    &nbsp;·&nbsp;
    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" style="color:var(--gold-dim);text-decoration:none;">Toshimart</a>
    <br />
    © 2026 Neko on Base &nbsp;·&nbsp; Last Update: {{ last_update }}
  </div>
  <p class="ft-disclaimer">DYOR – Not financial advice. $NEKO is a meme token on Base. Trade responsibly.</p>
</footer>

<script>
  /* ── CURSOR ── */
  const cur = document.getElementById('cur');
  document.addEventListener('mousemove', e => {
    cur.style.left = e.clientX + 'px';
    cur.style.top  = e.clientY + 'px';
  });
  document.querySelectorAll('a,button,.ca-pill,.tc,.clan-card,.gi').forEach(el => {
    el.addEventListener('mouseenter', () => cur.classList.add('big'));
    el.addEventListener('mouseleave', () => cur.classList.remove('big'));
  });

  /* ── SAKURA PETALS ── */
  const container = document.getElementById('sakura');
  for (let i = 0; i < 18; i++) {
    const p = document.createElement('div');
    p.className = 'petal';
    p.style.cssText = `
      left:${Math.random()*100}%;
      width:${4+Math.random()*5}px;
      height:${6+Math.random()*7}px;
      animation-duration:${8+Math.random()*12}s;
      animation-delay:${Math.random()*14}s;
      opacity:0;
    `;
    container.appendChild(p);
  }

  /* ── SCROLL REVEAL ── */
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

  /* ── PLAY VIDEO ── */
  function playVideo() {
    const video = document.getElementById('neko-video');
    const overlay = document.getElementById('play-overlay');
    video.play();
    overlay.style.opacity = '0';
    overlay.style.pointerEvents = 'none';
    overlay.style.transition = 'opacity .4s';
  }

  /* ── COPY CA ── */
  function copyCA() {
    navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453').then(() => {
      const ok = document.getElementById('ca-ok');
      ok.classList.add('on');
      setTimeout(() => ok.classList.remove('on'), 2200);
    });
  }
</script>
</body>
</html>
'''

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

@app.route('/video')
def video():
    from flask import send_from_directory
    import os
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'NekoSamurai.mp4', mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)





