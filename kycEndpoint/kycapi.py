# standard modules
from flask import Flask, request, jsonify
from flask_cors import CORS

# selfmade modules for defined tasks
from verifyJWT import parse_request
from recordJSONtoFile import recordJSON
import sendTransaction_Rinkeby as sendTx

# standard instantiantion of the api application through flask
app = Flask(__name__)

# applies the Access-Control-Allow-Origin property to the api route as required by IDM
CORS(app, resources={r"/kyc": {"origins":"*"}})

# setup the KYC route
@app.route("/kyc", methods=["POST"])
def processKYC():
    payload = parse_request(request.get_json()) # verify and retrieve JSON from JWT
    recordJSON(payload) # log JSON into text file
    tx_hash = sendTx.main(payload['form_data']['btc'])

    #return jsonify({"success":True})
    return jsonify({"addr": payload['form_data']['btc'], "tx_hash": tx_hash})

@app.route("/test")
def testFunc():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(host='127.0.0.1', debug=True)
