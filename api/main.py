from flask import Flask
import connexion
from connexion import request
from operations.ping import *

app = connexion.App(__name__, specification_dir='../documentation')

app.add_api('swagger.yml')

@app.route('/ping')
def ping():
    return pong()

@app.route('/generate_mnemonic_phrase')
def generate_mnemonic_phrase():
    passphrase = request.args.get('passphrase')
    return generate_mnemonic_phrase(passphrase)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)