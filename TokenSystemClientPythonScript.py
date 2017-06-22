import json
import requests, sys, argparse
import Tkinter as tk
import ast

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Base url for tokens server")
args = parser.parse_args()

'''jsonData = json.loads(requests.get(args.url+'?vendorName=V1').text)
jsonDataDict = ast.literal_eval(jsonData)'''

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Token Count")
countLabel = tk.Label(root)
#countLabel = tk.Label(root, text = jsonDataDict['tokencount'], font = (None, 150), fg = 'green' )

def incrementCountForVendor(event):
    purchasePostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':entrytext.get(), 'vendorId':1}))
    jsonData = json.loads(requests.get(args.url+'?vendorId=1').text)
    jsonDataDict = ast.literal_eval(jsonData)
    if purchasePostRes.status_code == 200:
    	countLabel.config(text = jsonDataDict['tokencount'], font = (None, 150), fg = 'green')
    else:
        countLabel.config(text = 'X', font = (None, 150), fg = 'red')
    event.widget.delete(0, 'end')

countLabel.place(relx = 0.5, rely = 0.5, anchor = "center")
entrytext = tk.StringVar()
txBox = tk.Entry(root, textvariable=entrytext, width = 25)
txBox.bind('<Return>', incrementCountForVendor)
txBox.place(relx = 0.5, rely = 0.15, anchor = "center")
txBox.focus()
root.mainloop()
