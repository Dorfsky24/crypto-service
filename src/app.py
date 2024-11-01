# # app.py
# from flask import Flask, jsonify
# import requests
# import logging

# app = Flask(__name__)
# logging.basicConfig(level=logging.INFO)

# COIN_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

# def fetch_crypto_data(crypto_name):
#     try:
#         response = requests.get(COIN_API_URL)
#         response.raise_for_status()
#         data = response.json()
#         return data.get(crypto_name, {})
#     except requests.exceptions.RequestException as e:
#         app.logger.error(f"Error fetching {crypto_name} data: {e}")
#         return {"error": "Failed to fetch data"}

# @app.route('/bitcoin', methods=['GET'])
# def get_bitcoin():
#     bitcoin_data = fetch_crypto_data("bitcoin")
#     return jsonify(bitcoin_data), 200 if 'error' not in bitcoin_data else 500

# @app.route('/ethereum', methods=['GET'])
# def get_ethereum():
#     ethereum_data = fetch_crypto_data("ethereum")
#     return jsonify(ethereum_data), 200 if 'error' not in ethereum_data else 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

###########################################################################################################

from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# API URLs
BITCOIN_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
ETHEREUM_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"

# API endpoint for Bitcoin price
@app.route('/bitcoin', methods=['GET'])
def get_bitcoin_price():
    try:
        response = requests.get(BITCOIN_API_URL)
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        return jsonify({"bitcoin_price_usd": bitcoin_price})
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Bitcoin price: {e}")
        return jsonify({"error": "Failed to fetch Bitcoin price"}), 500

# API endpoint for Ethereum price
@app.route('/ethereum', methods=['GET'])
def get_ethereum_price():
    try:
        response = requests.get(ETHEREUM_API_URL)
        response.raise_for_status()
        data = response.json()
        ethereum_price = data['ethereum']['usd']
        return jsonify({"ethereum_price_usd": ethereum_price})
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Ethereum price: {e}")
        return jsonify({"error": "Failed to fetch Ethereum price"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

