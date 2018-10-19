import jwt
# docs for pyJWT https://pyjwt.readthedocs.io/en/latest/usage.html
# This script is to make sure that I can correctly read in the key files and generate a JWT for use in sending to the API through postman

f = open('privateKey.pem')
prKey = f.read()
f.close()

# f = open('kycEndpoint/static/keys/publicKey.pem')
# puKey = f.read()
# f.close()

objToJWT = {
    "form_data": {
        "backsideImageData": "",
        "btc": "",
        "btc_type": "ETH",
        "city": "",
        "country": "",
        "dfp": "",
        "dob": "",
        "docCountry": "",
        "docType": "",
        "email": "",
        "full_name": "",
        "gdpr_purpose": "",
        "last_name": "",
        "phone": "",
        "phone_code": "",
        "scanData": "",
        "show_address_list": [
            ""
        ],
        "show_id_list": [
            ""
        ],
        "ssn": "",
        "state": "",
        "street": "",
        "user_id": "vip",
        "version": "",
        "zip_code": ""
    },
    "kyc_result": "ACCEPT",
    "tid": "0000000000000000000000000000000000000000000000000000000000000000"
}


encodedJWT = jwt.encode(objToJWT, prKey, algorithm='RS256')
#decodedJWT = jwt.decode(encodedJWT, puKey, algorithms='RS256')

with open('encodedJWT','w') as f:
    f.write(encodedJWT.decode('utf-8'))
