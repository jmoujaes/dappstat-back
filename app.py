from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from etherscan_service import EtherscanService
import requests

app = Flask(__name__)
CORS(app)

@app.route("/<contract>/addresses", methods=['GET'])
def address(contract):
    e = EtherscanService()
    return e.addresses_by_contract(contract)

if __name__ == '__main__':
   app.run(debug = True)
