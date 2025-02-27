from flask import Flask, redirect, Request, Response, make_response, send_file
from time import sleep
import config
import io
import git


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

@app.route('/update/<key>')
def update(key):
    badKeyResponse = Response(status=404, response=b"Don't know what do you want me to do")
    if not key:
        return badKeyResponse

@app.route('/repros/badcontentencoding', methods=['GET', 'POST'])
def bad_content_encoding():
    binary_data = b'This is some binary data.'
    file_like_object = io.BytesIO(binary_data)
    resp =  make_response(send_file(file_like_object, mimetype='application/octet-stream', as_attachment=True, download_name='bindata.bin'))
    resp.headers.set('Content-Type', 'application/octet=stream')
    resp.status_code = 200
    return resp
     
     
    
    
         