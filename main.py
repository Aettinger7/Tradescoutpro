from flask import Flask, render_template_string
from datetime import datetime
from time import sleep
import threading
import pandas as pd
import numpy as np
from polygon import RESTClient

app = Flask(__name__)

# Your Polygon API key
client = RESTClient("2lm_5uIh9NF6hQkcOxJN85RL9Ta0xHjF")

# Assets to scan
ASSETS = ["AAPL", "MSFT", "TSLA", "X:BTCUSD", "X:ETHUSD"]

# Timeframes
TIMEFRAMES = ["1h", "4h", "1d"]

# Simple indicators
def rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def macd_histogram(close):
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd - signal

def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()

# Check for buy signal on one timeframe
def check_signal(df):
    if len(df) < 60:
        return None
    close = df['close']
    low = df['low']
    volume = df['volume']
    last = df.iloc[-1]

    score = 0
    reasons = []

    # RSI reclaim from oversold
    current_rsi = rsi(close).iloc[-1]
    prev_rsi = rsi(close).iloc[-2]
    if prev_rsi < 30 and current_rsi > 30:
        score += 30
        reasons.append("RSI reclaim from oversold")

    # MACD histogram positive and expanding
    hist = macd_histogram(close)
    if hist.iloc[-1] > 0 and hist.iloc[-1] > hist.iloc[-2] > hist.iloc[-3]:
        score += 25
        reasons.append("MACD histogram expansion")

    # Bullish EMA stack
    if last['close'] > ema(close, 10).iloc[-1] > ema(close, 20).iloc[-1] > ema(close, 50).iloc[-1]:
        score += 25
        reasons.append("Bullish EMA stack")

    # Volume expansion
    avg_vol = volume.rolling(20).mean().iloc[-1]
    if volume.iloc[-1] > 1.5 * avg_vol:
        score += 20
        reasons.append("Volume expansion")

    if score >= 70:
        recent_low = low.iloc[-20:].min()
        invalidation = recent_low - (close.iloc[-1] - recent_low) * 0.5  # simple stop
        return {
            "score": score,
            "reasons": ", ".join(reasons),
            "invalidation": round(invalidation, 2)
        }
    return None

# Global results
results = {
    "time": "Starting...",
    "signals": []
}

def scanner_loop():
    global results
    while True:
        signals = []
        for symbol in ASSETS:
            for tf in TIMEFRAMES:
                try:
                    multiplier = int(tf[:-1])
                    timespan = tf[-1]
                    if timespan == 'm':
                        timespan = 'minute'
                    elif timespan == 'h':
                        timespan = 'hour'
                    elif timespan == 'd':
                        timespan = 'day'
                    aggs = client.get_aggs(symbol, multiplier, timespan, "2025-01-01", "2026-01-03", limit=50000)
                    if not aggs:
                        continue
                    df = pd.DataFrame(aggs)
                    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                    df.set_index('timestamp', inplace=True)
                    df = df[['open', 'high', 'low', 'close', 'volume']]
                    signal = check_signal(df)
                    if signal:
                        signals.append({
                            "symbol": symbol.replace("X:", ""),
                            "timeframe": tf,
                            **signal
                        })
                except:
                    continue
        results = {
            "time": datetime.now().strftime("%b %d, %Y %H:%M"),
            "signals": signals
        }
        sleep(900)  # 15 minutes

threading.Thread(target=scanner_loop, daemon=True).start()

# Dashboard
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro</title>
    <meta http-equiv="refresh" content="60">
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(to bottom, #f0f8ff, #e0f2fe); color: #2c3e50; text-align: center; padding: 20px; margin: 0; }
        h1 { font-size: 3em; margin-bottom: 10px; }
        .subtitle { font-size: 1.3em; color: #3498db; margin-bottom: 30px; }
        .time { font-size: 1.4em; color: #2980b9; margin: 40px 0; }
        .signals { max-width: 800px; margin: 0 auto; }
        .signal { background: white; border-radius: 15px; padding: 25px; margin: 20px 10px; box-shadow: 0 6px 20px rgba(0,0,0,0.1); }
        .symbol { font-size: 2em; font-weight: bold; color: #27ae60; }
        .score { font-size: 1.8em; color: #e67e22; }
        .reasons { font-size: 1.2em; margin: 15px 0; }
        .invalidation { font-size: 1.2em; color: #c0392b; font-weight: bold; }
        .no-signal { font-size: 2em; color: #95a5a6; margin: 100px 20px; }
        footer { margin-top: 80px; color: #7f8c8d; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>🚀 TradeScout Pro</h1>
    <p class="subtitle">High-Probability Buy Signals for Stocks & Crypto</p>
    <div class="time">Last scan: {{ time }}</div>
    <div class="signals">
        {% if signals %}
            <h2>🎯 Strong Buy Opportunities</h2>
            {% for s in signals %}
                <div class="signal">
                    <div class="symbol">{{ s.symbol }} ({{ s.timeframe }})</div>
                    <div class="score">Confidence Score: {{ s.score }}/100</div>
                    <div class="reasons">{{ s.reasons }}</div>
                    <div class="invalidation">Invalidation below: ${{ s.invalidation }}</div>
                </div>
            {% endfor %}
        {% else %}
            <p class="no-signal">😴 No high-probability buy signals right now.<br>Scanner checking again in 15 minutes...</p>
        {% endif %}
    </div>
    <footer>Page auto-refreshes every minute • Scanner runs every 15 minutes</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, **results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
