# this function simply writes the JSON files to a text file for logging
import json

def recordJSON(json_in):
    g = open('requestLog.txt','a+')
    g.write('\n\n')
    g.write(json.dumps(json_in, sort_keys=True, indent=4))
#    g.write(json_in['kyc_result'])
    g.close()
