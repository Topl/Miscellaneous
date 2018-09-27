#this function is for verifying and decoding the jwt and returning to the API
import jwt

f = open('publicKey.pem')
publicKey = f.read()
f.close()

def parse_request(req):
    # Parse and verify JWT token
    #jwtResponse = req.split('.')
    #payload = base64.standard_b64decode(jwtResponse[1])

    payload = jwt.decode(req, publicKey, algorithms='RS256')

    return payload