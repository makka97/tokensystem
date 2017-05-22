import json
import requests, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Base url for tokens server")
parser.add_argument("barcode", help="Barcode used for item purchase")
args = parser.parse_args()

purchasePostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':args.barcode, 'vendorName':'V1'}))

if purchasePostRes.status_code == 200:
    tokensCountRes = requests.get(args.url+'?vendorName=V1')
    print(tokensCountRes.text)
else:
    print("Error from Server: Invalid barcode : " + args.barcode)
