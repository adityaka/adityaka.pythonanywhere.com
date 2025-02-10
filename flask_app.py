from flask import Flask, redirect, request
from time import sleep

app = Flask(__name__)

@app.route('/')
def hello():
    # dumb comment
    return 'Site under construction'

@app.route('/redirect')
@app.route('/redirect/<delay>')
def redir(delay=1):
    sleep(delay)    
    return redirect('https://www.google.com', code=302)

