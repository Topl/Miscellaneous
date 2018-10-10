from web3 import Web3
from toplEthTX.contracts import ABI

class Local:
    def __init__(self):
        # Establish connection to Ethereum network
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:7545')) # for local dev

        # Set contract addresses as deployed on ethereum network
        self.arbits_presale_addr = '0x62834b754a9265bbab089ef2c36b1c9714055dc0' # replace this with the addr from deployment

    def add_to_whitelist(self, user_addr):
        # Set account to send from as the first account in the testnet list
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]

        # set the to address to it's checksummed value
        to_addr = self.w3.toChecksumAddress(self.arbits_presale_addr)

        #Use the address of the deployed contract and the contract abi loaded from the json file to create the contract instance
        contract = self.w3.eth.contract( address = to_addr, abi = ABI().arbits_presale)

        # Send the transaction and get back the transaction hash
        tx_hash = contract.functions.add_to_whitelist(self.w3.toChecksumAddress(user_addr)).transact()

        return Web3.toHex(tx_hash)