from flask import Flask, render_template_string, jsonify, request
from datetime import datetime
from time import sleep
import threading
import pandas as pd
import numpy as np
from polygon import RESTClient

app = Flask(__name__)

# Polygon key
client = RESTClient("2lm_5uIh9NF6hQkcOxJN85RL9Ta0xHjF")

# Assets for stocks and crypto
STOCKS = ["AAPL", "MSFT", "TSLA"]
CRYPTO = ["X:BTCUSD", "X:ETHUSD", "X:SOLUSD"]  # Added SOL for example

live_prices = {}
news_sentiment = {}

def update_prices():
    global live_prices
    while True:
        prices = {}
        for symbol in STOCKS + CRYPTO:
            try:
                sym = symbol.replace("X:", "").replace("USD", "")
                last = client.get_last_trade(symbol)
                prices[sym] = round(last.price, 2)
            except:
                prices[sym] = "N/A"
        live_prices = prices
        sleep(60)  # Update every minute

def update_sentiment():
    global news_sentiment
    while True:
        sentiment = {}
        for symbol in STOCKS + CRYPTO:
            try:
                news = client.get_news(symbol, limit=5)
                if news:
                    text = ' '.join([n.title + ' ' + n.description for n in news])
                    positive = text.lower().count('good') + text.lower().count('rise') + text.lower().count('gain')  # Simple sentiment
                    negative = text.lower().count('bad') + text.lower().count('fall') + text.lower().count('loss')
                    sentiment[symbol.replace("X:", "").replace("USD", "")] = "Positive" if positive > negative else "Negative" if negative > positive else "Neutral"
                else:
                    sentiment[symbol.replace("X:", "").replace("USD", "")] = "No News"
            except:
                sentiment[symbol.replace("X:", "").replace("USD", "")] = "N/A"
        news_sentiment = sentiment
        sleep(900)  # Update every 15 minutes

threading.Thread(target=update_prices, daemon=True).start()
threading.Thread(target=update_sentiment, daemon=True).start()

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

@app.route('/markets/<type>')
def markets(type):
    if type == 'crypto':
        return jsonify({k: live_prices.get(k, 'N/A') for k in [s.replace("X:", "").replace("USD", "") for s in CRYPTO]})
    elif type == 'stocks':
        return jsonify({k: live_prices.get(k, 'N/A') for k in STOCKS})
    return jsonify({})

