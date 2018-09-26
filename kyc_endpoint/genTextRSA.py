from Crypto.PublicKey import RSA
import jwt
# docs for Crypto followed from https://www.dlitz.net/software/pycrypto/api/2.6/
# docs for pyJWT https://pyjwt.readthedocs.io/en/latest/usage.html

key = RSA.generate(2048) #generate a new 256 byte RSA key
f = open('mykey.pem','wb')
f.write(key.exportKey('PEM'))
f.write(key.publickey().exportKey('PEM'))
f.close()
privateKey = key.exportKey('PEM')
publicKey = key.publickey().exportKey('PEM')

encodedJWT = jwt.encode({'some': 'payload'}, privateKey, algorithm='RS256')
decodedJWT = jwt.decode(encodedJWT, publicKey, algorithms='RS256')