# A very simple flask app which supports two methods:
#   - return own instance name (via /name)
#   - tries to connect to other app instance and returns own and other name (via /)
# Own name and other instance address are read by /app-data/config.json
#
# author: Stephan Hüwe
# 
#

from flask import Flask
import urllib.request
import os,json

app = Flask(__name__)
 
@app.route('/')
def hello_docker():
    '''
    Returns own instance name and tries to get name from other instance.
    '''
    res= f'Hello from {os.environ.get("NAME","Name-not-set")}'
    appName = os.environ.get("CONNECT_TO")
    if appName is not None:
        url = appName+":5000/name"
        res += f'<br/> Try to call {url}'
        try:
            f = urllib.request.urlopen(url)
            res+="<br/>"+f'.. connected to {f.read().decode("utf-8")}'
        except:
            res+="<br/>"+f'.. unable to connect to {appName}'
    return res


@app.route('/name')
def get_name():
    '''
    Gets name of instance
    '''
    return os.environ.get("NAME","")
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')