from django.test import TestCase

# Create your tests here.
from django.db import models
from webapp.models import Vendor, Token, Barcode
import datetime
import webapp.barcodevalidator
from barcodevalidator import insertToken, validateBarcode, countToken

class validateTest (TestCase):

	def tests(self):
		barcode1 = Barcode(barcode = 1111)
		barcode1.save()

		barcode2 = Barcode(barcode = 1112)
		barcode2.save()

		insertToken(1111,'V1')
		insertToken(1112,'V1')
		insertToken(1111,'V2')

		self.assertEqual(countToken('V1'), 2)

		self.assertTrue(countToken(1111,'V1'), 1)

		self.assertEqual(countToken(1112,'V1'), 1)

		
