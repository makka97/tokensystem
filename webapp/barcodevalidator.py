from django.db import models
from webapp.models import Vendor, Token, Barcode
import datetime
from datetime import datetime
import json

#request has barcodeNumber and vendorId

def validateBarcode (barcodeIn):
	valid = Barcode.objects.filter(barcode = barcodeIn).count()
	return valid != 0

def insertToken (barcodeIn, vendorNameIn):
	barcode = Barcode.objects.get(barcode = barcodeIn)
	vendor = Vendor.objects.get(vendorName = vendorNameIn)
	insertDateTime = Token(tokenDateTime = datetime.now(), vendor = vendor, barcode = barcode)
	insertDateTime.save()	

def countToken(startDateIn, endDateIn, barcodeIn):
	startDate = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
	endDate = datetime.now()

	if startDateIn is not None:
		startDate = datetime.strptime(startDateIn, '%m/%d/%Y %I:%M:%S %p')
	
	if endDateIn is not None:
		endDate = datetime.strptime(endDateIn, '%m/%d/%Y %I:%M:%S %p')

	if barcodeIn is not None:
		numberOfTokens = Token.objects.filter(barcode=barcodeIn).filter(tokenDateTime__gte = startDate).filter(tokenDateTime__lte = endDate).count()
	else:
		numberOfTokens = Token.objects.filter(tokenDateTime__gte = startDate).filter(tokenDateTime__lte = endDate).count()
	
	return numberOfTokens
	
