from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    # dumb comment
    return 'Site under construction'

