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
transactions = []
lastSuccessfulTransactionsCount = 0
#countLabel = tk.Label(root, text = jsonDataDict['tokencount'], font = (None, 150), fg = 'green' )

def incrementCountForVendor():
    for barcode in transactions:
        purchasePostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':barcode, 'vendorId':1}))
        jsonData = json.loads(requests.get(args.url+'?vendorId=1').text)
        jsonDataDict = ast.literal_eval(jsonData)
        if purchasePostRes.status_code == 200:
            #remove the entry from the list, update the lastTransactionCount
            transactions.remove(barcode)
            lastSuccessfulTransactionsCount = jsonDataDict['tokencount']

        if purchasePostRes.status_code == 401:
            #Unauthorized user, the display should show X
            countLabel.config(text = 'X', font = (None, 150), fg = 'red')


def saveBarcodeTransactionLocally(event):
    #save transaction to list
    transactions.append(entrytext.get())
    # Call API
    incrementCountForVendor()
    #Update the display with lastTransactionCount + transactions array length
    totalTransactionsCount = lastSuccessfulTransactionsCount + len(transactions)
    countLabel.config(text = totalTransactionsCount, font = (None, 150), fg = 'green')
    event.widget.delete(0, 'end')

countLabel.place(relx = 0.5, rely = 0.5, anchor = "center")
entrytext = tk.StringVar()
txBox = tk.Entry(root, textvariable=entrytext, width = 25)
txBox.bind('<Return>', saveBarcodeTransactionLocally)
txBox.place(relx = 0.5, rely = 0.15, anchor = "center")
txBox.focus()
root.mainloop()
