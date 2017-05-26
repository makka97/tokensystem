import json
import requests, sys, argparse
#from tkinter import *

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Base url for tokens server")
args = parser.parse_args()
"""root = tkinter.Tk()
root.title("Token Count")
countLabel = Tkinter.Label(root)"""

def requestsToServer():
    purchasePostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':inp, 'vendorName':'V1'}))

    if purchasePostRes.status_code == 200:
        tokensCountRes = requests.get(args.url+'?vendorName=V1')
        #countLabel.config(text = tokensCountRes.text)
    else:
        #countLabel.config(text = "Error from Server: Invalid barcode : " + inp, fg = "red" )


while True:
    inp = raw_input()
    if inp == "":
        continue
    else:
        requestsToServer()