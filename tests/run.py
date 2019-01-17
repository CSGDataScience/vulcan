from flask import jsonify
from vulcan.service import VulcanService
from vulcan.server import VulcanServer
import logging


class TestService(VulcanService):
    def init(self, context=None):
        if context:
            return jsonify({'data': context['facility_mnemonic']})
        else:
            return "Wowo"

    def fetch_one(self, context=None):
        if context:
            return jsonify({'data': context['facility_mnemonic']})
        else:
            return "Wowo"

    def fetch_all(self, context=None):
        if context:
            return jsonify({'data': context['facility_mnemonic']})
        else:
            return "Wowo"


test_app = VulcanServer(__name__, service=TestService)

if __name__ == '__main__':
    test_app.run(debug=True)
