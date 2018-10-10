from web3 import Web3
from toplEthTX.contracts import ABI
import toplEthTX.settings as settings

class Rinkeby:
    def __init__(self):
        ##Establish connection to Ethereum network
        self.w3 = Web3(Web3.HTTPProvider(settings.API_URL)) # for rinkeby testing

        # Set contract addresses as deployed on rinkeby network
        self.arbits_presale_addr = '0x4393CeF911B451ab098c6973a28C913326E9413E'
        self.icnq_token_addr = '0x5A22b87A9C0084D49Aa3cb25fD4Ba9aD50323576'
        self.iconiq_data_pipe_addr = '0xD86cdd3978D3b293d3e29C6B7eCD76a0360993d8'

    def _getKey(self):
        with open(settings.ETH_KEY_PATH) as keyfile: 
            return self.w3.eth.account.privateKeyToAccount(self.w3.eth.account.decrypt(keyfile.read(), settings.ETH_PHRASE))

    def setup_contract_tx(self, contract_addr_, abi_):
        #Use the address of the deployed contract and the contract abi loaded from the json file to create the contract instance
        return self.w3.eth.contract( address = self.w3.toChecksumAddress(contract_addr_), abi = abi_)

    def get_tx_params(self, topl_addr_):
        # Specify tx_parameters
        return {
            'from': self.w3.toChecksumAddress(topl_addr_),
            'chainId': 4,
            'nonce': self.w3.eth.getTransactionCount(self.w3.toChecksumAddress(topl_addr_)),
            'gas': 100000,
            'gasPrice': self.w3.eth.gasPrice,
            }

    def add_to_whitelist(self, user_addr):
        # Unlock ethereum account
        toplAcct = self._getKey()

        # Setup contract instance
        _contract = self.setup_contract_tx(self.arbits_presale_addr, ABI().arbits_presale)

        # create various stages of the transaction
        rawTX = _contract.functions.add_to_whitelist(self.w3.toChecksumAddress(user_addr)).buildTransaction(self.get_tx_params(toplAcct.address))
        signTX = toplAcct.signTransaction(rawTX)

        # send the final signed transaction
        self.w3.eth.sendRawTransaction(signTX.rawTransaction)

        return self.w3.toHex(self.w3.sha3(signTX.rawTransaction))


    def check_icnq_balance(self, addr_):
        # Setup contract instance
        _contract = self.setup_contract_tx(self.icnq_token_addr, ABI().icnq_token)

        return _contract.functions.balanceOf(self.w3.toChecksumAddress(addr_)).call()


    def set_iconiq_token_allotment(self, addr_):
        # Unlock ethereum account
        toplAcct = self._getKey()

        # Setup contract instance
        _contract = self.setup_contract_tx(self.iconiq_data_pipe_addr, ABI().icnq_data_pipe)

        # create various stages of the transaction
        rawTX = _contract.functions.set_iconiq_token_amount(self.w3.toChecksumAddress(addr_), 18000000).buildTransaction(self.get_tx_params(toplAcct.address))
        signTX = toplAcct.signTransaction(rawTX)

        # send the final signed transaction
        self.w3.eth.sendRawTransaction(signTX.rawTransaction)

        return self.w3.toHex(self.w3.sha3(signTX.rawTransaction))
        
       