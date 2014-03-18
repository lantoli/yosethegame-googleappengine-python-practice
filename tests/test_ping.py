import unittest
import webapp2
import ping


class TestPing(unittest.TestCase):
    def test_ping(self):
        response = webapp2.Request.blank('/ping').get_response(ping.app)
        self.assertEqual(response.status_int, 200)
        self.assertEqual('application/json', response.headers['content-type'])
        self.assertEqual({"alive": True}, response.json)
