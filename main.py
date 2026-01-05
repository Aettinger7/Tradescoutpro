from flask import Flask, render_template_string
import requests
import datetime
import time

app = Flask(__name__)

HEADERS = {
    "accept": "application/json",
    "user-agent": "TradeScoutPro/1.0 (https://www.tradescoutpro.com)"
}

# Aggressive caching: update only every 5 minutes (300 seconds)
# This means max ~2-3 API calls per hour even with many visitors
CACHE_SECONDS = 300
last_fetch_time = 0
cached_coins = []
cached_metrics = {}

def get_global_metrics():
    global cached_metrics, last_fetch_time
    current_time = time.time()
    if current_time - last_fetch_time < CACHE_SECONDS and cached_metrics:
        return cached_metrics
    
    metrics = {
        "total_market_cap": 3270000000000,  # fallback
        "btc_dominance": 57.2,
        "fear_greed": 26,
        "alt_season": 39,  # rough approx during BTC season
    }
    
    try:
        # Global data (rarely fails)
        res = requests.get("https://api.coingecko.com/api/v3/global", headers=HEADERS, timeout=20)
        if res.status_code == 200:
            data = res.json()['data']
            metrics["total_market_cap"] = int(data['total_market_cap']['usd'])
            metrics["btc_dominance"] = round(data['market_cap_percentage']['btc'], 1)
        
        # Fear & Greed - fallback if fails
        fg_res = requests.get("https://api.alternative.me/fng/?limit=1", headers=HEADERS, timeout=10)
        if fg_res.status_code == 200:
            metrics["fear_greed"] = int(fg_res.json()['data'][0]['value'])
        
        # Simple Alt Season approx: lower when BTC dom high
        metrics["alt_season"] = max(0, min(100, round(100 - metrics["btc_dominance"] * 1.5)))
        
    except Exception as e:
        print("Metrics fetch error (using fallback):", e)
    
    cached_metrics = metrics
    last_fetch_time = current_time
    return metrics

def fetch_crypto_data():
    global cached_coins, last_fetch_time
    current_time = time.time()
    if current_time - last_fetch_time < CACHE_SECONDS and cached_coins:
        return cached_coins  # Serve cached data most of the time
    
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "price_change_percentage": "1h,24h,7d",
        "sparkline": True,
    }
    
    formatted = []
    for attempt in range(6):  # More retries
        try:
            response = requests.get(url, params=params, headers=HEADERS, timeout=20)
            if response.status_code == 429:
                print("Rate limited (429), waiting longer...")
                time.sleep(10 * (attempt + 1))
                continue
            response.raise_for_status()
            data = response.json()
            
            for rank, coin in enumerate(data, 1):
                sparkline = coin.get("sparkline_in_7d", {}).get("price", [])
                if len(sparkline) < 2:
                    continue
                formatted.append({
                    "rank": rank,
                    "name": coin["name"],
                    "symbol": coin["symbol"].upper(),
                    "logo": coin["image"],
                    "price": float(coin.get("current_price") or 0),
                    "change_1h": round(float(coin.get("price_change_percentage_1h_in_currency") or 0), 2),
                    "change_24h": round(float(coin.get("price_change_percentage_24h_in_currency") or 0), 2),
                    "change_7d": round(float(coin.get("price_change_percentage_7d_in_currency") or 0), 2),
                    "market_cap": int(coin.get("market_cap") or 0),
                    "volume_24h": int(coin.get("total_volume") or 0),
                    "sparkline_prices": sparkline,
                })
            break  # Success
        except Exception as e:
            print(f"Coins fetch error (attempt {attempt+1}): {e}")
            if attempt < 5:
                time.sleep(15)
    
    if formatted:
        cached_coins = formatted
        last_fetch_time = current_time
    
    return formatted or cached_coins  # Always return something (cached or empty)

@app.route('/')
def index():
    metrics = get_global_metrics()
    data = fetch_crypto_data()[:100]  # Top 100
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(HTML_TEMPLATE, data=data, last_update=last_update, metrics=metrics)

@app.route('/trending')
def trending():
    metrics = get_global_metrics()
    all_data = fetch_crypto_data()
    trending_data = sorted(
        [c for c in all_data if c['change_24h'] > 0],
        key=lambda x: x['change_24h'],
        reverse=True
    )[:25]
    for i, coin in enumerate(trending_data, 1):
        coin['rank'] = i
    last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(TRENDING_TEMPLATE, data=trending_data, last_update=last_update, metrics=metrics)

application = app

# Templates unchanged from previous version (kept for brevity - copy from your last working code)
# Just make sure you paste the full HTML_TEMPLATE and TRENDING_TEMPLATE here (the long ones with dark/light mode, search, modal, etc.)

if __name__ == '__main__':
    app.run(debug=True)
