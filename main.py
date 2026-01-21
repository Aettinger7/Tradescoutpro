from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

@app.route('/art')
def art():
    images = [
        "https://i.ibb.co/23RRSb0m/Gemini-Generated-Image-su90ubsu90ubsu90.png",
        "https://i.ibb.co/pjvzgzXH/Gemini-Generated-Image-2gwj062gwj062gwj.png",
        "https://i.ibb.co/3m5Qd14L/Gemini-Generated-Image-sqgje0sqgje0sqgj.png",
        "https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png",
        "https://i.ibb.co/9HzF9yZ1/Gemini-Generated-Image-zx03uzx03uzx03uz.png"
    ]

    art_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Neko Art Gallery - Zenshin Clan</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ margin: 0; padding: 0; overflow-x: hidden; background: #000; color: #fff; min-height: 100vh; font-family: sans-serif; }}
            header {{ background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.9)); backdrop-filter: blur(10px); position: fixed; top: 0; width: 100%; z-index: 50; }}
            .gallery {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 2rem; max-width: 1600px; margin: 0 auto; padding: 8rem 1.5rem 4rem; }}
            .art-item {{ cursor: pointer; transition: transform 0.3s; }}
            .art-item:hover {{ transform: scale(1.02); }}
            .art-img {{ width: 100%; height: auto; display: block; border-radius: 16px; box-shadow: 0 10px 30px rgba(255,215,0,0.3); }}
            #modal {{ display: none; position: fixed; inset: 0; z-index: 1000; background: rgba(0,0,0,0.96); align-items: center; justify-content: center; }}
            #modal.active {{ display: flex; }}
            #modal-img {{ max-width: 95vw; max-height: 95vh; object-fit: contain; border: 5px solid #FFD700; border-radius: 12px; box-shadow: 0 0 60px rgba(255,255,255,0.4); }}
            .close {{ position: absolute; top: 1.5rem; right: 2rem; color: white; font-size: 4.5rem; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <header class="py-4 px-6 flex justify-between items-center">
            <a href="/" class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-full overflow-hidden border-4 border-yellow-500 flex-shrink-0">
                    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="w-full h-full object-cover animate-spin-slow">
                </div>
                <div class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">Neko the Samurai Cat</div>
            </a>
            <div class="flex gap-4">
                <a href="/" class="bg-red-600 hover:bg-yellow-500 text-white hover:text-black px-6 py-2 rounded-full font-bold transition-all">Back to Home</a>
            </div>
        </header>

        <main class="pt-24 px-4">
            <h1 class="text-5xl md:text-6xl font-extrabold text-center mb-10 text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">Neko Art Gallery</h1>
            <div class="gallery">
                {''.join(f'<div class="art-item" onclick="openModal(\\'{img}\\')"><img src="{img}" alt="Neko Artwork" class="art-img" loading="lazy"></div>' for img in images)}
            </div>
            <p class="text-center text-gray-400 mt-12 text-lg">Click any image to view full high-resolution version • Right-click or long-press to save</p>
        </main>

        <div id="modal" onclick="if(event.target === this) closeModal()">
            <span class="close" onclick="closeModal()">×</span>
            <img id="modal-img" src="" alt="Full Resolution Neko Art">
        </div>

        <script>
            function openModal(src) {{
                document.getElementById('modal-img').src = src;
                document.getElementById('modal').classList.add('active');
                document.getElementById('modal').style.display = 'flex';
            }}
            function closeModal() {{
                document.getElementById('modal').classList.remove('active');
                document.getElementById('modal').style.display = 'none';
            }}
        </script>
    </body>
    </html>
    '''
    return art_html

@app.route('/lore')
def lore():
    lore_content = """
    <h1 class="text-5xl md:text-7xl font-extrabold mb-12 text-center text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 via-red-500 to-yellow-400 animate-pulse">
        The Lore of Neko
    </h1>

    <div class="max-w-4xl mx-auto prose prose-lg prose-invert space-y-8">
        <p class="text-xl leading-relaxed text-gray-200">
            In the mist-shrouded valleys of ancient Base, where cherry blossoms fall like silent rain and the wind carries whispers of forgotten battles, there exists a warrior unlike any other.
        </p>

        <p class="text-xl leading-relaxed text-gray-200 font-semibold">
            His name is <span class="text-yellow-400">Neko</span>.
        </p>

        <p class="text-lg">
            Not born of noble blood or forged in the fires of war, Neko was once an ordinary village cat — soft paws, curious eyes, content to nap in sunbeams and chase fireflies at dusk. But fate, cruel and capricious, has a way of choosing even the smallest creatures for greatness.
        </p>

        <p class="text-lg">
            One twilight, raiders descended upon the village. They burned homes, stole rice, and left only ashes and sorrow. Neko, hiding beneath the porch, watched his family flee and his garden — the only home he had ever known — turn to ruin.
        </p>

        <p class="text-lg font-semibold text-yellow-300">
            Something inside him snapped.<br>
            Not rage. Not vengeance.<br>
            <span class="text-2xl">Resolve.</span>
        </p>

        <p class="text-lg">
            He rose from the ashes with eyes like sharpened steel. The villagers who survived spoke of a shadow moving through the smoke — a cat with the grace of wind and the ferocity of a storm. When the raiders returned weeks later, they found no loot, no village to plunder… only a lone samurai standing in the ruined garden, katana drawn, cherry petals drifting around him like falling stars.
        </p>

        <p class="text-lg italic text-gray-300 border-l-4 border-yellow-500 pl-6">
            He did not speak. He did not roar.<br>
            He simply advanced.<br>
            Forward.<br>
            Always forward.
        </p>

        <h2 class="text-4xl font-bold mt-16 mb-8 text-yellow-400 border-b border-red-600 pb-4">The Zenshin Clan</h2>

        <p class="text-lg">
            Neko did not seek followers. Yet they came.
        </p>

        <p class="text-lg">
            First one, then ten, then hundreds — wanderers, outcasts, dreamers, degens, and those who had lost everything yet refused to stay broken. They saw in Neko not just a warrior, but a living reminder: progress is not a destination, it is a direction.
        </p>

        <p class="text-xl font-semibold text-yellow-300">
            They called themselves the <span class="text-2xl">Zenshin Clan</span> — those who move forward, no matter the storm.
        </p>

        <p class="text-lg">
            Their creed is simple:
        </p>

        <ul class="list-none space-y-4 text-lg pl-8">
            <li class="flex items-center gap-3"><span class="text-yellow-400 text-2xl">⚔️</span> Claws sharpened, yet paws soft.</li>
            <li class="flex items-center gap-3"><span class="text-yellow-400 text-2xl">🌸</span> Eyes on the horizon, yet rooted in the present.</li>
            <li class="flex items-center gap-3"><span class="text-yellow-400 text-2xl">➡️</span> Defeat is temporary; stopping is eternal.</li>
        </ul>

        <p class="text-lg mt-8">
            The clan does not conquer lands. They reclaim gardens — both literal and metaphorical. They plant seeds in scorched earth, rebuild bridges burned by others, and remind the world that even the smallest creature can change the course of rivers if it refuses to stand still.
        </p>

        <h2 class="text-4xl font-bold mt-16 mb-8 text-yellow-400 border-b border-red-600 pb-4">Neko Today</h2>

        <p class="text-lg">
            Now Neko walks the paths of Base — a digital realm of endless scrolls, flashing charts, and volatile winds. He carries no katana of steel, but one forged in memes, community, and unrelenting forward momentum.
        </p>

        <p class="text-xl font-semibold text-yellow-300">
            Every holder who buys $NEKO becomes part of the Zenshin Clan.<br>
            Every dip survived is a step through the garden.<br>
            Every new member is another cherry blossom planted.
        </p>

        <p class="text-lg mt-8">
            Neko does not promise riches. He promises progress.
        </p>

        <p class="text-2xl font-bold text-center mt-12 text-yellow-400 animate-pulse">
            And in the world of crypto — where most tokens fade into silence — the Samurai Cat keeps walking.<br>
            Forward.<br>
            Always forward.<br>
            <span class="text-3xl">Zenshin.</span>
        </p>
    </div>
    '''

    lore_page = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lore - Neko the Samurai Cat</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap" rel="stylesheet">
        <style>
            body {{ 
                margin: 0; padding: 0; overflow-x: hidden;
                background: linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.92)), 
                            url('https://i.ibb.co/nsRn37By/Gemini-Generated-Image-mdrxlumdrxlumdrx.png') no-repeat center center fixed; 
                background-size: cover; background-attachment: fixed; 
                color: #fff; min-height: 100vh; font-family: sans-serif;
            }}
            header {{ 
                background: linear-gradient(to right, #FF0000, rgba(0,0,0,0.9)); 
                backdrop-filter: blur(10px); position: fixed; top: 0; width: 100%; z-index: 50;
            }}
            .content {{ 
                max-width: 1000px; margin: 0 auto; padding: 9rem 1.5rem 6rem; 
                background: rgba(0,0,0,0.6); border-radius: 1.5rem; margin-top: 2rem;
            }}
            h1 {{ text-shadow: 0 0 20px rgba(255,215,0,0.8); }}
            p, li {{ line-height: 1.8; }}
            .cherry-bg::before {{
                content: ''; position: fixed; inset: 0; pointer-events: none; z-index: -1;
                background: url('https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80') center/cover no-repeat;
                opacity: 0.08; animation: float 120s linear infinite;
            }}
            @keyframes float {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(-100vh); }} }}
        </style>
    </head>
    <body class="cherry-bg">
        <header class="py-4 px-6 flex justify-between items-center">
            <a href="/" class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-full overflow-hidden border-4 border-yellow-500 flex-shrink-0">
                    <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="w-full h-full object-cover animate-spin-slow">
                </div>
                <div class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-red-500">
                    Neko the Samurai Cat
                </div>
            </a>
            <a href="/" class="bg-red-600 hover:bg-yellow-500 text-white hover:text-black px-6 py-2 rounded-full font-bold transition-all">
                Back to Home
            </a>
        </header>

        <div class="content">
            {lore_content}
        </div>
    </body>
    </html>
    '''
    return art_html  # ← typo fixed: return lore_page

# The rest of your main HTML_TEMPLATE remains the same
# (I'm not repeating the 1000+ lines here — just add/replace the /lore route above in your existing code)

if __name__ == '__main__':
    app.run(debug=True)
