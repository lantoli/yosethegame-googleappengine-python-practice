import os
import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):

        github = 'https://github.com/lantoli/yosethegame-googleappengine-python-practice'
        twitter = 'https://twitter.com/lantoli'

        template_values = {
            'contactme': twitter,
            'link': github,
            'pingsvc': '/ping',
            'pingcode': github + '/blob/master/ping.py'
        }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
