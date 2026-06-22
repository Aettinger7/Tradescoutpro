<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neko the Samurai Cat ⚔️🐱 $NEKO on Base</title>
<meta name="description" content="Zenshin Clan – Forward Progress. $NEKO meme token on Base.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Shippori+Mincho+B1:wght@500;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --indigo-deep:#0a0707;
  --indigo-mid:#1c0c0d;
  --indigo-soft:#3a1216;
  --gold:#c79a3b;
  --gold-bright:#f0cf76;
  --crimson:#9e1b25;
  --ivory:#ede6d3;
  --ivory-dim:#b8a99c;
  --font-display:'Shippori Mincho B1', serif;
  --font-script:'Cormorant Garamond', serif;
  --font-body:'Inter', sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  background:var(--indigo-deep);
  color:var(--ivory);
  font-family:var(--font-body);
  overflow-x:hidden;
  position:relative;
}
a{color:inherit;text-decoration:none;}

/* ---------- background seigaiha wave layer (parallax) ---------- */
.wave-bg{
  position:fixed;
  inset:0;
  z-index:0;
  background-image:radial-gradient(circle at 0 0, transparent 38%, var(--indigo-mid) 39%, var(--indigo-mid) 40%, transparent 41%);
  background-size:90px 90px;
  opacity:.18;
  pointer-events:none;
  will-change:transform;
}

/* ---------- nav ---------- */
nav{
  position:fixed;top:0;left:0;right:0;z-index:50;
  display:flex;align-items:center;justify-content:space-between;
  padding:18px 5vw;
  background:linear-gradient(180deg, rgba(12,21,48,.92), rgba(12,21,48,0));
  backdrop-filter:blur(6px);
}
.logo{font-family:var(--font-display);font-size:1.4rem;color:var(--gold-bright);letter-spacing:.05em;}
.nav-links{display:flex;gap:26px;font-size:.85rem;letter-spacing:.03em;}
.nav-links a{opacity:.85;transition:opacity .2s, color .2s;}
.nav-links a:hover{opacity:1;color:var(--gold-bright);}
.nav-cta{
  background:linear-gradient(135deg,var(--gold),var(--gold-bright));
  color:var(--indigo-deep);
  padding:9px 20px;border-radius:2px;
  font-weight:600;font-size:.85rem;
  box-shadow:0 0 18px rgba(212,175,55,.35);
}
@media (max-width:820px){ .nav-links{display:none;} }

