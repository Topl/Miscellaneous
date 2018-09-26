import jwt
# docs for pyJWT https://pyjwt.readthedocs.io/en/latest/usage.html

f = open('privateKey.pem')
prKey = f.read()
f.close()

f = open('publicKey.pem')
puKey = f.read()
f.close()

encodedJWT = jwt.encode({'some': 'payload'}, prKey, algorithm='RS256')
decodedJWT = jwt.decode(encodedJWT, puKey, algorithms='RS256')