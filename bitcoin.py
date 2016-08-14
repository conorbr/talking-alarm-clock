# Bitcoin Price Index Module

import requests
import json

def get_bitcoin_price():
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
    if request.status_code == 200:
        obj = json.loads(request.text)
        return float(obj['bpi']['USD']['rate'])
    else:
        print "Failed to retrieve bitcoin price index. Response returned code " + str(request.response_code)
        return False