/* ---------- hero ---------- */
.hero{
  position:relative;
  min-height:100vh;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;
  padding:120px 5vw 80px;
  overflow:hidden;
  z-index:1;
}
.hero-eyebrow{
  font-size:.8rem;letter-spacing:.25em;text-transform:uppercase;color:var(--gold-bright);
  margin-bottom:22px;opacity:0;animation:fadeUp 1s ease forwards .1s;
}
.hero-portrait-wrap{
  position:relative;width:min(360px,70vw);margin:0 auto 10px;
  will-change:transform;
}
.hero-portrait{
  width:100%;display:block;border-radius:4px;
  filter:drop-shadow(0 30px 60px rgba(0,0,0,.55));
  opacity:0;animation:fadeUp 1.1s ease forwards .2s;
}
.hero-ring{
  position:absolute;inset:-26px;border:1px solid var(--gold);border-radius:50%;opacity:.35;
  animation:spin 40s linear infinite;
}
.hero h1{
  font-family:var(--font-display);
  font-size:clamp(2.6rem,7vw,5.2rem);
  font-weight:800;
  line-height:1;
  margin-top:28px;
  color:var(--ivory);
  opacity:0;animation:fadeUp 1s ease forwards .35s;
}
.hero h1 em{color:var(--gold-bright);font-style:normal;}
.hero .kanji-line{
  font-family:var(--font-script);
  font-size:1.2rem;letter-spacing:.08em;color:var(--ivory-dim);
  margin-top:14px;opacity:0;animation:fadeUp 1s ease forwards .5s;
}
.hero .tagline{
  font-style:italic;font-family:var(--font-script);
  font-size:1.25rem;color:var(--ivory-dim);margin-top:18px;max-width:520px;
  opacity:0;animation:fadeUp 1s ease forwards .6s;
}
.ca-pill{
  margin-top:30px;display:inline-flex;align-items:center;gap:10px;
  border:1px solid var(--gold);padding:10px 18px;border-radius:30px;
  font-size:.82rem;letter-spacing:.02em;cursor:pointer;
  background:rgba(212,175,55,.06);
  opacity:0;animation:fadeUp 1s ease forwards .7s;
  transition:background .2s;
}
.ca-pill:hover{background:rgba(212,175,55,.14);}
.hero-ctas{
  margin-top:28px;display:flex;gap:18px;flex-wrap:wrap;justify-content:center;
  opacity:0;animation:fadeUp 1s ease forwards .8s;
}
.btn{
  padding:15px 32px;border-radius:2px;font-weight:600;font-size:.9rem;letter-spacing:.03em;
  display:inline-flex;align-items:center;gap:8px;transition:transform .25s, box-shadow .25s;
}
.btn-primary{
  background:linear-gradient(135deg,var(--gold),var(--gold-bright));color:var(--indigo-deep);
  box-shadow:0 8px 28px rgba(212,175,55,.3);
}
.btn-primary:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(212,175,55,.45);}
.btn-ghost{
  border:1px solid var(--ivory-dim);color:var(--ivory);
}
.btn-ghost:hover{border-color:var(--gold-bright);color:var(--gold-bright);transform:translateY(-3px);}
.scroll-cue{
  margin-top:60px;font-size:.75rem;letter-spacing:.2em;color:var(--ivory-dim);
  display:flex;flex-direction:column;align-items:center;gap:8px;
}
.scroll-cue .line{width:1px;height:38px;background:linear-gradient(var(--gold),transparent);animation:dropline 1.8s ease-in-out infinite;}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:translateY(0);}}
@keyframes spin{from{transform:rotate(0);}to{transform:rotate(360deg);}}
@keyframes dropline{0%{transform:scaleY(0);opacity:0;}50%{transform:scaleY(1);opacity:1;}100%{transform:scaleY(0);opacity:0;transform-origin:bottom;}}

/* ---------- petals (parallax, scroll + float) ---------- */
.petal{
  position:fixed;top:-40px;z-index:2;pointer-events:none;
  width:18px;height:18px;
  background:radial-gradient(circle at 30% 30%, var(--gold-bright), var(--crimson) 80%);
  border-radius:60% 0% 60% 0%;
  opacity:.55;
  will-change:transform;
}

/* ---------- katana divider (signature element) ---------- */
.katana-divider{
  position:relative;height:140px;display:flex;align-items:center;justify-content:center;
  overflow:hidden;z-index:1;
}
.katana-svg{
  width:min(900px,90vw);
  filter:drop-shadow(0 0 14px rgba(212,175,55,.35));
  will-change:transform;
}

/* ---------- section shell ---------- */
section{position:relative;z-index:1;padding:120px 5vw;}
.section-head{text-align:center;max-width:760px;margin:0 auto 60px;}
.eyebrow{
  font-size:.78rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-bright);margin-bottom:16px;
}
.section-head h2{font-family:var(--font-display);font-size:clamp(2rem,4.2vw,3.2rem);color:var(--ivory);font-weight:800;}
.section-head h2 em{font-style:normal;color:var(--gold-bright);}
.section-sub{color:var(--ivory-dim);margin-top:14px;font-size:1rem;}

/* alternating section backgrounds */
.bg-mid{background:linear-gradient(180deg,var(--indigo-deep),var(--indigo-mid));}

/* ---------- video ---------- */
.video-wrap{
  max-width:880px;margin:0 auto;border:1px solid rgba(212,175,55,.3);
  border-radius:6px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.5);
}
.video-wrap iframe{display:block;width:100%;aspect-ratio:16/9;border:0;}

/* ---------- trade ---------- */
.trade-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;max-width:1100px;margin:0 auto;}
@media (max-width:900px){.trade-grid{grid-template-columns:1fr;}}
.trade-card{
  background:linear-gradient(160deg, rgba(58,18,22,.5), rgba(12,21,48,.5));
  border:1px solid rgba(212,175,55,.22);
  border-radius:6px;padding:34px 28px;
  transition:transform .35s, border-color .35s, box-shadow .35s;
  display:flex;flex-direction:column;gap:14px;
}
.trade-card:hover{transform:translateY(-10px);border-color:var(--gold);box-shadow:0 24px 50px rgba(0,0,0,.4);}
.trade-tag{font-size:.72rem;letter-spacing:.15em;color:var(--gold-bright);text-transform:uppercase;}
.trade-card h3{font-family:var(--font-display);font-size:1.5rem;}
.trade-card p{color:var(--ivory-dim);font-size:.92rem;line-height:1.5;flex:1;}
.trade-card a{align-self:flex-start;color:var(--gold-bright);font-weight:600;font-size:.88rem;border-bottom:1px solid var(--gold-bright);padding-bottom:2px;}

