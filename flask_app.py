from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    # dumb comment
    return 'Site under construction'

@app.route('/redirect')
def redirect():
    return redirect('https://wwww.google.com')

