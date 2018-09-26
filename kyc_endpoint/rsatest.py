from Crypto.PublicKey import RSA

key = RSA.generate(2048)
f = open('mykey.pem','wb')
f.write(key.exportKey('PEM') + '\n')
f.write(key.publickey().exportKey('PEM'))
f.close()

print(key.exportKey('PEM'))
print(key.publickey().exportKey('PEM'))