from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_cors import CORS
from etherscan_service import EtherscanService
from address_serializer import AddressSerializer


app = Flask(__name__)
CORS(app)

@app.route("/<contract>/addresses", methods=['GET'])
def addresses(contract):
    e = EtherscanService()
    addresses = e.addresses_by_contract(contract)
    return AddressSerializer.render_json(addresses)

@app.route("/<contracts>/common-addresses", methods=['GET'])
def in_common(contracts):
    li_contracts = list(contracts.split(','))
    e = EtherscanService()
    addresses_in_common = e.addresses_in_common(li_contracts)
    return AddressSerializer.render_json(addresses_in_common)

@app.route("/unique-users", methods=['POST'])
def unique():
    data = request.json
    contract = data['contract']
    ooi_contracts = data['ooi_contracts']
    e = EtherscanService()
    addresses = e.unique_users(contract, ooi_contracts)
    return AddressSerializer.render_json(addresses)

@app.route("/dashboard-info-2", methods=['GET', 'POST'])
def dashboard():
    """
    Returns analysis on the given contract and category.
    """
    with open('fake-data.json') as fp:
        to_ret = json.load(fp)
        return to_ret


if __name__ == '__main__':
   app.run(debug = True)
