from flask import jsonify


class AddressSerializer:
    def __init__(self):
        pass

    def render_json(addresses):
        return jsonify({'Data':{'count': len(addresses),
                        'addresses': addresses}})