.chart-frame{
  max-width:980px;margin:60px auto 0;border:1px solid rgba(212,175,55,.25);border-radius:6px;overflow:hidden;
}
.chart-frame-head{display:flex;justify-content:space-between;align-items:center;padding:16px 22px;border-bottom:1px solid rgba(212,175,55,.2);font-size:.85rem;}
.chart-frame iframe{width:100%;height:500px;border:0;display:block;}

/* ---------- lore ---------- */
.lore-layout{display:grid;grid-template-columns:1fr 1.3fr;gap:60px;max-width:1100px;margin:0 auto;align-items:start;}
@media (max-width:900px){.lore-layout{grid-template-columns:1fr;}}
.lore-portrait{position:relative;will-change:transform;}
.lore-portrait img{width:100%;border-radius:6px;box-shadow:0 30px 60px rgba(0,0,0,.5);}
.lore-text p{color:var(--ivory-dim);line-height:1.85;margin-bottom:20px;font-size:1.02rem;}
.lore-text strong{color:var(--gold-bright);font-weight:600;}
.oath-list{list-style:none;margin:24px 0;padding:0;}
.oath-list li{
  padding:12px 0 12px 30px;border-bottom:1px solid rgba(212,175,55,.15);
  position:relative;color:var(--ivory);font-size:.96rem;
}
.oath-list li::before{content:"⚔";position:absolute;left:0;color:var(--gold);}
.lore-text .btn{margin-top:10px;}

/* ---------- gallery ---------- */
.gallery-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;max-width:1100px;margin:0 auto;}
@media (max-width:900px){.gallery-grid{grid-template-columns:repeat(2,1fr);}}
.gallery-item{
  position:relative;overflow:hidden;border-radius:6px;aspect-ratio:1/1;
  border:1px solid rgba(212,175,55,.2);
}
.gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .6s ease;}
.gallery-item:hover img{transform:scale(1.08);}
.gallery-item::after{
  content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 60%,rgba(12,21,48,.85));
  opacity:0;transition:opacity .35s;
}
.gallery-item:hover::after{opacity:1;}

/* ---------- community ---------- */
.community-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;max-width:1000px;margin:0 auto;}
@media (max-width:820px){.community-grid{grid-template-columns:repeat(2,1fr);}}
.community-card{
  text-align:center;padding:32px 18px;border:1px solid rgba(212,175,55,.22);border-radius:6px;
  background:rgba(58,18,22,.35);
  transition:transform .3s, border-color .3s;
}
.community-card:hover{transform:translateY(-8px);border-color:var(--gold);}
.community-card .icon{font-size:1.8rem;margin-bottom:10px;display:block;}
.community-card .label{font-weight:600;font-size:.95rem;}
.community-card .sub{font-size:.78rem;color:var(--ivory-dim);margin-top:4px;}

/* ---------- footer ---------- */
footer{padding:60px 5vw 40px;text-align:center;border-top:1px solid rgba(212,175,55,.18);position:relative;z-index:1;}
.footer-logo{font-family:var(--font-display);font-size:1.6rem;color:var(--gold-bright);margin-bottom:18px;}
.footer-links{display:flex;gap:18px;justify-content:center;flex-wrap:wrap;font-size:.85rem;color:var(--ivory-dim);margin-bottom:24px;}
.footer-links a:hover{color:var(--gold-bright);}
.footer-meta{font-size:.78rem;color:var(--ivory-dim);opacity:.7;margin-bottom:18px;}
.disclaimer{max-width:680px;margin:0 auto;font-size:.74rem;line-height:1.6;color:var(--ivory-dim);opacity:.55;}

.reveal{opacity:0;transform:translateY(40px);transition:opacity .8s ease, transform .8s ease;}
.reveal.in{opacity:1;transform:translateY(0);}

