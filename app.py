from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from etherscan_service import EtherscanService
import requests

app = Flask(__name__)
CORS(app)

@app.route("/<contract>/addresses", methods=['GET'])
def addresses(contract):
    e = EtherscanService()
    addresses = e.addresses_by_contract(contract)
    return jsonify({'count': len(addresses), 'addresses': addresses})

@app.route("/<contracts>/common-addresses", methods=['GET'])
def in_common(contracts):
    li_contracts = list(contracts.split(','))
    e = EtherscanService()
    addresses_in_common = e.addresses_in_common(li_contracts)
    return jsonify({'shared_users': {'count': len(addresses_in_common), 'addresses': addresses_in_common}})

if __name__ == '__main__':
   app.run(debug = True)
