import json

class ABI:
    def __init__(self):
        with open('toplEthTX/artifacts/arbits_presale.json','r') as f:
            arbits_presale = json.load(f)
            self.arbits_presale = arbits_presale['abi']