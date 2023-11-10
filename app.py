from flask import Flask, render_template, request, jsonify
from web3 import Web3
from chainlink_web3.utils import ChainlinkUtils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price', methods=['POST'])
def get_price():
    contract_address = request.form['contract_address']
    # Setup Web3 and chainlink-web3
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/efd567867c2d402aabae90e5eb57d24e'))
    chainlink = ChainlinkUtils(w3=w3)
    
    try:
        # Use the contract address to fetch the price
        price = chainlink.get_price(contract_address)
        return jsonify({'price': price})
    except Exception as e:
        # Log the error and send an error response
        app.logger.error(f"Error fetching price: {e}")
        return jsonify({'error': 'Error fetching price'}), 500

if __name__ == '__main__':
    app.run(debug=True)
