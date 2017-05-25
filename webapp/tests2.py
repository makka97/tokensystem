from django.test import TestCase

# Create your tests here.
from django.db import models
from webapp.models import Vendor, Token, Barcode
import datetime
from datetime import datetime, timedelta
import barcodevalidator
import BarcodeView
import logging

logger = logging.getLogger(__name__)

class validateTest (TestCase):

	def tests(self):

		BarcodeView.addBarcode(1111,'B1')
		BarcodeView.addBarcode(1112,'B2')

		date = datetime.now()
		yesterday = datetime.now() + timedelta(days = -1)
		tomorrow = datetime.now() + timedelta(days = 1)
		
		insertDateTime = Token(tokenDateTime = yesterday, vendor = Vendor.objects.get(vendorName = 'V1'), barcode= Barcode.objects.get(barcode = 1111))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = date, vendor = Vendor.objects.get(vendorName = 'V1'), barcode = Barcode.objects.get(barcode = 1111))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = tomorrow, vendor = Vendor.objects.get(vendorName = 'V1'), barcode = Barcode.objects.get(barcode = 1111))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = date, vendor = Vendor.objects.get(vendorName = 'V1'), barcode = Barcode.objects.get(barcode = 1112))
		insertDateTime.save()

		insertDateTime = Token(tokenDateTime = tomorrow, vendor = Vendor.objects.get(vendorName = 'V2'), barcode = Barcode.objects.get(barcode = 1112))
		insertDateTime.save()


		self.assertEqual(barcodevalidator.countToken(None,None,None,'V1'), 2)

		self.assertEqual(barcodevalidator.countToken(None,date.strftime("%m/%d/%Y %H:%M:%S"),None,'V1'), 2)

		self.assertEqual(barcodevalidator.countToken(yesterday.strftime("%m/%d/%Y %H:%M:%S"),date.strftime("%m/%d/%Y %H:%M:%S"),1111,'V1'), 2)

		self.assertEqual(barcodevalidator.countToken(date.strftime("%m/%d/%Y %H:%M:%S"),tomorrow.strftime("%m/%d/%Y %H:%M:%S"),1112,'V1'), 1)



		

