from Crypto.PublicKey import RSA
# docs for Crypto followed from https://www.dlitz.net/software/pycrypto/api/2.6/
# docs for pyJWT https://pyjwt.readthedocs.io/en/latest/usage.html

key = RSA.generate(2048) #generate a new 256 byte RSA key

