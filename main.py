<style>
    body {
        margin: 0;
        background: 
            linear-gradient(rgba(0, 0, 0, 0.92), rgba(0, 0, 0, 0.95)),
            url('https://i.postimg.cc/1zn9gsLR/image(24).jpg') no-repeat center center fixed;
        background-size: cover;
        color: #f5f5f5;                   /* light off-white */
        font-family: Arial, sans-serif;
        scroll-behavior: smooth;
        overflow-x: hidden;
        min-height: 100vh;
    }

    .header {
        background: rgba(10, 10, 15, 0.96);
        backdrop-filter: blur(12px);
        box-shadow: 0 4px 25px rgba(212, 175, 55, 0.18);   /* subtle gold shadow */
        position: fixed;
        top: 0;
        width: 100%;
        z-index: 1000;
        border-bottom: 1px solid rgba(212, 175, 55, 0.25);
    }

    .btn-buy {
        background: linear-gradient(135deg, #D4AF37, #B8860B);   /* gold gradient */
        color: #0f0f0f;                   /* near-black text */
        padding: 0.7rem 1.4rem;
        border-radius: 9999px;
        font-weight: bold;
        transition: all 0.35s ease;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        border: 2px solid #D4AF37;
        white-space: nowrap;
    }

    .btn-buy:hover {
        background: linear-gradient(135deg, #FFD700, #F5C842);
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 12px 40px rgba(255, 215, 0, 0.6);
        border: 2px solid #FFD700;
    }

    .section-title {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to right, #FFD700, #D4AF37, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 25px rgba(212, 175, 55, 0.6);
    }

    .card {
        background: rgba(15, 15, 25, 0.92);
        border: 2px solid rgba(212, 175, 55, 0.5);
        border-radius: 1.25rem;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
        transition: all 0.4s ease;
        width: 100%;
    }

    .card:hover {
        box-shadow: 0 15px 50px rgba(212, 175, 55, 0.35);
        transform: translateY(-6px);
        border-color: #FFD700;
    }

    .animate-spin-slow {
        animation: spin 36s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .glow-gold {                               /* replaced glow-blue */
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.7);
    }

    img {
        max-width: 100%;
        height: auto;
        display: block;
    }

    /* Art gallery images get subtle gold hover frame */
    #art .card:hover img {
        transform: scale(1.08);
        transition: transform 0.5s ease;
    }

    .toast {
        animation: popIn 0.4s ease forwards;
        background: #1a1a2e;
        border: 2px solid #D4AF37;
        color: #FFD700;
    }

    @keyframes popIn {
        from { transform: translate(-50%, 30px); opacity: 0; }
        to { transform: translate(-50%, 0); opacity: 1; }
    }

    /* Fix potential mobile/desktop background behavior */
    @media (max-width: 640px) {
        body {
            background-attachment: scroll;
            background-position: center top;
        }
        main {
            padding-top: 120px;
        }
        .header {
            padding: 1rem;
        }
        .btn-buy {
            padding: 0.6rem 1.2rem;
            font-size: 0.9rem;
        }
    }

    /* Ensure images stay visible and crisp */
    @media (min-width: 1024px) {
        #art .grid {
            gap: 2.5rem;   /* more breathing room on large screens */
        }
    }
</style>
