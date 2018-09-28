# standard modules
from flask import Flask, request, jsonify
from flask_cors import CORS

# selfmade modules for defined tasks
from verifyJWT import parse_request
from recordJSONtoFile import recordJSON

# standard instantiantion of the api application through flask
app = Flask(__name__)

# applies the Access-Control-Allow-Origin property to the api route as required by IDM
CORS(app, resources={r"/kyc": {"origins":"*"}})

# setup the KYC route
@app.route("/kyc", methods=["POST"])
def processKYC():
    payload = parse_request(request.get_json()) # verify and retrieve JSON from JWT
    recordJSON(payload) # log JSON into text file

    return jsonify({"success":True})

@app.route("/test")
def testRoute():
    return "Hello World!"


# if __name__ == '__main__':
#     app.run(debug=True)