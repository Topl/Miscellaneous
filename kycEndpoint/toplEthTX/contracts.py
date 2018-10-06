import json

class ABI:
    def __init__(self):

        def read_artifact(contract):
            artifact_path = 'toplEthTX/artifacts/'

            with open(artifact_path + contract +'.json','r') as f:
                contract_artifact = json.load(f)
                return contract_artifact['abi']

        self.database = read_artifact('database')
        self.arbits_presale = read_artifact('arbits_presale')
        self.iconiq_presale = read_artifact('iconiq_presale')