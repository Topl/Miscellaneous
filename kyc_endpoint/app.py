from flask import Flask, request, jsonify
from flask_cors import CORS
from verifyJWT import parse_request
from recordJSONtoFile import recordJSON

app = Flask(__name__)
CORS(app)

g = open('idmResp.txt','a+')

@app.route("/kyc", methods=["POST"])
def processKYC():
    #payload = parse_request(request.form.get('response'))
    #payload = parse_request(request.get_json())

    recordJSON(request.get_json())
    return jsonify(request.get_json())
    #return jsonify(payload)


if __name__ == '__main__':
    app.run(debug=True)