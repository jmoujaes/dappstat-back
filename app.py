from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_cors import CORS
from etherscan_service import EtherscanService
from address_serializer import AddressSerializer
from dashboard_serializer import DashboardSerializer
from dapp import Dapp


app = Flask(__name__)
CORS(app)

@app.route("/<contract>/addresses", methods=['GET'])
def addresses(contract):
    e = EtherscanService()
    addresses = e.addresses_by_contract(contract)
    return AddressSerializer.render_json(addresses)

@app.route("/analyze", methods=['POST'])
def analyze():
    e = EtherscanService()
    data = request.json
    dapp = Dapp.find_info_by_address(data['dapp_address'])
    users = Dapp.users(data['dapp_address'])
    oois =  Dapp.ooi_info(data['dapp_address'], data['category'])
    external_oois = Dapp.external_ooi_info(data['dapp_address'], data['category'])

    return DashboardSerializer.render_json(dapp, users, oois, external_oois)

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


if __name__ == '__main__':
   app.run(debug = True)