@media (prefers-reduced-motion: reduce){
  *{animation-duration:.01ms !important;transition-duration:.01ms !important;}
}
</style>
</head>
<body>

<div class="wave-bg" id="waveBg"></div>
<div id="petals"></div>

<nav>
  <div class="logo">NEKO ⚔</div>
  <div class="nav-links">
    <a href="#trade">⚔ Trade</a>
    <a href="#lore">📜 Lore</a>
    <a href="#art">🖼 Gallery</a>
    <a href="#join">🐱 Clan</a>
    <a href="/litepaper">📄 Litepaper</a>
  </div>
  <a class="nav-cta" href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Buy $NEKO</a>
</nav>

<section class="hero">
  <div class="hero-eyebrow">⚔ Zenshin Clan · $NEKO on Base ⚔</div>
  <div class="hero-portrait-wrap" id="heroPortrait">
    <div class="hero-ring"></div>
    <img class="hero-portrait" src="https://i.ibb.co/wrgX2S3W/Gemini-Generated-Image-9hscr99hscr99hsc.png" alt="Neko the Samurai Cat">
  </div>
  <h1>Neko the <em>Samurai</em></h1>
  <div class="kanji-line">前進 · Zenshin · Forward Progress</div>
  <p class="tagline">"Warrior in a garden, claws sharpened on Base."</p>
  <div class="ca-pill" id="caPill">CA 0x2897...8453 📋 <span id="caCopiedTxt"></span></div>
  <div class="hero-ctas">
    <a class="btn btn-primary" href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Buy on Uniswap</a>
    <a class="btn btn-ghost" href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank">View Chart</a>
  </div>
  <div class="scroll-cue"><div class="line"></div>Scroll</div>
</section>

<div class="katana-divider"><svg class="katana-svg" id="katana1" viewBox="0 0 900 60" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="40" x2="860" y2="20" stroke="#c79a3b" stroke-width="2" opacity="0.6"/>
  <line x1="20" y1="40" x2="860" y2="20" stroke="#f0cf76" stroke-width="1" opacity="0.9"/>
  <circle cx="20" cy="40" r="6" fill="#7c2630" stroke="#c79a3b" stroke-width="1.5"/>
</svg></div>

<section class="bg-mid">
  <div class="section-head reveal">
    <div class="eyebrow">⚔ The Clan in Motion</div>
    <h2>Watch <em>Neko</em></h2>
  </div>
  <div class="video-wrap reveal">
    <iframe src="https://www.youtube.com/embed/I4_fKxAayRM?autoplay=1&mute=1&loop=1&playlist=I4_fKxAayRM&controls=1&modestbranding=1&rel=0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>
</section>

<section id="trade">
  <div class="section-head reveal">
    <div class="eyebrow">⚔ Trade $NEKO</div>
    <h2>Acquire Your <em>Blade</em></h2>
    <p class="section-sub">Three paths into the Zenshin Clan</p>
  </div>
  <div class="trade-grid">
    <div class="trade-card reveal">
      <span class="trade-tag">01 · Primary Exchange</span>
      <h3>Uniswap V3</h3>
      <p>Live V3 pool on Base chain. The primary arena for $NEKO warriors.</p>
      <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Swap Now →</a>
    </div>
    <div class="trade-card reveal">
      <span class="trade-tag">02 · Real-Time Data</span>
      <h3>Dexscreener</h3>
      <p>Live price, volume, and liquidity. Watch the Clan's strength grow.</p>
      <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank">View Chart →</a>
    </div>
    <div class="trade-card reveal">
      <span class="trade-tag">03 · Legacy Platform</span>
      <h3>Toshimart</h3>
      <p>Original launch platform. Where the Zenshin Clan was forged.</p>
      <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">View Token →</a>
    </div>
  </div>

  <div class="chart-frame reveal">
    <div class="chart-frame-head">
      <span>$NEKO Live Chart · Base Chain</span>
      <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank" style="color:var(--gold-bright);">Open Dexscreener →</a>
    </div>
    <iframe src="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e?embed=1&theme=dark&trades=0&info=0"></iframe>
  </div>
</section>

<div class="katana-divider"><svg class="katana-svg" id="katana2" viewBox="0 0 900 60" xmlns="http://www.w3.org/2000/svg">
  <line x1="880" y1="20" x2="40" y2="42" stroke="#c79a3b" stroke-width="2" opacity="0.6"/>
  <line x1="880" y1="20" x2="40" y2="42" stroke="#f0cf76" stroke-width="1" opacity="0.9"/>
  <circle cx="880" cy="20" r="6" fill="#7c2630" stroke="#c79a3b" stroke-width="1.5"/>
