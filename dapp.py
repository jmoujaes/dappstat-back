import records
from etherscan_service import EtherscanService

class Dapp:
    def __init__():
        self.conn = records.database(Secrets.db_link)

    def find_info_by_address(address):
        result = self.conn.query(f"SELECT organizations.name, organizations.category FROM contracts INNER JOIN organizations ON organizations.id = contracts.organization_id WHERE contracts.address = {address}")
        return result[0]


    def dapps_by_category(category):
        result = self.conn.query(f"SELECT name FROM organizations WHERE category = {category}")
        names = []
        for result in results:
            names.append(result['name'])

        return names

    def ooi_info(contract, oois):
        result = {}
        e = EtherscanService()
        for ooi in oois:
            info = self.find_info_by_address(ooi)
            result.append({
            'name': info['name'],
            'category': info['category'],
            'shared_users': e.unique_users(contract, ooi)
            })

        return result

    def users(contract, oois):
        e = EtherscanService()
        count = len(e.addresses_by_contract(contract))
        shared = len(e.addresses_in_common(contract, oois))
        unique = len(e.unique_users(contract, oois))

        return {
            'count': count,
            'total_shared': shared,
            'total_unique': unique
        }
