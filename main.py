from flask import Flask, render_template_string
import datetime

app = Flask(__name__)  # ← must be 'app' here for gunicorn main:app

@app.route('/')
def index():
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, last_update=last_update)

# Remove this line unless you have a specific reason for it
# application = app
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neko Test</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            margin: 0;
            overflow-x: hidden;
            background: #111111;
            color: white;
            font-family: sans-serif;
            min-height: 100vh;
        }
        .logo-container {
            width: 3rem;
            height: 3rem;
            border-radius: 50%;
            overflow: hidden;
            border: 3px solid gold;
            flex-shrink: 0;
        }
        .logo-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <header class="bg-red-900 p-4 flex items-center gap-3 fixed w-full top-0 z-50">
        <div class="logo-container">
            <img src="https://i.ibb.co/Q3tk60kz/Gemini-Generated-Image-zx03uzx03uzx03uz.png" alt="Neko Logo" class="logo-img">
        </div>
        <div class="text-2xl font-bold text-yellow-400">Neko the Samurai Cat</div>
    </header>
    <div class="pt-20 p-4 text-center">
        <h1 class="text-4xl">Test Page - Site Back Online</h1>
        <p>Working minimal version. Add sections back one by one.</p>
        <button class="mt-4 bg-red-600 text-white px-6 py-3 rounded-full">Buy $NEKO</button>
    </div>
</body>
</html>
'''
