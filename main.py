HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko the Samurai Cat - Official Memecoin Site</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            margin: 0;
            overflow-x: hidden;
            background: linear-gradient(to bottom, #111111, #1a1a1a);
            color: white;
            font-family: 'Segoe UI', sans-serif;
            min-height: 100vh;
        }
        .logo-container {
            width: 4rem;
            height: 4rem;
            border-radius: 50%;
            overflow: hidden;
            border: 4px solid #FFD700; /* gold */
            box-shadow: 0 0 15px rgba(255,215,0,0.5);
        }
        .logo-img { width: 100%; height: 100%; object-fit: cover; }
        .neko-red { color: #991B1B; } /* deep red for samurai vibe */
        .gold-text { color: #FFD700; }
    </style>
</head>
<body class="bg-black text-white">
    <!-- Header -->
    <header class="bg-gradient-to-r from-red-950 to-black p-4 flex items-center justify-between fixed w-full top-0 z-50 shadow-lg">
        <div class="flex items-center gap-4">
            <div class="logo-container">
                <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko the Samurai Cat Logo" class="logo-img">
            </div>
            <h1 class="text-2xl md:text-3xl font-bold gold-text">Neko the Samurai Cat</h1>
        </div>
        <div class="text-sm text-gray-400">Zenshin Clan – Forward Progress</div>
    </header>

    <!-- Main Content -->
    <main class="pt-24 pb-12 px-4 md:px-8 max-w-5xl mx-auto text-center">
        <h2 class="text-5xl md:text-6xl font-extrabold gold-text mb-6">Warrior in a Garden</h2>
        <p class="text-xl md:text-2xl mb-8 text-gray-300">Claws sharpened on Base. Join the Zenshin Clan.</p>

        <!-- Big Buy CTA -->
        <a href="https://toshimart.xyz/0x28973c4ef9ae754b076a024996350d3b16a38453" 
           target="_blank" rel="noopener noreferrer"
           class="inline-block bg-red-700 hover:bg-red-600 text-white text-2xl font-bold px-12 py-6 rounded-full shadow-2xl transform hover:scale-105 transition mb-12">
           Buy $NEKO Now on Toshimart
        </a>

        <!-- Token Info Card -->
        <div class="bg-gray-900/80 backdrop-blur-md p-8 rounded-2xl border border-gold-500/30 mb-12">
            <h3 class="text-3xl gold-text mb-6">Token Details</h3>
            <p class="text-lg mb-4">Contract Address (Base):</p>
            <div class="flex flex-col md:flex-row items-center justify-center gap-4 mb-6">
                <code class="bg-black px-4 py-2 rounded font-mono text-yellow-300 break-all">0x28973c4ef9ae754b076a024996350d3b16a38453</code>
                <button onclick="navigator.clipboard.writeText('0x28973c4ef9ae754b076a024996350d3b16a38453'); alert('CA copied!')" 
                        class="bg-gray-700 hover:bg-gray-600 px-4 py-2 rounded">Copy CA</button>
            </div>
            <p class="text-gray-400">Live on Toshimart Bonding Curve • Price rises with buys • Early holders win</p>
            <p class="mt-4 text-sm text-gray-500">Dexscreener coming after curve completion</p>
        </div>

        <!-- Socials -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-12">
            <a href="https://x.com/NekoTheSamurai" target="_blank" class="bg-gray-800 hover:bg-gray-700 p-6 rounded-xl">Follow @NekoTheSamurai on X</a>
            <a href="https://t.me/toshimart" target="_blank" class="bg-gray-800 hover:bg-gray-700 p-6 rounded-xl">Toshimart Telegram</a>
            <a href="https://discord.com/invite/toshibase" target="_blank" class="bg-gray-800 hover:bg-gray-700 p-6 rounded-xl">Toshi Base Discord</a>
            <a href="https://warpcast.com/toshibase" target="_blank" class="bg-gray-800 hover:bg-gray-700 p-6 rounded-xl">Toshi Base Warpcast</a>
        </div>

        <!-- Status / Last Update -->
        <p class="text-sm text-gray-500">Site last updated: {{ last_update }}</p>
        <p class="text-sm text-gray-600 mt-2">Bonding curve at ~99% – clan growing fast. Zenshin!</p>
    </main>
</body>
</html>
'''
