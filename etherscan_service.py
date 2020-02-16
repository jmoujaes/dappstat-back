from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

class EtherscanService:
    def __init__(self):
        self.uri = 'https://api.etherscan.io/api'

    def addresses_by_contract(self, contract):
        addresses = []
        raw_json = self.connection(f"module=account&action=txlist&address={contract}&startblock=0&endblock=99999999&sort=asc&apikey=S6DZ4QDQ61QTV1HJ3WTH6A395MWH7C2AV3")['result']

        for item in raw_json:
            if item['from'] not in addresses:
                addresses.append(item['from'])

        return str(len(addresses))

    def connection(self, params):
        r = requests.get(f"{self.uri}?{params}")
        return r.json()