@app.route('/sentiment')
def sentiment():
    return jsonify(news_sentiment)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    # Simple settings page placeholder
    return "Settings page - Dark/Light mode, API keys, etc. (Coming soon)"

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <style>
        :root {
            --bg: #f8fafc;
            --card: #ffffff;
            --text: #1e293b;
            --accent: #2563eb;
            --green: #059669;
            --red: #dc2626;
            --gray: #64748b;
        }
        [data-theme="dark"] {
            --bg: #0f172a;
            --card: #1e293b;
            --text: #e2e8f0;
            --accent: #3b82f6;
            --green: #10b981;
            --red: #ef4444;
            --gray: #64748b;
        }
        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
        }
        .sidebar {
            width: 240px;
            background: var(--card);
            padding: 30px 20px;
            box-shadow: 4px 0 20px rgba(0,0,0,0.1);
            position: fixed;
            height: 100vh;
            transition: 0.3s;
        }
        .logo {
            font-size: 1.8em;
            font-weight: 700;
            color: var(--accent);
            margin-bottom: 40px;
        }
        .menu-item { padding: 15px; border-radius: 8px; margin-bottom: 10px; cursor: pointer; transition: 0.3s; }
        .menu-item:hover { background: var(--accent); color: white; }
        .submenu { margin-left: 20px; display: none; }
        .menu-item.active .submenu { display: block; }
        .main { margin-left: 240px; padding: 40px; width: calc(100% - 240px); }
        .header { text-align: center; margin-bottom: 40px; }
        h1 { font-size: 2.5em; margin: 0; }
        .market-list { display: grid; gap: 20px; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); }
        .market-card { background: var(--card); border-radius: 12px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .market-symbol { font-size: 1.8em; font-weight: 600; color: var(--green); }
        .market-price { font-size: 1.6em; margin: 10px 0; }
        .market-sentiment { color: var(--gray); }
        .no-data { text-align: center; color: var(--gray); margin: 100px; font-size: 1.6em; }
        .theme-toggle { cursor: pointer; margin-top: 20px; }
        footer { text-align: center; margin-top: 80px; color: var(--gray); font-size: 0.9em; }
    </style>
</head>
<body data-theme="dark">
    <div class="sidebar">
        <div class="logo">TradeScout Pro</div>
        <div class="menu-item" onclick="showPage('dashboard')">Dashboard</div>
        <div class="menu-item" onclick="toggleSubmenu('markets')">Markets</div>
        <div class="submenu" id="markets-submenu">
            <div class="menu-item" onclick="showPage('crypto')">Cryptocurrency</div>
            <div class="menu-item" onclick="showPage('stocks')">Stocks</div>
        </div>
        <div class="menu-item" onclick="showPage('settings')">Settings</div>
        <div class="theme-toggle" onclick="toggleTheme()">🌙 Dark Mode</div>
    </div>
    <div class="main" id="main-content">
        <div id="dashboard-page">
            <div class="header">
                <h1>TradeScout Pro</h1>
            </div>
            <p class="no-data">Welcome to TradeScout Pro - Your real-time market viewer!</p>
        </div>
        <div id="crypto-page" style="display: none;">
            <h1>Cryptocurrency Markets</h1>
            <div class="market-list" id="crypto-list"></div>
        </div>
        <div id="stocks-page" style="display: none;">
            <h1>Stock Markets</h1>
            <div class="market-list" id="stocks-list"></div>
        </div>
        <div id="settings-page" style="display: none;">
            <h1>Settings</h1>
            <p>Settings coming soon - API keys, theme, etc.</p>
        </div>
    </div>
    <footer>Real-time prices from Polygon • Updates every minute</footer>
    <script>
        function toggleTheme() {
            const body = document.body;
            const text = document.querySelector('.theme-toggle');
            if (body.getAttribute('data-theme') === 'dark') {
                body.setAttribute('data-theme', 'light');
                text.textContent = '☀️ Light Mode';
            } else {
                body.setAttribute('data-theme', 'dark');
                text.textContent = '🌙 Dark Mode';
            }
        }
        function toggleSubmenu(id) {
            document.getElementById(id + '-submenu').style.display = document.getElementById(id + '-submenu').style.display === 'block' ? 'none' : 'block';
        }
        function showPage(page) {
            document.querySelectorAll('.main > div').forEach(d => d.style.display = 'none');
            document.getElementById(page + '-page').style.display = 'block';
            if (page === 'crypto') loadMarkets('crypto');
            if (page === 'stocks') loadMarkets('stocks');
        }
        async function loadMarkets(type) {
            try {
                const res = await axios.get('/markets/' + type);
                const data = res.data;
                let list = '';
                for (const sym in data) {
                    list += `
                        <div class="market-card">
                            <div class="market-symbol">${sym}</div>
                            <div class="market-price">${data[sym]}</div>
                            <div class="market-sentiment">Sentiment: Loading...</div>
                        </div>
                    `;
                }
                document.getElementById(type + '-list').innerHTML = list;
                updateSentiment();
            } catch (e) {
                document.getElementById(type + '-list').innerHTML = '<p class="no-data">No data available</p>';
            }
        }
        async function updateSentiment() {
            try {
                const res = await axios.get('/sentiment');
                const sent = res.data;
                document.querySelectorAll('.market-sentiment').forEach((el, i) => {
                    const sym = el.parentElement.querySelector('.market-symbol').textContent;
                    el.textContent = `Sentiment: ${sent[sym] || 'N/A'}`;
                });
            } catch (e) {}
        }
        showPage('dashboard');
    </script>
</body>
</html>
"""
