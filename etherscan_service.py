from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

class EtherscanService:
    def __init__(self):
        self.uri = 'https://api.etherscan.io/api'

    def addresses_by_contract(self, contract):
        addresses = []
        raw_json = self.connection(f"module=account&action=txlist&address={contract}&startblock=0&endblock=99999999&sort=asc&apikey={os.environ['ETHERSCAN_KEY']}")['result']

        for item in raw_json:
            if item['from'] not in addresses:
                addresses.append(item['from'])

        return addresses

    def count_of_addresses(self, contract):
        return str(len(self.addresses_by_contract(contract)))


    # def balance_by_address(self, addresses):
    #     batches = chunk(addresses, 20)
    #
    #     for batch in batches:
    #

    def addresses_in_common(self, contracts):
        set_1 = set(self.addresses_by_contract(contracts[0]))
        set_2 = set(self.addresses_by_contract(contracts[1]))
        return list(set_1.intersection(set_2))


    def connection(self, params):
        r = requests.get(f"{self.uri}?{params}")
        return r.json()
