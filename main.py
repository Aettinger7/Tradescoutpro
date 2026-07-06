<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neko the Samurai — $NEKO on Base</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;700;800&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --ink: #16161A;
    --dusk: #22243A;
    --washi: #EDE6D6;
    --washi-soft: #F6F1E6;
    --indigo: #22364F;
    --hanko: #B23A2E;
    --hanko-dark: #8E2C22;
    --gold: #C9A24B;
    --sakura: #D98C99;
    --sakura-deep: #B85C6E;
    --bamboo: #4C6B4F;
    --line: rgba(22,22,26,0.12);
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { margin: 0; background: var(--washi); color: var(--ink); font-family: 'Inter', sans-serif; overflow-x: hidden; position: relative; }
  .wrap { max-width: 1240px; margin: 0 auto; padding: 0 28px; }
  a { color: inherit; }

  @keyframes floaty { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-14px); } }
  @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
  @keyframes petal-fall {
    0%   { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 0; }
    10%  { opacity: .9; }
    100% { transform: translateY(110vh) translateX(60px) rotate(320deg); opacity: 0; }
  }
  .reveal { opacity: 0; transform: translateY(24px); transition: opacity .7s ease, transform .7s ease; }
  .reveal.in { opacity: 1; transform: translateY(0); }

  .petal-field { position: fixed; inset: 0; pointer-events: none; z-index: 1; overflow: hidden; }
  .petal {
    position: absolute; top: -5%; width: 16px; height: 16px;
    background: radial-gradient(circle at 30% 30%, var(--sakura), var(--sakura-deep));
    border-radius: 70% 30% 70% 30%; animation: petal-fall linear infinite; opacity: 0;
  }

  .nav { position: sticky; top: 0; z-index: 50; background: rgba(237,230,214,0.88); backdrop-filter: blur(10px); border-bottom: 1px solid var(--line); }
  .nav-inner { display: flex; align-items: center; justify-content: space-between; padding: 16px 0; }
  .logo { display: flex; align-items: center; gap: 10px; font-family: 'Shippori Mincho', serif; font-weight: 800; font-size: 22px; }
  .logo .mark { width: 34px; height: 34px; background: var(--hanko); border-radius: 6px; display:flex; align-items:center; justify-content:center; color: var(--washi-soft); font-size: 16px; }
  .nav-links { display: flex; gap: 30px; font-size: 14px; font-weight: 600; }
  .nav-links a { text-decoration: none; opacity: .8; }
  .nav-links a:hover { opacity: 1; }
  .nav-cta { display: flex; gap: 12px; }
  .btn-ghost, .btn-solid { font-family: 'Inter', sans-serif; font-weight: 700; font-size: 13.5px; padding: 11px 20px; border-radius: 999px; border: 1.5px solid var(--ink); cursor: pointer; background: none; color: var(--ink); text-decoration: none; display: inline-flex; align-items: center; }
  .btn-solid { background: var(--hanko); color: var(--washi-soft); border-color: var(--hanko); }
  @media (max-width: 880px) { .nav-links { display: none; } }

  .hero { position: relative; padding: 70px 0 40px; z-index: 2; }
  .hero-grid { display: grid; grid-template-columns: 1.1fr 1fr; gap: 40px; align-items: center; }
  .eyebrow { font-family: 'JetBrains Mono', monospace; font-size: 13px; letter-spacing: 2px; text-transform: uppercase; color: var(--hanko); display: flex; align-items: center; gap: 10px; margin-bottom: 22px; }
  .eyebrow::before { content: ""; width: 24px; height: 1px; background: var(--hanko); }
  .hero-copy h1 { font-family: 'Shippori Mincho', serif; font-weight: 800; letter-spacing: -1px; font-size: clamp(52px, 7.2vw, 104px); line-height: 0.95; margin: 0 0 18px; }
  .hero-copy .kanji-sub { font-family: 'Shippori Mincho', serif; font-size: 21px; color: var(--indigo); margin: 0 0 24px; }
  .hero-copy p.desc { font-size: 18.5px; line-height: 1.65; max-width: 480px; color: #3a3a3e; margin: 0 0 34px; font-style: italic; }
  .hero-ctas { display: flex; align-items: center; gap: 20px; flex-wrap: wrap; margin-bottom: 30px;}

  .hanko-btn { position: relative; display: inline-flex; align-items: center; justify-content: center; padding: 20px 40px; border-radius: 10px; background: var(--hanko); color: var(--washi-soft); font-family: 'Shippori Mincho', serif; font-weight: 700; font-size: 19px; letter-spacing: 1px; border: none; cursor: pointer; box-shadow: 0 6px 0 var(--hanko-dark), 0 14px 24px rgba(178,58,46,0.3); transition: transform .12s ease; text-decoration: none; }
  .hanko-btn:hover { transform: translateY(-3px); }
  .hanko-btn:active { transform: translateY(4px); box-shadow: 0 2px 0 var(--hanko-dark); }
  .secondary-link { font-family: 'JetBrains Mono', monospace; font-size: 14px; border-bottom: 1.5px solid var(--ink); padding-bottom: 3px; text-decoration: none; font-weight: 600; }

  .contract-chip { display: inline-flex; align-items: center; gap: 12px; background: var(--washi-soft); border: 1px solid var(--line); padding: 12px 18px; border-radius: 999px; font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #555; }
  .contract-chip button { border: none; background: var(--indigo); color: var(--washi-soft); font-family:'Inter'; font-size: 11px; font-weight: 700; padding: 6px 12px; border-radius: 999px; cursor: pointer; }

  .portrait-stage { position: relative; perspective: 800px; }
  .portrait { aspect-ratio: 4/5; border-radius: 20px; background: linear-gradient(155deg, var(--dusk), var(--ink) 70%); display: flex; align-items: center; justify-content: center; color: rgba(237,230,214,0.5); font-family: 'JetBrains Mono', monospace; font-size: 13px; text-align: center; padding: 24px; box-shadow: 0 30px 60px rgba(22,22,26,0.3); position: relative; overflow: hidden; transition: transform .1s linear; transform-style: preserve-3d; }
  .portrait::before { content:""; position:absolute; inset:0; background: radial-gradient(circle at 25% 15%, rgba(217,140,153,0.28), transparent 55%); }
  .portrait::after { content: "武"; position: absolute; font-family: 'Shippori Mincho', serif; font-size: 340px; color: rgba(237,230,214,0.05); right: -40px; bottom: -60px; line-height: 1; }

  .float-badge { position: absolute; background: var(--washi-soft); border: 1px solid var(--line); border-radius: 14px; padding: 14px 18px; box-shadow: 0 16px 30px rgba(22,22,26,0.16); font-family: 'JetBrains Mono', monospace; animation: floaty 5s ease-in-out infinite; z-index: 3; }
  .float-badge .label { font-size: 10.5px; text-transform: uppercase; letter-spacing: 1px; color: #888; display:block; margin-bottom: 4px; }
  .float-badge .value { font-size: 18px; font-weight: 700; color: var(--ink); }
  .badge-price { top: -6%; left: -8%; animation-delay: 0s; }
  .badge-holders { bottom: 8%; left: -12%; animation-delay: 1.2s; }
  .badge-nft { top: 6%; right: -10%; animation-delay: 0.6s; }
  .badge-clan { bottom: -6%; right: 4%; animation-delay: 1.8s; }
  @media (max-width: 980px) { .float-badge { display: none; } }

  .marquee-strip { background: var(--ink); color: var(--washi-soft); overflow: hidden; padding: 16px 0; margin-top: 50px; position: relative; z-index: 2;}
  .marquee-track { display: flex; width: max-content; animation: marquee 22s linear infinite; }
  .marquee-track span { font-family: 'Shippori Mincho', serif; font-size: 22px; padding: 0 40px; white-space: nowrap; display: flex; align-items: center; gap: 16px; }
  .marquee-track span::after { content: "刀"; color: var(--sakura); font-size: 16px; }

  .exchanges { padding: 60px 0; border-bottom: 1px solid var(--line); position: relative; z-index: 2; }
  .exchanges .label-row { text-align:center; font-family:'JetBrains Mono', monospace; font-size: 12.5px; letter-spacing: 2px; text-transform: uppercase; color: #888; margin-bottom: 30px; }
  .exchange-row { display: flex; justify-content: center; gap: 18px; flex-wrap: wrap; }
  .exchange-pill { display: flex; align-items: center; gap: 10px; background: var(--washi-soft); border: 1px solid var(--line); padding: 14px 24px; border-radius: 999px; font-weight: 700; font-size: 14.5px; text-decoration: none; color: var(--ink); transition: transform .15s ease, box-shadow .15s ease; }
  .exchange-pill:hover { transform: translateY(-4px); box-shadow: 0 14px 24px rgba(22,22,26,0.12); }
  .exchange-pill .dot { width: 9px; height: 9px; border-radius: 50%; background: var(--bamboo); }

  .video-section { padding: 100px 0; border-bottom: 1px solid var(--line); background: var(--washi-soft); position: relative; z-index: 2; }
  .video-frame { aspect-ratio: 16/9; border-radius: 18px; background: linear-gradient(150deg, var(--dusk), var(--ink)); display: flex; align-items: center; justify-content: center; color: rgba(237,230,214,0.5); font-family: 'JetBrains Mono', monospace; font-size: 13px; box-shadow: 0 30px 60px rgba(22,22,26,0.25); position: relative; overflow: hidden; }
  .video-frame .play-badge { width: 74px; height: 74px; border-radius: 50%; background: var(--hanko); display: flex; align-items: center; justify-content: center; color: var(--washi-soft); font-size: 22px; box-shadow: 0 12px 26px rgba(178,58,46,0.4); animation: floaty 4s ease-in-out infinite; }

  .howto { padding: 100px 0; border-bottom: 1px solid var(--line); position: relative; z-index: 2; }
  .section-head { margin-bottom: 54px; max-width: 640px; }
  .section-head h2 { font-family: 'Shippori Mincho', serif; font-size: clamp(32px, 4.4vw, 48px); margin: 10px 0 0; font-weight: 700; }
  .steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 26px; }
  .step-card { background: var(--washi-soft); border: 1px solid var(--line); border-radius: 14px; padding: 34px 28px; position: relative; transition: transform .2s ease, box-shadow .2s ease; }
  .step-card:hover { transform: translateY(-8px); box-shadow: 0 20px 36px rgba(22,22,26,0.14); }
  .step-kanji { font-family: 'Shippori Mincho', serif; font-size: 48px; font-weight: 700; color: var(--hanko); line-height: 1; margin-bottom: 20px; display: block; }
  .step-card h3 { font-family: 'Shippori Mincho', serif; font-size: 21px; margin: 0 0 12px; }
  .step-card p { font-size: 15px; line-height: 1.6; color: #4a4a4e; margin: 0; }

  .trade-section { padding: 100px 0; border-bottom: 1px solid var(--line); position: relative; z-index: 2; }
  .trade-note { font-size: 14px; color: #777; font-family: 'JetBrains Mono', monospace; margin: -30px 0 40px; }
  .trade-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 26px; }
  .trade-card { background: var(--ink); color: var(--washi-soft); border-radius: 16px; padding: 32px 28px; text-decoration: none; display: block; position: relative; overflow: hidden; transition: transform .2s ease, box-shadow .2s ease; }
  .trade-card:hover { transform: translateY(-8px); box-shadow: 0 24px 44px rgba(22,22,26,0.28); }
  .trade-card .tag { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--sakura); text-transform: uppercase; letter-spacing: 1px; }
  .trade-card h3 { font-family: 'Shippori Mincho', serif; font-size: 22px; margin: 12px 0 10px; }
  .trade-card p { font-size: 14px; line-height: 1.6; color: rgba(237,230,214,0.65); margin: 0 0 20px; }
  .trade-card .go { font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700; color: var(--gold); }
  .trade-card::after { content: "刀"; position: absolute; right: -10px; bottom: -30px; font-family: 'Shippori Mincho', serif; font-size: 140px; color: rgba(237,230,214,0.04); }

  .lore { padding: 110px 0; border-bottom: 1px solid var(--line); background: var(--washi-soft); position: relative; z-index: 2; }
  .lore-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
  .lore-art { position: relative; }
  .scroll-frag { background: linear-gradient(150deg, var(--dusk), var(--ink)); border-radius: 16px; aspect-ratio: 4/3; position: relative; overflow: hidden; box-shadow: 0 26px 50px rgba(22,22,26,0.25); }
  .scroll-frag::after { content: "禅"; position: absolute; font-family:'Shippori Mincho',serif; font-size: 220px; color: rgba(217,140,153,0.08); right: -20px; bottom: -40px; }
  .quote-float { position: absolute; bottom: -30px; left: -30px; background: var(--washi); border: 1px solid var(--line); border-radius: 12px; padding: 20px 24px; max-width: 260px; box-shadow: 0 20px 36px rgba(22,22,26,0.16); font-family: 'Shippori Mincho', serif; font-size: 15px; line-height: 1.5; animation: floaty 6s ease-in-out infinite; }
  .lore-copy h2 { font-family: 'Shippori Mincho', serif; font-size: clamp(30px,4vw,42px); margin: 10px 0 22px; }
  .lore-copy p { font-size: 16.5px; line-height: 1.7; color: #3a3a3e; margin: 0 0 18px; }
  .lore-copy ul { padding-left: 20px; margin: 0 0 22px; }
  .lore-copy li { font-size: 15.5px; line-height: 1.8; color: #3a3a3e; }

  .gallery { padding: 100px 0; border-bottom: 1px solid var(--line); position: relative; z-index: 2; }
  .gallery-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 46px; }
  .gallery-tile { aspect-ratio: 3/4; border-radius: 14px; position: relative; overflow: hidden; background: linear-gradient(160deg, var(--dusk), var(--ink)); display: flex; align-items: flex-end; padding: 16px; transition: transform .25s ease; }
  .gallery-tile:hover { transform: translateY(-8px) scale(1.02); }
  .gallery-tile span { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: rgba(237,230,214,0.6); }
  .gallery-tile::before { content:""; position:absolute; inset:0; background: radial-gradient(circle at 70% 20%, rgba(217,140,153,0.18), transparent 55%); }
  @media (max-width: 900px) { .gallery-grid { grid-template-columns: repeat(2,1fr); } }

  .tokenomics { padding: 100px 0; border-bottom: 1px solid var(--line); background: var(--ink); color: var(--washi-soft); position: relative; z-index: 2; }
  .tokenomics .section-head h2 { color: var(--washi-soft); }
  .tokenomics .eyebrow { color: var(--gold); }
  .tokenomics .eyebrow::before { background: var(--gold); }
  .stat-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; margin-bottom: 46px; }
  .stat-box { background: rgba(237,230,214,0.06); border: 1px solid rgba(237,230,214,0.14); border-radius: 14px; padding: 26px; transition: transform .2s ease; }
  .stat-box:hover { transform: translateY(-6px); }
  .stat-box .num { font-family: 'JetBrains Mono', monospace; font-size: 30px; font-weight: 700; color: var(--sakura); }
  .stat-box .cap { font-size: 12.5px; text-transform: uppercase; letter-spacing: 1px; color: rgba(237,230,214,0.6); margin-top: 6px; }

  footer { padding: 60px 0 40px; position: relative; z-index: 2; }
  .footer-top { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px; margin-bottom: 34px; }
  .socials { display: flex; gap: 14px; }
  .socials a { width: 40px; height: 40px; border-radius: 50%; border: 1px solid var(--ink); display: flex; align-items: center; justify-content: center; font-size: 13px; text-decoration: none; font-weight: 700; transition: transform .15s ease, background .15s ease; }
  .socials a:hover { transform: translateY(-4px); background: var(--ink); color: var(--washi-soft); }
  .footer-legal { font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #888; line-height: 1.7; border-top: 1px solid var(--line); padding-top: 24px; }

  @media (max-width: 980px) {
    .hero-grid, .lore-grid, .trade-grid { grid-template-columns: 1fr; }
    .steps { grid-template-columns: 1fr; }
    .stat-grid { grid-template-columns: repeat(2,1fr); }
    .gallery-grid { grid-template-columns: repeat(2,1fr); }
  }
  @media (prefers-reduced-motion: reduce) {
    .float-badge, .marquee-track, .quote-float, .petal, .video-frame .play-badge { animation: none; }
  }
  button:focus-visible, a:focus-visible, input:focus-visible { outline: 2px solid var(--gold); outline-offset: 2px; }
</style>
</head>
<body>

<div class="petal-field" id="petal-field"></div>

<nav class="nav">
  <div class="wrap nav-inner">
    <div class="logo"><span class="mark">刀</span> Neko the Samurai</div>
    <div class="nav-links">
      <a href="#trade">Trade</a>
      <a href="#lore">Lore</a>
      <a href="#gallery">Gallery</a>
      <a href="#join">Clan</a>
      <a href="/litepaper">Litepaper</a>
    </div>
    <div class="nav-cta">
      <a class="btn-ghost" href="https://opensea.io/collection/neko-shogun" target="_blank" rel="noopener">OpenSea</a>
      <a class="btn-ghost" href="https://YOUR_MERCH_STORE_URL_HERE" target="_blank" rel="noopener">Merch</a>
      <a class="btn-solid" href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank" rel="noopener">Buy $NEKO</a>
    </div>
  </div>
</nav>

<!-- ... rest of your original code stays exactly the same ... -->

<section class="hero">
  ... (your hero section unchanged)
</section>

<!-- All other sections unchanged -->

</body>
</html>

