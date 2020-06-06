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
    data=getData()
    res= f'Hello from {data.get("name","Name-not-set")}'
    if "otherInstance" in data.keys():
        appName = data["otherInstance"]
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
    return getData().get("name","")

def getData():
    '''
    Returns data from config file
    '''
    data={}
    if os.path.exists("/app-data/config.json"):
        with open("/app-data/config.json") as jsonfile:
            data = json.load(jsonfile)
    return data

 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')