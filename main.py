from flask import Flask
import requests
import datetime

app = Flask(__name__)

# Your CoinGecko Demo API key
CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

# List of coins to track
COINS = ["bitcoin", "ethereum", "solana", "ripple", "cardano", "dogecoin", "litecoin", "polygon"]

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(COINS),
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_market_cap": "true",
        "include_24h_vol": "true",
        "x_cg_demo_api_key": CG_API_KEY  # This uses your dedicated key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        formatted_data = []
        for coin in COINS:
            info = data.get(coin, {})
            formatted_data.append({
                "name": coin.capitalize(),
                "price": info.get("usd", 0),
                "change_24h": info.get("usd_24h_change", 0),
                "market_cap": info.get("usd_market_cap", 0),
                "volume_24h": info.get("usd_24h_vol", 0)
            })
        
        last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return formatted_data, last_update
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

@app.route('/')
def index():
    crypto_data, last_update = fetch_crypto_data()
    
    # Build table rows safely
    rows = ""
    for coin in crypto_data:
        change_class = "positive" if coin["change_24h"] > 0 else "negative"
        
        market_cap_display = f"${coin['market_cap']:,.0f}" if coin["market_cap"] else "N/A"
        volume_display = f"${coin['volume_24h']:,.0f}" if coin["volume_24h"] else "N/A"
        
        rows += f"""
        <tr>
            <td>{coin["name"]}</td>
            <td>${coin["price"]:,.2f}</td>
            <td class="{change_class}">{coin["change_24h"]:.2f}%</td>
            <td>{market_cap_display}</td>
            <td>{volume_display}</td>
        </tr>
        """
    
    # Main HTML template
    table_section = """
    <table>
        <thead>
            <tr>
                <th>Coin</th>
                <th>Price (USD)</th>
                <th>24h Change</th>
                <th>Market Cap</th>
                <th>24h Volume</th>
            </tr>
        </thead>
        <tbody>
            """ + rows + """
        </tbody>
    </table>
    """ if crypto_data else '<p style="text-align:center;color:#ff5555;">Failed to load data. Please try refreshing.</p>'
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Live Crypto Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #121212; color: #eee; margin: 0; padding: 20px; }}
            h1 {{ text-align: center; color: #00ffaa; }}
            table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
            th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #333; }}
            th {{ background: #1e1e1e; }}
            tr:hover {{ background: #2a2a2a; }}
            .positive {{ color: #00ffaa; }}
            .negative {{ color: #ff5555; }}
            .update {{ text-align: center; font-style: italic; color: #888; margin: 20px 0; }}
            .container {{ max-width: 1200px; margin: 0 auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Live Cryptocurrency Prices</h1>
            <div class="update">Last updated: {last_update}</div>
            
            {table_section}
            
            <div class="update">Refresh the page to update prices</div>
        </div>
    </body>
    </html>
    """
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
