import webapp2
import webtest
import unittest
import main


class AppTest(unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication([('/', main.MainHandler)])
        self.testapp = webtest.TestApp(app)

    def test_hello_world(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertIn('Hello Yose', response.normal_body)
