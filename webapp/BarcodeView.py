from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.db import models
import json
from webapp import barcodevalidator
from webapp.models import Vendor, Token, Barcode
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def addBarcode(barcodeNumberIn,nameIn):
	addBarcode = Barcode()
	addBarcode.barcode = barcodeNumberIn
	addBarcode.barcodeName = nameIn
	addBarcode.save()
	logger.info('Barcode added')

class BarcodeView(View):

	def post(self, request):
		jsonData =  request.read() 
		data = json.loads(jsonData)
		barcodeNumber = data['barcodeNumber']
		name = data['Name']
		logger.info('Json decoded while adding barcode')
		addBarcode(barcodeNumber,name)
		