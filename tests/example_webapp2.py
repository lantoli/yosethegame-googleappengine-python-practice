import unittest
import webapp2
import main


class TestHandlers(unittest.TestCase):
    def test_hello(self):
        request = webapp2.Request.blank('/')
        response = request.get_response(main.app)
        self.assertEqual(response.status_int, 200)
        self.assertIn('Hello Yose', response.body)

    def test_unallowed_metod(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        response = request.get_response(main.app)
        self.assertEqual(response.status_int, 405)

