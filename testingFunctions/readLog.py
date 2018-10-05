import json
import sendTransaction_Rinkeby as sendTX

with open('requestLog.txt','r') as f:
    payload = json.load(f)

txHash = sendTX.main(payload['form_data']['btc'])

print(txHash)
