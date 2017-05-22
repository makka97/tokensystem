from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.db import models
import json
from webapp import barcodevalidator
from webapp.models import Vendor, Token, Barcode


# Create your views here.
class Barcode(View):

	def post(self, request):
		jsonData =  request.read() 
		data = json.loads(jsonData)
		barcodeNumber = data['barcodeNumber']
		name = data['Name']
		addBarcode = Barcode()
		addBarcode.barcode = barcodeNumber
		addBarcode.barcodeName = name