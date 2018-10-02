from web3 import Web3
import json


# Get API key for infura
with open('./keys/pr_infuraRinkebyAPI.txt','r') as infura:
    apiKey = infura.read()

##Establish connection to Ethereum network
w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/' + apiKey)) # for rinkeby testing

# Set contract addresses as deployed on rinkeby network
arbits_presale_addr = "0x4393CeF911B451ab098c6973a28C913326E9413E"

##ABI should be from the contract json created in the truffle build folder after migration
with open('./abi/arbits_presale.json','r') as f:
    arbits_presale_abi = json.load(f)
    arbits_presale_abi = arbits_presale_abi['abi']

# Setup contract instance
arbContract = w3.eth.contract(
    address=w3.toChecksumAddress(arbits_presale_addr), 
    abi=arbits_presale_abi
    )

def _getKey():
    with open('./keys/pr_eth0_keyfile') as keyfile: 
        return w3.eth.account.privateKeyToAccount(w3.eth.account.decrypt(keyfile.read(), 'tZn%FKkHQ8MmCNv&Ng9m'))

def main(user_addr):
    toplAcct = _getKey()

    txParams = {
        'from': w3.toChecksumAddress(toplAcct.address),
        'chainId': 4,
        'nonce': w3.eth.getTransactionCount(w3.toChecksumAddress(toplAcct.address)),
        'gas': 100000,
        'gasPrice': w3.eth.gasPrice,
    }

    rawTX = arbContract.functions.add_to_whitelist(w3.toChecksumAddress(user_addr)).buildTransaction(txParams)
    signTX = toplAcct.signTransaction(rawTX)
    w3.eth.sendRawTransaction(signTX.rawTransaction)

    return w3.toHex(w3.sha3(signTX.rawTransaction))