</svg></div>

<section id="lore" class="bg-mid">
  <div class="section-head reveal">
    <div class="eyebrow">⚔ The Legend</div>
    <h2>Neko <em>Lore</em></h2>
  </div>
  <div class="lore-layout">
    <div class="lore-portrait reveal" id="lorePortrait">
      <img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms">
    </div>
    <div class="lore-text reveal">
      <p>In the shadowed valleys of the Base chain, where cherry blossoms drift across digital winds and the blockchain rivers flow with ancient power, a legend was forged.</p>
      <p>From the mists of code and courage rose <strong>Neko the Samurai Cat</strong> — eternal leader of the Zenshin Clan. Zenshin is not just a name. It is the sacred principle: <strong>"Forward Progress"</strong> — advance steadily, honorably, and without unnecessary haste. With katana ever-ready and vision sharp as a blade's edge, Neko moves like the wind: quiet, fierce, and unstoppable.</p>
      <p>The Zenshin Clan are samurai cats sworn to <strong>Toshi the Emperor</strong>. Their oath is unbreakable:</p>
      <ul class="oath-list">
        <li>Defend Toshi</li>
        <li>Safeguard the holders</li>
        <li>Protect the Base ecosystem</li>
        <li>Preserve harmony no matter the threat</li>
      </ul>
      <p><strong>$NEKO</strong> is the living spirit of this legend. Born on the Base chain as a pure community memecoin, $NEKO is more than a token — it is the blade you wield to join the clan. Every holder becomes part of the saga. Every trade echoes the call of Zenshin. Every diamond hand strengthens the oath.</p>
      <p>Hold $NEKO. Walk with Neko. Join the Zenshin Clan. Forward progress awaits those who stand ready. <em>Zenshin.</em></p>
      <a class="btn btn-primary" href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Join the Clan</a>
    </div>
  </div>
</section>

<section id="art">
  <div class="section-head reveal">
    <div class="eyebrow">⚔ Clan Artwork</div>
    <h2>The <em>Gallery</em></h2>
  </div>
  <div class="gallery-grid">
    <div class="gallery-item reveal"><img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Samurai Portrait"></div>
    <div class="gallery-item reveal"><img src="https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png" alt="Neko in Cherry Blossoms"></div>
    <div class="gallery-item reveal"><img src="https://i.ibb.co/6cpdFyYv/image-24.jpg" alt="Clan Art"></div>
    <div class="gallery-item reveal"><img src="https://i.ibb.co/QF6cS9ZV/Neko-The-Samurai.png" alt="Clan Art"></div>
  </div>
</section>

<div class="katana-divider"><svg class="katana-svg" id="katana3" viewBox="0 0 900 60" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="40" x2="860" y2="20" stroke="#c79a3b" stroke-width="2" opacity="0.6"/>
  <line x1="20" y1="40" x2="860" y2="20" stroke="#f0cf76" stroke-width="1" opacity="0.9"/>
  <circle cx="20" cy="40" r="6" fill="#7c2630" stroke="#c79a3b" stroke-width="1.5"/>
</svg></div>

<section id="join" class="bg-mid">
  <div class="section-head reveal">
    <div class="eyebrow">⚔ The Community</div>
    <h2>Join the <em>Clan</em></h2>
  </div>
  <div class="community-grid">
    <a class="community-card reveal" href="https://x.com/NekoTheSamurai" target="_blank">
      <span class="icon">𝕏</span><span class="label">Follow on X</span><span class="sub">@NekoTheSamurai</span>
    </a>
    <a class="community-card reveal" href="https://t.me/toshimart" target="_blank">
      <span class="icon">✈️</span><span class="label">Telegram</span><span class="sub">Toshimart TG</span>
    </a>
    <a class="community-card reveal" href="https://discord.gg/yKreTaD6Ua" target="_blank">
      <span class="icon">🎮</span><span class="label">Discord</span><span class="sub">Neko Talk</span>
    </a>
    <a class="community-card reveal" href="https://warpcast.com/toshibase" target="_blank">
      <span class="icon">🟣</span><span class="label">Warpcast</span><span class="sub">Toshi Base</span>
    </a>
  </div>
