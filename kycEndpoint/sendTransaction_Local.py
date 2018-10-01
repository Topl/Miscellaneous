from web3 import Web3
import json, asyncio

##Establish connection to Ethereum network
web3 = Web3(Web3.HTTPProvider('http://localhost:7545')) # for local dev

# Set contract addresses as deployed on ethereum network
arbits_presale_addr = "0x62834b754a9265bbab089ef2c36b1c9714055dc0" # replace this with the addr from deployment

##ABI should be from the contract json created in the truffle build folder after migration
with open('./abi/arbits_presale.json','r') as f:
    arbits_presale_abi = json.load(f)
    arbits_presale_abi = arbits_presale_abi['abi']

def main(user_addr):
    ## This is for local development
    print("Is connected?", web3.isConnected())
    web3.eth.defaultAccount = web3.eth.accounts[0]
    #Use the address of the deployed contract and the contract abi loaded from the json file to create the contract instance
    contract = web3.eth.contract(address=web3.toChecksumAddress(arbits_presale_addr), abi=arbits_presale_abi)
    tx_hash = contract.functions.add_to_whitelist(web3.toChecksumAddress(user_addr)).transact()
    print(Web3.toHex(tx_hash))
    return Web3.toHex(tx_hash)

    