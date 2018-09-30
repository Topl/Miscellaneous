import jwt
# docs for pyJWT https://pyjwt.readthedocs.io/en/latest/usage.html
# This script is to make sure that I can correctly read in the key files and generate a JWT for use in sending to the API through postman

f = open('privateKey.pem')
prKey = f.read()
f.close()

f = open('publicKey.pem')
puKey = f.read()
f.close()

objToJWT = {
    'some': 'payload',
    'field': 'testField'
}

encodedJWT = jwt.encode(objToJWT, prKey, algorithm='RS256')
decodedJWT = jwt.decode(encodedJWT, puKey, algorithms='RS256')