import json
import web3
import getpass

pr = getpass.getpass("Private Key: ")

with open('prFile','w') as f:
    f.write(json.dumps(web3.eth.Account.encrypt(pr, 'Xja^8gS7TQu4D#y77MM3')))