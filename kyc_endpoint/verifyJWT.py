#this function is for verifying and decoding the jwt and returning the JSON to the API application
import jwt

# Identity Mind public keys are available at https://regtech.identitymind.store/accounts/d/%20
#f = open('./keys/publicKey.pem') # this is for locally generated testing
f = open('./keys/idmSandboxPubKey.pem') # Identitymind's sandbox public key
#f = open('./keys/idmProdPubKey.pem') # Identitymind's production public key

publicKey = f.read()
f.close()

def parse_request(req):
    # Parse and verify JWT token
    # payload = base64.standard_b64decode(jwtResponse[1])

    payload = jwt.decode(req['jwtresponse'], publicKey, algorithms='RS256')

    return payload