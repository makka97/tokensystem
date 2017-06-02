import json
import requests, sys, argparse
import Tkinter as tk

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Base url for tokens server")
args = parser.parse_args()

root = tk.Tk()
root.title("Add Barcode")

def barcodeAdd(event):
    barcodeAddPostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':entrytext.get(), 'barcodeName':''}))
    event.widget.delete(0, 'end')

entrytext = tk.StringVar()
txBox = tk.Entry(root, textvariable=entrytext, width = 25)
txBox.bind('<Return>', incrementCountForVendor)
txBox.pack()
root.mainloop()

