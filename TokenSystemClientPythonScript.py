import json
import requests, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Base url for tokens server")
args = parser.parse_args()

while True:
    inp = raw_input()
    if inp == "":
        continue
    else:
        purchasePostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':inp, 'vendorName':'V1'}))

        if purchasePostRes.status_code == 200:
            tokensCountRes = requests.get(args.url+'?vendorName=V1')
            print(tokensCountRes.text)
        else:
            print("Error from Server: Invalid barcode : " + inp)
