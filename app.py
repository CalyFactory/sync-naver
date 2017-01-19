from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__,static_url_path='')

with open('key.json') as json_data:
    d = json.load(json_data)
    naverClientId = d['naver']['client_id']
    naverClientSecret = d['naver']['client_secret']

@app.route('/', methods=['GET', 'POST'])
def home():
    oAuthUrl = (
        "<html><a href='https://nid.naver.com/oauth2.0/authorize?response_type=code"+
        "&client_id=" + naverClientId + 
        "&redirect_uri=" + "http://localhost:5000/callback" +
        "&state='/>link</html>"
    )
    return oAuthUrl

@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')

    callbackAuthUrl = (
        "https://nid.naver.com/oauth2.0/token?grant_type=authorization_code"+
        "&client_id=" + naverClientId + 
        "&client_secret=" + naverClientSecret + 
        #"&redirect_uri=".$redirectURI.
        "&code=" + code 
#        "&state="
    )
    
    result = requests.post(callbackAuthUrl).json()
    print(result)
    return 'result : ' + str(result)



app.run(debug = True)
