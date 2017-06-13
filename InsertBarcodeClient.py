import json
import requests, sys, argparse
import Tkinter as tk

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Base url for tokens server")
args = parser.parse_args()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Add Barcode")
countLabel = tk.Label(root)

def barcodeAdd(event):
    barcodePostRes = requests.post(args.url, data = json.dumps({'barcodeNumber':entrytext.get(), 'Name':''}))
    if barcodePostRes.status_code == 200:
        countLabel.config(text = 'Barcode ' + str(entrytext.get()) + ' added', font = '100')
    else:
        countLabel.config(text = 'Barcode ' + str(entrytext.get()) + ' already exists ' , font = '100')
    countLabel.place(relx = 0.5, rely = 0.5, anchor = "center")
    event.widget.delete(0, 'end')

entrytext = tk.StringVar()
txBox = tk.Entry(root, textvariable=entrytext, width = 25)
txBox.bind('<Return>', barcodeAdd)
txBox.place(relx = 0.5, rely = 0.25, anchor = "center")
txBox.focus()
root.mainloop()
