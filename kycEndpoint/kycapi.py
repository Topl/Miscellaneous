# standard modules
from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import datetime

# selfmade modules for defined tasks
import verifyJWT
from recordJSONtoFile import recordJSON
#import sendTransaction_Rinkeby as sendTx
import sendTransaction_Local as sendTx

# standard instantiantion of the api application through flask
app = Flask(__name__)

# Define function vars
errFilePath = lambda ts: './Logs/' + ts + '_errorLog'

# applies the Access-Control-Allow-Origin property to the api route as required by IDM
CORS(app, resources={r"/kyc": {"origins":"*"}})

# setup the KYC route
@app.route("/kyc", methods=["POST"])
def processKYC():
    try:
        payload = verifyJWT.parse_request(request) # verify and retrieve JSON from JWT
        recordJSON(payload) # log JSON into text file
        tx_hash = sendTx.main(payload['form_data']['btc']) # send KYC request via Infura API

        return jsonify({"success":True})

    except Exception as e:
        # Handle exceptions to the process by creating a logfile and 
        with open(errFilePath(datetime.datetime.now().strftime("%Y.%m.%d.%H%M")),'a+') as errFile:
            errFile.write(traceback.format_exc())

        return jsonify({"success":False})
    
  
    
    

@app.route("/test")
def testFunc():
    return "The server is up and running!"


if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(host='127.0.0.1', debug=True)
