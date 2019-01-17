"""
Vulcan Server Module
"""

from flask import Flask, request, jsonify
from vulcan.service import VulcanService


class BaseVulcanService(VulcanService):
    def init(self, context=None):
        return """VulcanService.init
        should return enough data to service a clients rendering
        of your resource.
        """

    def fetch_one(self, context=None):
        return "Fetch One Func"

    def fetch_all(self, context=None):
        return "Fetch One Func"


class VulcanServer:
    def __init__(self, import_name, service=BaseVulcanService):
        self._flask_server = Flask(__name__)
        self._service = service()
        self._initialize_endpoints()

    @property
    def flask_server(self):
        return self._flask_server

    def _handle_ping(self):
        return jsonify({'data': 'pong'})

    def _initialize_endpoints(self):
        self._flask_server.add_url_rule(
            '/api/ping', 'ping', self._handle_ping, methods=['GET', 'PUT'])
        self._flask_server.add_url_rule("/api/init", 'init',
                                        self._handle_init, methods=['GET', 'PUT'])
        self._flask_server.add_url_rule("/api/fetch-one", "fetch-one",
                                        self._handle_fetch_one, methods=['GET', 'PUT'])
        self._flask_server.add_url_rule("/api/fetch-all", "fetch-all",
                                        self._handle_fetch_all, methods=['GET', 'PUT'])

    def _handle_init(self):
        try:
            context = request.get_json()
            return self._service.init(context=context)
        except:
            return self._service.init()

    def _handle_fetch_one(self):
        try:
            context = request.get_json()
            return self._service.fetch_one(context=context)
        except:
            return self._service.fetch_one()

    def _handle_fetch_all(self):
        try:
            context = request.get_json()
            return self._service.fetch_all(context=context)
        except:
            return self._service.fetch_all()

    def run(self, debug=False, port=8080, load_dotenv=True, **options):
        self._flask_server.run(port=port, debug=debug,
                               load_dotenv=load_dotenv, **options)
