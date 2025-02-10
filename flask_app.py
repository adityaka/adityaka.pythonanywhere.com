from flask import Flask, redirect, request
from time import sleep
import config

app = Flask(__name__,
            static_folder=config.MYAPP_CONFIG["static_directory"],
            template_folder=config.MYAPP_CONFIG["template_directory"])

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
    return redirect('/static/html/heavyone.html', code=302)

