from flask import Flask, render_template, request, jsonify
from web3 import Web3
from chainlink_web3.utils import ChainlinkUtils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price', methods=['POST'])
def get_price():
    asset_pair = request.form['asset_pair']
    # Setup Web3 and chainlink-web3 (use appropriate contract address and API)
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_KEY'))
    chainlink = ChainlinkUtils(w3=w3)
    price = chainlink.get_price(asset_pair)  # Modify as per the actual usage
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
