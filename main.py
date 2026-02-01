<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko the Samurai Cat - $NEKO on Base</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: #fff;
            background: url('https://example.com/japanese-background.jpg') no-repeat center center fixed;
            background-size: cover;
            background-opacity: 0.8; /* Note: Use rgba for overlay if needed */
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            text-align: center;
            padding: 20px 0;
        }
        .logo {
            width: 150px;
            height: auto;
        }
        .spin {
            animation: spin 10s linear infinite;
        }
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        section {
            padding: 40px 0;
            background: rgba(0, 0, 0, 0.6); /* Semi-transparent background for sections */
            margin-bottom: 20px;
            border-radius: 10px;
        }
        h1, h2 {
            text-align: center;
        }
        .buttons {
            text-align: center;
            margin: 20px 0;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            background: #000;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            border: 2px solid gold;
            transition: all 0.3s;
        }
        .button:hover {
            background: #333;
            box-shadow: 0 0 15px gold;
            transform: scale(1.05);
        }
        .chart-container {
            width: 100%;
            height: 500px;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .gallery img {
            width: 200px;
            height: auto;
            margin: 10px;
            border-radius: 10px;
        }
        .trending-list {
            list-style: none;
            padding: 0;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .trending-list li {
            background: rgba(255, 255, 255, 0.1);
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
        }
        footer {
            text-align: center;
            padding: 20px 0;
            background: rgba(0, 0, 0, 0.8);
        }
        /* Mobile optimizations */
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            section {
                padding: 20px 0;
            }
            .gallery img {
                width: 100%;
                margin: 5px 0;
            }
            .button {
                display: block;
                margin: 10px auto;
            }
        }
    </style>
</head>
<body>
    <header>
        <img src="https://example.com/neko-logo.png" alt="Neko Logo" class="logo spin">
        <h1>Neko the Samurai Cat - $NEKO on Base</h1>
    </header>

    <div class="container">

        <!-- Hero Section -->
        <section id="hero">
            <img src="https://example.com/hero-image.png" alt="Hero Neko" class="spin" style="display: block; margin: 0 auto; width: 300px;">
            <p style="text-align: center;">Welcome to the world of Neko, the fierce samurai cat protecting the Base ecosystem!</p>
        </section>

        <!-- Trade Section -->
        <section id="trade">
            <h2>Trade $NEKO</h2>
            <div class="buttons">
                <a href="https://app.uniswap.org/#/swap?outputCurrency=0x28973c4ef9ae754b076a024996350d3b16a38453&chain=base" class="button">Buy on Uniswap</a>
                <a href="https://base.org/" class="button">Buy on Base App</a>
                <a href="https://toshimart.com/" class="button">Buy on Toshimart</a>
            </div>
        </section>

        <!-- Chart Section -->
        <section id="chart">
            <h2>Neko Live Chart</h2>
            <div class="chart-container">
                <iframe src="https://dexscreener.com/base/0x28973c4ef9ae754b076a024996350d3b16a38453?embed=1&theme=dark&info=0" frameborder="0" style="width: 100%; height: 100%;"></iframe>
            </div>
        </section>

        <!-- Join Section -->
        <section id="join">
            <h2>Join the Community</h2>
            <p style="text-align: center;">Follow us on X, join Telegram, and become part of the Zenshin Clan!</p>
            <div class="buttons">
                <a href="https://x.com/" class="button">X (Twitter)</a>
                <a href="https://telegram.org/" class="button">Telegram</a>
            </div>
        </section>

        <!-- Lore Section -->
        <section id="lore">
            <h2>Lore of Neko the Samurai Cat</h2>
            <p>In the ancient lands of the Base ecosystem, where digital realms merge with timeless traditions, rises Neko, the legendary samurai cat. Born from the shadows of cherry blossoms and forged in the fires of blockchain battles, Neko leads the Zenshin Clan—a fierce group of warrior cats dedicated to protecting the Toshi emperor and the thriving Toshi community.</p>
            <p>The Zenshin Clan, meaning "forward progress" in the ancient tongue, stands as the unbreakable shield against chaos and deceit that threatens the harmony of the ecosystem. Under Neko's vigilant gaze, they patrol the digital frontiers, ensuring the safety of the emperor's realm and fostering growth within the community. Their code of honor emphasizes loyalty, courage, and innovation, inspiring all who join to push the boundaries of what's possible in the crypto world.</p>
            <p>But the threats are many: shadowy invaders seeking to disrupt the balance, treacherous scams that prey on the unwary, and volatile storms that shake the foundations of the market. Neko, with his razor-sharp katana and unyielding spirit, rallies the clan to defend the Toshi emperor's throne—a symbol of stability and prosperity. Through epic quests and strategic alliances, they safeguard the ecosystem, allowing innovation to flourish and the community to thrive.</p>
            <p>Join Neko and the Zenshin Clan in their eternal vigil. Together, we protect, we progress, we conquer. Zenshin!</p>
        </section>

        <!-- Art Section -->
        <section id="art">
            <h2>Art Gallery</h2>
            <div class="gallery">
                <img src="https://example.com/gemini-portrait1.png" alt="Gemini Portrait 1">
                <img src="https://example.com/gemini-portrait2.png" alt="Gemini Portrait 2">
                <img src="https://example.com/cherry-blossoms.png" alt="Cherry Blossoms">
                <img src="https://example.com/tweet-media1.png" alt="Tweet Media 1">
                <!-- Add more images here with IMGBB links provided by user -->
                <img src="https://example.com/new-art1.png" alt="New Art 1">
                <img src="https://example.com/new-art2.png" alt="New Art 2">
                <img src="https://example.com/new-art3.png" alt="New Art 3">
            </div>
        </section>

        <!-- Trending Section -->
        <section id="trending">
            <h2>Top 10 Trending Coins on Base</h2>
            <ul class="trending-list">
                <!-- Fixed top 5 trending (example placeholders; update with real data) -->
                <li>1. TOSHI ($TOSHI)</li>
                <li>2. BRETT ($BRETT)</li>
                <li>3. DEGEN ($DEGEN)</li>
                <li>4. HIGHER ($HIGHER)</li>
                <li>5. AERODROME ($AERO)</li>
                <!-- 5 popular Base ones -->
                <li>6. YUKI ($YUKI)</li>
                <li>7. MOTO ($MOTO)</li>
                <li>8. DOGINME ($DOGINME)</li>
                <li>9. NORMIE ($NORMIE)</li>
                <li>10. BENJI ($BENJI)</li>
            </ul>
        </section>

    </div>

    <footer>
        <p>&copy; 2026 Neko the Samurai Cat. All rights reserved. Zenshin! 🐱⚔️</p>
    </footer>

</body>
</html>

