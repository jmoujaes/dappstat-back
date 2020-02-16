from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import requests

class EtherscanService:
    def __init__(self):
        self.uri = 'https://api.etherscan.io/api'

    def addresses_by_contract(self, contract):
        addresses = []
        raw_json = self.connection(f"module=account&action=txlist&address={contract}&startblock=9488528&endblock=99999999&sort=asc&apikey={os.environ['ETHERSCAN_KEY']}")['result']

        for item in raw_json:
            if item['from'] not in addresses:
                addresses.append(item['from'])

        return addresses

    def count_of_addresses(self, contract):
        return str(len(self.addresses_by_contract(contract)))


    def unique_users(self, contract, ooi_contracts):
        ooi_addresses = set()
        for c in ooi_contracts:
            ooi_addresses.union(set(self.addresses_by_contract(c)))

        user_addresses = self.addresses_by_contract(contract)

        for address in user_addresses:
            if address in ooi_contracts:
                user_addresses.remove(address)

        return user_addresses


    def addresses_in_common(self, contracts):
        if contracts:
            common = set(self.addresses_by_contract(contracts[0]))

        for contract in contracts[1:]:
            addresses = set(self.addresses_by_contract(contract))
            common.intersection_update(addresses)

        return len(list(common))


    def connection(self, params):
        r = requests.get(f"{self.uri}?{params}")
        return r.json()
