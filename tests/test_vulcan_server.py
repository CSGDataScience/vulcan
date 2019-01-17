from vulcan.service import VulcanService
from vulcan.server import VulcanServer
from flask import jsonify
from unittest import TestCase


class TestVulcanService(VulcanService):
    def init(self, context=None):
        if context:
            return jsonify({'wow': 'oh man', 'facility_mnemonic': context['facility_mnemonic']})
        return 'Init'

    def fetch_one(self, context=None):
        if context:
            return jsonify({'fetch_one': 0})
        return 'Fetch One'

    def fetch_all(self, context=None):
        if context:
            return jsonify({'fetch_all': []})
        return 'Fetch All'


class TestVulcanServer(TestCase):

    def setUp(self):
        app = VulcanServer(__name__, service=TestVulcanService)
        app.flask_server.config['TESTING'] = True
        self.app = app.flask_server.test_client()

    def test_init_route(self):
        resp = self.app.get('/api/init', data=dict(facility_mnemonic='COCBR'))
        self.assertEqual(resp.status_code, 200)
