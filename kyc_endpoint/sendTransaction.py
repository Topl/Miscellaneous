from web3 import Web3
import json, asyncio

##truffle_file should load the contract json created in the build folder after migration
# Path_Truffle =
# truffle_file = json.load(open(Path_Truffle + 'build/contracts/arbits_presale.json'))
arbits_presale_abi = truffle_file['abi']

##Use address of ethereum node
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

def main():
    print("Is connected?", web3.isConnected())
    web3.eth.defaultAccount = web3.eth.accounts[0]
    getAddressToWhitelist()
    ##Use the address of the deployed contract and the contract abi loaded from the json file to create the contract instance
    contract = web3.eth.contract(address=web3.toChecksumAddress("<contract address here>"), abi=arbits_presale_abi)
    tx_hash = contract.functions.add_to_whitelist("<address to whitelist here>").transact()
    # print(tx_hash)


if __name__ == '__main__':
    main()
