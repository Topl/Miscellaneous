import jwt
# docs for pyJWT https://pyjwt.readthedocs.io/en/latest/usage.html
# This script is to make sure that I can correctly read in the key files and generate a JWT for use in sending to the API through postman

f = open('../keys/privateKey.pem')
prKey = f.read()
f.close()

f = open('../keys/publicKey.pem')
puKey = f.read()
f.close()

objToJWT = {
    "form_data": {
        "backsideImageData": "data:image/jpeg;base64",
        "btc": "0x2e0051c32F8B36D94F81c05A3fA5be119Ed768E0",
        "btc_type": "ETH",
        "city": "detroit",
        "country": "US",
        "dfp": "eyJJRHMiOnsiZGV2aWNlSUQiOiIxOXpEVEc4dW0yS21JaWE5cDdjSE9aR2ZoRUciLCJjb29raWVJRCI6IjE5ekRUR3BYVHJxdF$",
        "dob": "2005-01-01",
        "docCountry": "US",
        "docType": "DL",
        "email": "j@r.com",
        "full_name": "d",
        "gdpr_purpose": "",
        "last_name": "d",
        "phone": "2817759652",
        "phone_code": "+1",
        "scanData": "data:image/jpeg;base64",
        "show_address_list": [
            "US"
        ],
        "show_id_list": [
            ""
        ],
        "ssn": "",
        "state": "DC",
        "street": "1928 help rd.",
        "user_id": "",
        "version": "2",
        "zip_code": "77098"
    },
    "kyc_result": "ACCEPT",
    "tid": "77c2b90e8e1391c79c27c569ee425d9ca2a45d5fc838f773deb72df56a39176b"
}


encodedJWT = jwt.encode(objToJWT, prKey, algorithm='RS256')
decodedJWT = jwt.decode(encodedJWT, puKey, algorithms='RS256')
