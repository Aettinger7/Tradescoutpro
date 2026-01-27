from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Neko the Samurai Cat — $NEKO</title>

<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">

<style>
body {
  background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.9)),
    url("https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png")
    center/cover fixed;
  color: #ffffff;
}

.title {
  font-family: "Cinzel", serif;
  background: linear-gradient(90deg,#FFD700,#FF4500);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card {
  background: rgba(12,12,12,.9);
  border: 1px solid #8b0000;
  border-radius: 1rem;
  box-shadow: 0 10px 40px rgba(0,0,0,.6);
}

.btn-primary {
  background: linear-gradient(135deg,#FFD700,#FF4500);
  color: #000;
  padding: .9rem 1.8rem;
  border-radius: 9999px;
  font-weight: bold;
  transition: all .3s ease;
}

.btn-primary:hover {
  transform: scale(1.07);
  box-shadow: 0 0 35px rgba(255,215,0,.6);
}
</style>
</head>

<body>

<header class="fixed w-full top-0 z-50 bg-black/80 backdrop-blur border-b border-red-900">
  <div class="max-w-7xl mx-auto flex items-center justify-between px-6 py-4">
    <div class="flex items-center gap-4">
      <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png"
           class="w-12 h-12 rounded-full border-2 border-yellow-500">
      <span class="text-xl font-bold">Neko</span>
    </div>
    <nav class="flex gap-6 text-sm">
      <a href="#trade" class="hover:text-yellow-400">Trade</a>
      <a href="#chart" class="hover:text-yellow-400">Chart</a>
      <a href="#lore" class="hover:text-yellow-400">Lore</a>
      <a href="#join" class="hover:text-yellow-400">Join</a>
    </nav>
  </div>
</header>

<main class="pt-32 max-w-7xl mx-auto px-6">

<section class="grid lg:grid-cols-2 gap-12 items-center py-20">
  <div>
    <h1 class="text-6xl font-extrabold title mb-6">
      Join the Zenshin Clan
    </h1>
    <p class="text-xl text-gray-300 mb-6">
      “Forward Progress” — a warrior in the garden, claws sharpened on Base.
    </p>

    <div class="bg-black/70 inline-block px-6 py-4 rounded-xl font-mono mb-8">
      CA: 0x28973c4ef9ae754b076a024996350d3b16a38453
    </div>

    <div class="flex gap-4">
      <a href="https://app.uniswap.org/explore/tokens/base/0x28973c4ef9ae754b076a024996350d3b16a38453"
         target="_blank"
         class="btn-primary">
        Buy $NEKO
      </a>
      <a href="#chart" class="px-6 py-4 rounded-full border border-yellow-500">
        View Chart
      </a>
    </div>
  </div>

  <div>
    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png"
         class="rounded-3xl shadow-2xl border-4 border-yellow-500">
  </div>
</section>

<section id="chart" class="grid lg:grid-cols-3 gap-8 py-20">
  <div class="card p-8 space-y-4">
    <h3 class="text-2xl title">$NEKO Stats</h3>
    <p>Network: Base</p>
    <p>DEX: Uniswap V3</p>
    <p>Status: Live</p>
    <a href="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570"
       target="_blank"
       class="inline-block mt-4 text-yellow-400 underline">
      Open Dexscreener →
    </a>
  </div>

  <div class="card col-span-2 p-4">
    <iframe
      src="https://dexscreener.com/base/0x97380293b0a33f37d48c3ba21bc452894607e570?embed=1&theme=dark&trades=0&info=0"
      style="width:100%;height:420px;border:0;"
      loading="lazy">
    </iframe>
  </div>
</section>

<section id="lore" class="py-20">
  <div class="card p-10 max-w-4xl mx-auto">
    <h2 class="text-4xl title mb-6">Neko Lore</h2>
    <p class="text-lg text-gray-300 leading-relaxed">
      Neko walks the path of Zenshin — forward progress without haste.
      The warrior in the garden sharpens claws in silence, protecting what
      matters without seeking applause.
    </p>
  </div>
</section>

<section id="join" class="py-20 grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
  <a href="https://x.com/NekoTheSamurai" target="_blank" class="card p-6 text-center hover:scale-105 transition">X</a>
  <a href="https://t.me/toshimart" target="_blank" class="card p-6 text-center hover:scale-105 transition">Telegram</a>
  <a href="https://discord.com/invite/toshibase" target="_blank" class="card p-6 text-center hover:scale-105 transition">Discord</a>
  <a href="https://warpcast.com/toshibase" target="_blank" class="card p-6 text-center hover:scale-105 transition">Warpcast</a>
</section>

<footer class="text-center text-gray-500 py-12 border-t border-red-900">
  <p>DYOR • Not financial advice • © 2026 Neko</p>
  <p class="mt-2">Last update: {{ last_update }}</p>
</footer>

</main>
</body>
</html>
"""

@app.route("/")
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

application = app

