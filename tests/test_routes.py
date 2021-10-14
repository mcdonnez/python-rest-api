'''
Test routes in routes.py
'''
import json
import unittest
from flask import Flask
from app.utils.json_encoder import CamelCaseEncoder
from app import routes
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.json_encoder = CamelCaseEncoder
        self.client = self.app.test_client()

    def test_healthcheck(self):
        with self.app.test_request_context('/'):
            response = routes.healthcheck()
            self.assertEqual(json.loads(response[0].data), {"status": "ok"})
            self.assertEqual(response[1], 200)

if __name__ == '__main__':
    unittest.main()
