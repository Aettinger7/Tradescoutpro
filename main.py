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

    /* === ALL YOUR ORIGINAL CSS STYLES GO HERE === */
    /* Paste your full <style> content from the previous version here (cursor, nav, hero, sections, responsive, etc.) */
    /* I kept it short in this message to avoid length issues, but keep everything you had. */

  </style>
</head>
<body>

<div id="cur"></div>

<!-- === YOUR FULL PAGE CONTENT (NAV, HERO, VIDEO, TRADE, LORE, GALLERY, JOIN) === -->
<!-- Paste all your sections here exactly as they were before -->

<!-- ── FOOTER ── -->
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

<!-- === NEKO AI CHATBOT (Chatbase) - CORRECTLY PLACED === -->
<script>
(function(){if(!window.chatbase||window.chatbase("getState")!=="initialized"){window.chatbase=(...arguments)=>{if(!window.chatbase.q){window.chatbase.q=[]}window.chatbase.q.push(arguments)};window.chatbase=new Proxy(window.chatbase,{get(target,prop){if(prop==="q"){return target.q}return(...args)=>target(prop,...args)}})}const onLoad=function(){const script=document.createElement("script");script.src="https://www.chatbase.co/embed.min.js";script.id="RkznU5gsjj1ggRKXeVnHD";script.domain="www.chatbase.co";document.body.appendChild(script)};if(document.readyState==="complete"){onLoad()}else{window.addEventListener("load",onLoad)}})();
</script>

<script>
  /* Your JavaScript (cursor, sakura petals, scroll reveal, copyCA) */
  const cur = document.getElementById('cur');
  document.addEventListener('mousemove', e => {
    cur.style.left = e.clientX + 'px';
    cur.style.top  = e.clientY + 'px';
  });
  document.querySelectorAll('a,button,.ca-pill,.tc,.clan-card,.gi').forEach(el => {
    el.addEventListener('mouseenter', () => cur.classList.add('big'));
    el.addEventListener('mouseleave', () => cur.classList.remove('big'));
  });

  const container = document.getElementById('sakura');
  for (let i = 0; i < 35; i++) {
    const p = document.createElement('div');
    p.className = 'petal';
    const size = 6 + Math.random() * 10;
    p.style.cssText = `left:${Math.random()*100}%; width:${size}px; height:${size*1.4}px; animation-duration:${7+Math.random()*10}s; animation-delay:${Math.random()*15}s; opacity:0;`;
    container.appendChild(p);
  }

  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

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
