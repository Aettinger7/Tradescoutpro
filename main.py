from flask import Flask, render_template_string, jsonify, request
import requests
import datetime
import json

app = Flask(__name__)

CG_API_KEY = "CG-AmnUtrzxMeYvcPeRsWejUaHu"

def fetch_crypto_data():
 url = "https://api.coingecko.com/api/v3/coins/markets"
 params = {
 "vs_currency": "usd",
 "order": "market_cap_desc",
 "per_page": 100,
 "page": 1,
 "price_change_percentage": "1h,24h,7d",
 "sparkline": True,
 }
 headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}

 try:
 response = requests.get(url, params=params, headers=headers, timeout=15)
 response.raise_for_status()
 data = response.json()

 formatted_data = []
 for rank, coin in enumerate(data, 1):
 sparkline_prices = coin.get("sparkline_in_7d", {}).get("price", [])
 formatted_data.append({
 "rank": rank,
 "id": coin["id"],
 "name": coin["name"],
 "symbol": coin["symbol"].upper(),
 "logo": coin["image"],
 "price": coin["current_price"] or 0,
 "change_1h": round(coin.get("price_change_percentage_1h_in_currency") or 0, 2),
 "change_24h": round(coin.get("price_change_percentage_24h_in_currency") or 0, 2),
 "change_7d": round(coin.get("price_change_percentage_7d_in_currency") or 0, 2),
 "market_cap": coin["market_cap"] or 0,
 "volume_24h": coin["total_volume"] or 0,
 "sparkline_prices": sparkline_prices,
 })

 last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
 return formatted_data, last_update

 except Exception as e:
 print(f"Error fetching data: {e}")
 return [], "Error"

def fetch_trending_data():
 try:
 trending_url = "https://api.coingecko.com/api/v3/search/trending"
 headers = {"x-cg-demo-api-key": CG_API_KEY} if CG_API_KEY else {}
 trending_res = requests.get(trending_url, headers=headers, timeout=15)
 trending_res.raise_for_status()
 trending_json = trending_res.json()
 trending_items = trending_json.get('coins', [])
 ids = [item['item']['id'] for item in trending_items]

 if ids:
 markets_url = "https://api.coingecko.com/api/v3/coins/markets"
 markets_params = {
 "vs_currency": "usd",
 "ids": ','.join(ids),
 "order": "market_cap_desc",
 "per_page": 50,
 "page": 1,
 "sparkline": True,
 "price_change_percentage": "1h,24h,7d",
 }
 markets_res = requests.get(markets_url, params=markets_params, headers=headers, timeout=15)
 markets_res.raise_for_status()
 full_data = markets_res.json()

 order_map = {item['item']['id']: idx for idx, item in enumerate(trending_items)}
 full_data.sort(key=lambda c: order_map.get(c['id'], 999))

 formatted_data = []
 for rank, coin in enumerate(full_data, 1):
 sparkline_prices = coin.get("sparkline_in_7d", {}).get("price", [])
 formatted_data.append({
 "rank": rank,
 "id": coin["id"],
 "name": coin["name"],
 "symbol": coin["symbol"].upper(),
 "logo": coin["image"],
 "price": coin["current_price"] or 0,
 "change_1h": round(coin.get("price_change_percentage_1h_in_currency") or 0, 2),
 "change_24h": round(coin.get("price_change_percentage_24h_in_currency") or 0, 2),
 "change_7d": round(coin.get("price_change_percentage_7d_in_currency") or 0, 2),
 "market_cap": coin["market_cap"] or 0,
 "volume_24h": coin["total_volume"] or 0,
 "sparkline_prices": sparkline_prices,
 })
 last_update = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
 return formatted_data, last_update
 except Exception as e:
 print(f"Trending error: {e}")

 return fetch_crypto_data()

# Rest of the routes and HTML_TEMPLATE (same as last version)

application = app

if __name__ == '__main__':
 app.run(debug=True)
