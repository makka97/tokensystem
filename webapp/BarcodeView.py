from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.db import models
import json
from webapp import barcodevalidator
from webapp.models import Vendor, Token, Barcode
import logging

logging.basicConfig(filename = 'test.log', level = logging.DEBUG)
logger = logging.getLogger(__name__)

# Create your views here.
def addBarcodeNumber(barcodeNumberIn,nameIn):
	addBarcode = Barcode()
	if Barcode.objects.filter(barcode = barcodeNumberIn).count() == 0:
		addBarcode.barcode = barcodeNumberIn
		addBarcode.barcodeName = nameIn
		addBarcode.save()
		logger.info('Barcode added')
		return True
	else:
		return False