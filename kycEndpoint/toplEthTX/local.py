from web3 import Web3
from toplEthTX.contracts import ABI

class Local:
    def __init__(self):
        # Establish connection to Ethereum network
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:7545')) # for local dev

        # Set contract addresses as deployed on ethereum network
        self.arbits_presale_addr = '0x3fa49c8b2662f7dcbe5d27b88ec2cf6b30621673' # replace this with the addr from deployment
        self.iconiq_data_pipe_addr = '0xeb828a191f4911d0e371855450ed5d5d057b06b1' # replace this with the addr from deployment

    def setup_contract_tx(self, contract_addr_, abi_):
        # Set account to send from as the first account in the testnet list
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]
        #Use the address of the deployed contract and the contract abi loaded from the json file to create the contract instance
        return self.w3.eth.contract( address = self.w3.toChecksumAddress(contract_addr_), abi = abi_)

    def add_to_whitelist(self, user_addr):
        # Setup contract object
        contract = self.setup_contract_tx(self.iconiq_data_pipe_addr, ABI().icnq_data_pipe)
        # Send the transaction and get back the transaction hash
        return Web3.toHex(contract.functions.add_to_whitelist(self.w3.toChecksumAddress(user_addr)).transact())

    def set_iconiq_token_allotment(self, addr_):
        # Setup contract object
        contract = self.setup_contract_tx(self.iconiq_data_pipe_addr, ABI().icnq_data_pipe)
         # Send the transaction and get back the transaction hash
        return Web3.toHex(contract.functions.set_iconiq_token_amount(self.w3.toChecksumAddress(addr_), 18000000).transact())