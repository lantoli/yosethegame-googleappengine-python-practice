from flask import Flask, render_template
app = Flask(__name__)

app.debug = True

@app.route('/flask/a')
def helloa():
    return 'returns: a'

@app.route('/flask/b/')
def hellob():
    return 'returns: b/'

@app.route('/flask/error')
def errorA():
    a = 1/0


@app.route('/flask/hello/')
@app.route('/flask/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def page_error(e):
    return 'Sorry, unexpected error', 200
