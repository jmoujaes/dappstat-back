import records
import os

class Dapp:
    def __init__():
        self.conn = records.database(os.environ['DATABASE_URL'])

    def find_name_by_address(address):
        result = self.conn.query(f"SELECT organizations.name FROM contracts INNER JOIN organizations ON organizations.id = contracts.organization_id WHERE contracts.address = {address}")
        return result[0]['name']


    def dapps_by_category(category):
        result = self.conn.query(f"SELECT name FROM organizations WHERE category = {category}")
        names = []
        for result in results:
            names.append(result['name'])

        return names
