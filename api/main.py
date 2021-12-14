from flask import Flask
import connexion
from connexion import request
from operations.ping import *
from config.constants import ServiceParameters

app = connexion.App(__name__, specification_dir='../documentation')

app.add_api('swagger.yml')

@app.route('/ping')
def ping():
    return pong()

@app.route('/generate_mnemonic_phrase')
def generate_mnemonic_phrase():
    return generate_mnemonic_phrase()

if __name__ == '__main__':
    print(f"Documentation to api be see on http://{ServiceParameters.HOST}:{ServiceParameters.PORT}/ui")
    app.run(host=ServiceParameters.HOST, port=ServiceParameters.PORT, debug=True)