from flask import Flask, redirect, request
from time import sleep

app = Flask(__name__)

@app.route('/')
def hello():
    # dumb comment
    return 'Site under construction'

@app.route('/redirect/<delay>')
@app.route('/redirect')
def redir(delay=3):
    try:
        temp_delay=int(delay)
        delay = temp_delay
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)
    sleep(delay)    
    return redirect('https://www.google.com', code=302)

