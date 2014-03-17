from flask import Flask
app = Flask(__name__)

@app.route('/flask/hello')
def hello():
    return 'Hello World Flask!'

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def page_not_found(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
