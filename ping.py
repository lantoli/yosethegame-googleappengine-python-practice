import webapp2
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'application/json'
        self.response.write(json.dumps({'alive': True}))


app = webapp2.WSGIApplication([
    ('/ping', MainHandler)
], debug=True)
