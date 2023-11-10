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
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_KEY'))
    chainlink = ChainlinkUtils(w3=w3)
    
    # Here, use the contract address to fetch the price
    # This might involve using a specific method of the ChainlinkUtils class
    # or directly interacting with the contract at the given address
    # The exact implementation depends on how the ChainlinkUtils class is designed
    price = chainlink.get_price(contract_address)  # Modify based on actual method

    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
