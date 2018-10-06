from web3 import Web3
from toplEthTX.contracts import ABI

class Rinkeby:
    def __init__(self):
        # Get API key for infura
        with open('toplEthTX/keys/pr_infuraRinkebyAPI','r') as infura:
            apiKey = infura.read()

        ##Establish connection to Ethereum network
        self.w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/' + apiKey)) # for rinkeby testing

        # Set contract addresses as deployed on rinkeby network
        arbits_presale_addr = "0x4393CeF911B451ab098c6973a28C913326E9413E"

        # Setup contract instance
        self.arbContract = self.w3.eth.contract(
            address = self.w3.toChecksumAddress(arbits_presale_addr), 
            abi = ABI().arbits_presale
            )

    def _getKey(self):
        with open('toplEthTX/keys/pr_eth0_keyfile') as keyfile: 
            return self.w3.eth.account.privateKeyToAccount(self.w3.eth.account.decrypt(keyfile.read(), 'Xja^8gS7TQu4D#y77MM3'))

    def add_to_whitelist(self, user_addr):
        toplAcct = self._getKey()

        txParams = {
            'from': self.w3.toChecksumAddress(toplAcct.address),
            'chainId': 4,
            'nonce': self.w3.eth.getTransactionCount(self.w3.toChecksumAddress(toplAcct.address)),
            'gas': 100000,
            'gasPrice': self.w3.eth.gasPrice,
        }

        cs_user_addr = self.w3.toChecksumAddress(user_addr)

        rawTX = self.arbContract.functions.add_to_whitelist(cs_user_addr).buildTransaction(txParams)
        signTX = toplAcct.signTransaction(rawTX)
        self.w3.eth.sendRawTransaction(signTX.rawTransaction)

        return self.w3.toHex(self.w3.sha3(signTX.rawTransaction))