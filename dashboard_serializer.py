from flask import jsonify

class DashboardSerializer:

    def __init__(self):
        pass


    def render_json(dapp, users, oois, eoois):
        return jsonify({
            'dapp_info': dapp,
            'ooi': oois,
            'external_ooi': eoois,
            'users': users
        })
