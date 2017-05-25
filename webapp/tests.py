from django.test import TestCase

# Create your tests here.
from django.db import models
from webapp.models import Vendor, Token, Barcode
import datetime
import barcodevalidator
import BarcodeView
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class validateTest (TestCase):

	def validateTokenCountNoDate(self):
		BarcodeView.addBarcode(1111,'B1')
		BarcodeView.addBarcode(1112,'B2')

		barcodevalidator.insertToken(1111,'V1')
		barcodevalidator.insertToken(1112,'V1')
		barcodevalidator.insertToken(1111,'V2')

		print "barcode added!"

		self.assertEqual(barcodevalidator.countToken(None,None,None,'V1'), 2)

		logger.info("No Dates, barcode: 1111, vendor v1 " + str(barcodevalidator.countToken(None,None,1111,'V1'))) 
		self.assertEqual(barcodevalidator.countToken(None,None,1111,'V1'), 1)

		self.assertEqual(barcodevalidator.countToken(None,None,1112,'V1'), 1)


		

