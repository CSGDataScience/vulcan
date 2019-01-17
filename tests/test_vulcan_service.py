from vulcan.service import VulcanService
import unittest


class TestCreatingAVulcanService(unittest.TestCase):
    """Test creating and using a VulcanService"""

    def setUp(self):
        class TestService(VulcanService):
            def init(self, context):
                return []

            def fetch_all(self, context):
                return []

            def fetch_one(self, context):
                return 0

        self.service = TestService()

    def test_calling_init(self):
        self.assertIsNotNone(self.service.init(context={}))