</section>

<footer>
  <div class="footer-logo">Neko ⚔ $NEKO</div>
  <div class="footer-links">
    <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Uniswap</a> ·
    <a href="https://dexscreener.com/base/0xb91f6f222d0eba27e552344157b8a98daa60df9e" target="_blank">Dexscreener</a> ·
    <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" target="_blank">Toshimart</a> ·
    <a href="/litepaper">Litepaper</a>
  </div>
  <div class="footer-meta">© 2026 Neko on Base · Zenshin Clan</div>
  <p class="disclaimer">$NEKO is a meme coin created for entertainment purposes only. It has no intrinsic value, makes no promises of financial return, and should not be considered an investment. Cryptocurrency trading involves significant risk. Always do your own research (DYOR) before making any financial decisions. Not financial advice.</p>
</footer>

<script>
// ---- petals ----
const petalCount = 14;
const petalsWrap = document.getElementById('petals');
const petals = [];
for(let i=0;i<petalCount;i++){
  const p = document.createElement('div');
  p.className='petal';
  const left = Math.random()*100;
  const size = 10+Math.random()*14;
  p.style.left = left+'vw';
  p.style.width = size+'px';
  p.style.height = size+'px';
  p.dataset.speed = (0.3+Math.random()*0.9).toFixed(2);
  p.dataset.driftAmp = (20+Math.random()*40).toFixed(0);
  p.dataset.driftSpeed = (0.0008+Math.random()*0.0012).toFixed(5);
  p.dataset.phase = (Math.random()*Math.PI*2).toFixed(2);
  petalsWrap.appendChild(p);
  petals.push(p);
}

let lastScroll = window.scrollY;
function animateFrame(t){
  const scrollY = window.scrollY;
  // background wave parallax
  document.getElementById('waveBg').style.transform = `translateY(${scrollY*0.15}px)`;
  // hero portrait parallax (bold)
  const heroP = document.getElementById('heroPortrait');
  if(heroP) heroP.style.transform = `translateY(${scrollY*0.35}px) scale(${Math.max(0.85,1-scrollY*0.0004)})`;
  const loreP = document.getElementById('lorePortrait');
  if(loreP){
    const rect = loreP.getBoundingClientRect();
    const offset = (window.innerHeight - rect.top) * 0.08;
    loreP.style.transform = `translateY(${-offset}px)`;
  }
  // katana dividers rotate/slide on scroll
  ['katana1','katana2','katana3'].forEach((id,i)=>{
    const el = document.getElementById(id);
    if(!el) return;
    const rect = el.getBoundingClientRect();
    const progress = (window.innerHeight - rect.top) / window.innerHeight;
    const rot = (progress*10-3) * (i%2===0?1:-1);
    const slide = (progress*60-30);
    el.style.transform = `translateX(${slide}px) rotate(${rot}deg)`;
  });
  // petals fall + drift, loop
  petals.forEach(p=>{
    const speed = parseFloat(p.dataset.speed);
    let top = parseFloat(p.dataset.top || -40);
    top += speed*1.4 + scrollY*0.00001;
    if(top > window.innerHeight+40) top = -40;
    p.dataset.top = top;
    const amp = parseFloat(p.dataset.driftAmp);
    const dspeed = parseFloat(p.dataset.driftSpeed);
    const phase = parseFloat(p.dataset.phase);
    const drift = Math.sin(t*dspeed + phase)*amp;
    p.style.transform = `translate(${drift}px, ${top}px) rotate(${t*0.02+phase*40}deg)`;
  });
  requestAnimationFrame(animateFrame);
}
requestAnimationFrame(animateFrame);

// ---- reveal on scroll ----
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries)=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){ entry.target.classList.add('in'); }
  });
},{threshold:0.15});
revealEls.forEach(el=>io.observe(el));

// ---- CA copy ----
const caPill = document.getElementById('caPill');
const caFull = '0x28973c4ef9ae754b076a024996350d3b16a38453';
caPill.addEventListener('click',()=>{
  navigator.clipboard.writeText(caFull).then(()=>{
    document.getElementById('caCopiedTxt').textContent = ' Copied ✓';
    setTimeout(()=>{ document.getElementById('caCopiedTxt').textContent=''; },1800);
  });
});
</script>

</body>
</html>

