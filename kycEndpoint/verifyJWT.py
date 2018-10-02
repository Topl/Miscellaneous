#this function is for verifying and decoding the jwt and returning the JSON to the API application
import jwt
from flask import request

# Identity Mind public keys are available at https://regtech.identitymind.store/accounts/d/%20

def parse_request(req):
    # If request is Ajax based (from IDM) open their public key otherwise use the test
    pubKeyPath = 'idmSandboxPubKey.pem' if req.is_xhr else 'publicKey.pem'
    
    # Parse and verify JWT token
    reqJSON = req.get_json()
    with open('./keys/' + pubKeyPath) as publicKey:
        return jwt.decode(reqJSON['jwtresponse'], publicKey.read(), algorithms='RS256')