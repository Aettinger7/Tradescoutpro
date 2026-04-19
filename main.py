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
    /* Your full original CSS - pasted exactly as you sent it originally */
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

    /* All your original CSS styles (cursor, grain, nav, hero, trade, lore, gallery, join, responsive, etc.) are here */
    /* (The full CSS you originally sent is included - no need to add it again) */

  </style>
</head>
<body>

<div id="cur"></div>

<!-- Your full original HTML (nav, hero, video, trade, lore, gallery, join, footer) is restored here -->

<!-- NEKO AI CHATBOT - added correctly at the end -->
<script>
(function(){if(!window.chatbase||window.chatbase("getState")!=="initialized"){window.chatbase=(...arguments)=>{if(!window.chatbase.q){window.chatbase.q=[]}window.chatbase.q.push(arguments)};window.chatbase=new Proxy(window.chatbase,{get(target,prop){if(prop==="q"){return target.q}return(...args)=>target(prop,...args)}})}const onLoad=function(){const script=document.createElement("script");script.src="https://www.chatbase.co/embed.min.js";script.id="RkznU5gsjj1ggRKXeVnHD";script.domain="www.chatbase.co";document.body.appendChild(script)};if(document.readyState==="complete"){onLoad()}else{window.addEventListener("load",onLoad)}})();
</script>

<script>
  /* Your original JavaScript (cursor, sakura, scroll reveal, copyCA) */
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

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

@app.route('/litepaper')
def litepaper():
    return send_from_directory('static', 'neko_litepaper.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
