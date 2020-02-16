import os
import records
from etherscan_service import EtherscanService

class Dapp:
    conn = records.Database(os.environ['DATABASE_URL'])

    def find_info_by_address(address):
        result = Dapp.conn.query(f"SELECT organizations.name, organizations.category FROM contracts INNER JOIN organizations ON organizations.id = contracts.organization_id WHERE contracts.address = '{address}'")
        return dict(result[0])


    def dapps_by_category(category):
        results = Dapp.conn.query("SELECT name, category FROM organizations WHERE category = '{0}'".format(category))
        names = []
        for result in results:
            names.append(result['name'])

        return names

    def dapps_by_other_categories(category):
        results = Dapp.conn.query("SELECT name, category FROM organizations WHERE category <> '{0}'".format(category))
        names = []
        for result in results:
            names.append(result['name'])

        return names

    def contracts_by_category(category):
        results = Dapp.conn.query("SELECT contracts.address FROM organizations INNER JOIN contracts ON organizations.id = contracts.organization_id WHERE organizations.category = '{0}'".format(category))
        addresses = []
        for result in results:
            addresses.append(result['address'])

        return addresses

    def contracts_by_other_categories(category):
        results = Dapp.conn.query("SELECT contracts.address FROM organizations INNER JOIN contracts ON organizations.id = contracts.organization_id WHERE organizations.category <> '{0}'".format(category))
        addresses = []
        for result in results:
            addresses.append(result['address'])

        return addresses

    def ooi_info(contract, category):
        result = []
        e = EtherscanService()

        oois = Dapp.contracts_by_category(category)
        for ooi in oois:
            info = Dapp.find_info_by_address(ooi)
            result.append({
            'name': info['name'],
            'category': info['category'],
            'shared_users': e.addresses_in_common([contract, ooi])
            })

        return result

    def external_ooi_info(contract, category):
        result = []
        e = EtherscanService()

        external_oois = Dapp.contracts_by_other_categories(category)
        for ooi in external_oois:
            info = Dapp.find_info_by_address(ooi)
            result.append({
            'name': info['name'],
            'category': info['category'],
            'shared_users': e.addresses_in_common([contract, ooi])
            })

        return result

    def users(contract):
        e = EtherscanService()
        count = len(e.addresses_by_contract(contract))

        return {
            'count': count,
        }
