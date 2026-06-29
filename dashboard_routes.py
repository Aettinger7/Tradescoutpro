"""
Neko the Samurai — Treasury Dashboard route
Drop this into your existing Flask app (app.py) or import it as a blueprint.

Setup:
1. Get a free Basescan API key: https://basescan.org/myapikey
2. Set env var BASESCAN_API_KEY (on Render: Dashboard -> Environment)
3. Add this blueprint to your app.py:

    from dashboard_routes import dashboard_bp
    app.register_blueprint(dashboard_bp)

4. Visit /dashboard on your site.
"""

import os
import time
import requests
from flask import Blueprint, render_template, jsonify

dashboard_bp = Blueprint("dashboard", __name__)

# ---- CONFIG ----
TREASURY_ADDRESS = "0x77bf5a2fc20c64f46e118377af2f1acf364c0043"
NEKO_CONTRACT = "0x28973C4ef9ae754b076a024996350D3B16a38453"
BASESCAN_API_KEY = os.environ.get("BASESCAN_API_KEY", "")
BASESCAN_URL = "https://api.basescan.org/api"
DEXSCREENER_URL = f"https://api.dexscreener.com/latest/dex/tokens/{NEKO_CONTRACT}"

# Simple in-memory cache to avoid hammering free-tier rate limits
_cache = {"data": None, "ts": 0}
CACHE_SECONDS = 60


def _get_eth_balance():
    params = {
        "module": "account",
        "action": "balance",
        "address": TREASURY_ADDRESS,
        "tag": "latest",
        "apikey": BASESCAN_API_KEY,
    }
    r = requests.get(BASESCAN_URL, params=params, timeout=10)
    r.raise_for_status()
    wei = int(r.json().get("result", "0"))
    return wei / 1e18


def _get_neko_balance():
    params = {
        "module": "account",
        "action": "tokenbalance",
        "contractaddress": NEKO_CONTRACT,
        "address": TREASURY_ADDRESS,
        "tag": "latest",
        "apikey": BASESCAN_API_KEY,
    }
    r = requests.get(BASESCAN_URL, params=params, timeout=10)
    r.raise_for_status()
    raw = int(r.json().get("result", "0"))
    return raw / 1e18  # NEKO uses 18 decimals


def _get_recent_txs(limit=5):
    params = {
        "module": "account",
        "action": "txlist",
        "address": TREASURY_ADDRESS,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": limit,
        "sort": "desc",
        "apikey": BASESCAN_API_KEY,
    }
    r = requests.get(BASESCAN_URL, params=params, timeout=10)
    r.raise_for_status()
    result = r.json().get("result", [])
    if not isinstance(result, list):
        return []
    txs = []
    for tx in result[:limit]:
        txs.append({
            "hash": tx.get("hash", ""),
            "hash_short": tx.get("hash", "")[:10] + "...",
            "value_eth": int(tx.get("value", 0)) / 1e18,
            "timestamp": int(tx.get("timeStamp", 0)),
            "method": tx.get("functionName", "").split("(")[0] or "transfer",
        })
    return txs


def _get_market_data():
    r = requests.get(DEXSCREENER_URL, timeout=10)
    r.raise_for_status()
    pairs = r.json().get("pairs") or []
    if not pairs:
        return {}
    # Use the highest-liquidity pair
    pair = max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
    return {
        "price_usd": float(pair.get("priceUsd", 0) or 0),
        "price_change_24h": pair.get("priceChange", {}).get("h24", 0),
        "volume_24h": pair.get("volume", {}).get("h24", 0),
        "liquidity_usd": pair.get("liquidity", {}).get("usd", 0),
        "market_cap": pair.get("marketCap") or pair.get("fdv", 0),
        "dex_url": pair.get("url", "#"),
    }


def get_treasury_data(force_refresh=False):
    now = time.time()
    if not force_refresh and _cache["data"] and (now - _cache["ts"]) < CACHE_SECONDS:
        return _cache["data"]

    eth_balance = _get_eth_balance()
    neko_balance = _get_neko_balance()
    market = _get_market_data()
    recent_txs = _get_recent_txs()

    price = market.get("price_usd", 0)
    neko_value_usd = neko_balance * price
    # Rough ETH/USD — pull from market pair if it's an ETH pair, else fallback estimate
    eth_value_usd = eth_balance * 3000  # fallback estimate; replace with live ETH price feed if desired

    data = {
        "address": TREASURY_ADDRESS,
        "eth_balance": round(eth_balance, 6),
        "eth_value_usd": round(eth_value_usd, 2),
        "neko_balance": round(neko_balance, 2),
        "neko_value_usd": round(neko_value_usd, 2),
        "total_value_usd": round(eth_value_usd + neko_value_usd, 2),
        "market": market,
        "recent_txs": recent_txs,
        "updated_at": int(now),
    }
    _cache["data"] = data
    _cache["ts"] = now
    return data


@dashboard_bp.route("/dashboard")
def dashboard():
    try:
        data = get_treasury_data()
        error = None
    except Exception as e:
        data = None
        error = str(e)
    return render_template("dashboard.html", data=data, error=error)


@dashboard_bp.route("/api/treasury")
def api_treasury():
    """JSON endpoint for live refresh via JS without reloading the page."""
    try:
        data = get_treasury_data(force_refresh=True)
        return jsonify({"ok": True, "data": data})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
