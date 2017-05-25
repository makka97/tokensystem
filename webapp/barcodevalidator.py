from django.db import models
from webapp.models import Vendor, Token, Barcode
import datetime
from datetime import datetime
import json
import logging
from django.db.models import Count

logging.basicConfig(filename = 'test.log', level = logging.DEBUG)
logger = logging.getLogger(__name__)

#request has barcodeNumber and vendorId

def validateBarcode (barcodeIn):
	logger.info('Validating barcode')
	valid = Barcode.objects.filter(barcode = barcodeIn).count()
	return valid != 0

def insertToken (barcodeIn, vendorNameIn):
	barcode = Barcode.objects.get(barcode = barcodeIn)
	vendor = Vendor.objects.get(vendorName = vendorNameIn)
	insertDateTime = Token(tokenDateTime = datetime.now(), vendor = vendor, barcode = barcode)
	insertDateTime.save()
	logger.info('Token inserted')	

def countToken(startDateIn, endDateIn, barcodeIn, vendorName):
	startDate = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
	endDate = datetime.now()

	if startDateIn is not None:
		startDate = datetime.strptime(startDateIn, "%m/%d/%Y %H:%M:%S")
		logger.info('Start date is given date')
	
	if endDateIn is not None:
		endDate = datetime.strptime(endDateIn, "%m/%d/%Y %H:%M:%S")
		logger.info('End date is given date')

	if barcodeIn is not None:
		numberOfTokens = Token.objects.filter(vendor__vendorName=vendorName).filter(barcode__barcode=barcodeIn).filter(tokenDateTime__gte = startDate).filter(tokenDateTime__lte = endDate).count()
	else:
		numberOfTokens = Token.objects.filter(vendor__vendorName=vendorName).filter(tokenDateTime__gte = startDate).filter(tokenDateTime__lte = endDate).count()
		logger.info('Barcode is not given when vendor is given')	
	
	return numberOfTokens
	
def countAllVendorTokens(barcodeIn):
	if barcodeIn is not None:
		listObj = Token.objects.filter(barcode_id__barcode = barcodeIn).values('vendor_id__vendorName').annotate(vendor_count=Count('vendor_id')).replace('barcode_id__barcode','barcode')
	else:
		listObj = Token.objects.values('vendor_id__vendorName').annotate(vendor_count=Count('vendor_id'))

	listObj = str(listObj).replace('vendor_id__vendorName','vendorName')
	logger.info('String object')
	
	return listObj
	
	
