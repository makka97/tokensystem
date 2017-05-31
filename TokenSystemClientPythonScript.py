import json
import requests, sys, argparse
import Tkinter as tk

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Base url for tokens server")
args = parser.parse_args()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Token Count")
countLabel = tk.Label(root)

def incrementCountForVendor(event):
    purchasePostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':entrytext.get(), 'vendorName':'V1'}))
    if purchasePostRes.status_code == 200:
        countLabel.config(text = requests.get(args.url+'?vendorName=V1').text, font = '100')
    else:
        countLabel.config(text = 'Could not validate barcode ' + str(entrytext.get()) + requests.get(args.url+'?vendorName=V1').text, font = '100')
    countLabel.pack()
    event.widget.delete(0, 'end')

entrytext = tk.StringVar()
txBox = tk.Entry(root, textvariable=entrytext, width = 25)
txBox.bind('<Return>', incrementCountForVendor)
txBox.pack()
root.mainloop()
