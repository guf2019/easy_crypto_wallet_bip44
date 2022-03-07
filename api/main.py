from flask import Flask
import connexion
from connexion import request
from operations.ping import *
from operations.blockchain_info import get_blockNumber
from operations.account_info import get_eth_balance
from operations.mnemonic_phrase import generate_mnemonic_phrase
from config.constants import ServiceParameters

app = connexion.App(__name__, specification_dir='../documentation')

app.add_api('swagger.yml')

@app.route('/ping')
def ping_app():
    return pong()

@app.route('/generate_mnemonic_phrase')
def generate_mnemonic_phrase_app():
    return generate_mnemonic_phrase()

@app.route('/get_eth_balance')
def get_eth_balance_app(account_address):
    return get_eth_balance(account_address)

@app.route('/get_blocknumber')
def get_blockNumber_app():
    return get_blockNumber()

if __name__ == '__main__':
    print(f"Documentation to api be see on http://{ServiceParameters.HOST}:{ServiceParameters.PORT}/ui")
    app.run(host=ServiceParameters.HOST, port=ServiceParameters.PORT, debug=True)