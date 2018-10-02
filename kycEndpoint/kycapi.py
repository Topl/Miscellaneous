# standard modules
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy
import traceback
import datetime
import os
import jwt

# selfmade modules for sending the ethereum transaction
#import sendTransaction_Rinkeby as sendTx
import sendTransaction_Local as sendTx

# Define error log location
errFilePath = lambda ts: './Logs/' + ts + '_errorLog'

# Define database location
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(os.path.sep, project_dir, 'db', "localTestnet.db"))

# standard instantiantion of the api application through flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# applies the Access-Control-Allow-Origin property to the api route as required by IDM
CORS(app, resources={r"/kyc": {"origins":"*"}})

# Setup database
db = flask_sqlalchemy.SQLAlchemy(app)

# Database model for saving form data
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.String(80), nullable=False)
    form_submit = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    kyc_result = db.Column(db.String(15), nullable=False)
    eth_addr = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(80))
    addr_country = db.Column(db.String(2), nullable=False)
    doc_country = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return "<tid: {}, kyc: {}, eth: {}, email: {}, country: {} >".format(
            self.tid, self.kyc_result, self.eth_addr, self.email, self.addr_country)

## This function will verify and return the payload from the JWT
# Identity Mind public keys are available at https://regtech.identitymind.store/accounts/d/%20
def verifyJWT(req):
    # If request is Ajax based (from IDM) open their public key otherwise use the test
    pubKeyPath = 'idmSandboxPubKey.pem' if req.headers['origin'] == 'https://regtech.identitymind.store' else 'publicKey.pem'
    
    # Parse and verify JWT token
    reqJSON = req.get_json()
    with open('./keys/' + pubKeyPath) as publicKey:
        return jwt.decode(reqJSON['jwtresponse'], publicKey.read(), algorithms='RS256')


## setup the KYC route
@app.route("/kyc", methods=["POST"])
def processKYC():
    try:
        # verify and retrieve JSON from JWT
        payload = verifyJWT(request) 

        # construct database object and save participant data
        db.session.add(Participant(
            tid = payload['tid'],
            kyc_result = payload['kyc_result'],
            eth_addr = payload['form_data']['btc'],
            email = payload['form_data']['email'],
            addr_country = payload['form_data']['country'],
            doc_country = payload['form_data']['docCountry']
            )
        )
        db.session.commit()

        # send KYC request via Infura API
        tx_hash = sendTx.main(payload['form_data']['btc']) 

        return jsonify({"success":True})

    except Exception as e:
        # Handle exceptions to the process by creating a logfile and 
        with open(errFilePath(datetime.datetime.now().strftime("%Y.%m.%d.%H%M")),'a+') as errFile:
            errFile.write(traceback.format_exc())

        return jsonify({"success":False})

## Setup a testing route
@app.route("/test")
def testFunc():
    return "The server is up and running!"


if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(host='127.0.0.1', debug=True)