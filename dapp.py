
import records

class Dapp:
    def __init__():
        self.conn = records.database('postgres://vummccgjanibtc:e7f4258876e39efe1670951cc47107e77d081a07306bc101ee38facbc6352cb7@ec2-184-72-236-57.compute-1.amazonaws.com:5432/dcj1957cfej19p')

    def find_name_by_address(address):
        result = self.conn.query(f"SELECT organizations.name FROM contracts INNER JOIN organizations ON organizations.id = contracts.organization_id WHERE contracts.address = {address}")
        return result[0]['name']


    def dapps_by_category(category):
        result = self.conn.query(f"SELECT name FROM organizations WHERE category = {category}")
        names = []
        for result in results:
            names.append(result['name'])

        return names
