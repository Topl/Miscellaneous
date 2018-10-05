from Crypto.PublicKey import RSA
# docs for Crypto followed from https://www.dlitz.net/software/pycrypto/api/2.6/
# this function is to generate a public private key pair for use in creating and verifying JWT tokens

key = RSA.generate(2048) #generate a new 256 byte RSA key

f = open('privateKey.pem','wb')
f.write(key.exportKey('PEM'))
f.close()

f = open('publicKey.pem','wb')
f.write(key.publickey().exportKey('PEM'))
f.close()

#privateKey = key.exportKey('PEM')
#publicKey = key.publickey().exportKey('PEM')