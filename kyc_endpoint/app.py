from flask import Flask, request, jsonify
from verifyJWT import parse_request

app = Flask(__name__)

@app.route("/kyc", methods=["POST"])
def processKYC():
    payload = parse_request(request.form.get('response'))
    return jsonify(payload)


if __name__ == '__main__':
    app.run(debug=True)