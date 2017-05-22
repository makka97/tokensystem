from django.test import TestCase

# Create your tests here.
from django.db import models
from webapp.models import Vendor, Token, Barcode
import datetime
import webapp.barcodevalidator
from barcodevalidator import validateAndIncrement, validateBarcode, incrementCount

class validateTest (TestCase):

	def tests(self):
		barcode1 = Barcode(barcode = 1111)
		barcode1.save()

		barcode2 = Barcode(barcode = 1112)
		barcode2.save()

		vendorTokenCountForDate = Token.objects.get(tokenDate = datetime.datetime.now().date(), vendor = 1)
		self.assertEqual(vendorTokenCountForDate.tokenCount, 0)
		
		returnBool = validateAndIncrement(1111,1)
		self.assertTrue(returnBool)

		vendorTokenCountForDate = Token.objects.get(tokenDate = datetime.datetime.now().date(), vendor = 1)
		self.assertEqual(vendorTokenCountForDate.tokenCount, 0)

		
