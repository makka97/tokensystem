from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.db import models
import json
from webapp import barcodevalidator
from webapp.models import Vendor, Token, Barcode
import datetime

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hey!</h2>")

class purchase(View):

	def post(self, request):
		jsonData =  request.read() 
		data = json.loads(jsonData)
		barcodeNumber = data['barcodeNumber']
		vendorNameIn = data['vendorName']
		if barcodevalidator.validateBarcode(barcodeNumber):
			barcodevalidator.insertToken(barcodeNumber, vendorNameIn)
			return HttpResponse.__init__(content='success', content_type=text, status=200, reason=None, charset=None)
		else:
			return HttpResponse.__init__(content='failure', content_type=text, status=401, reason=None, charset=None)

	def get(self, request):
		try:
			numberOfTokens = barcodevalidator.countToken(startDateIn, endDateIn, barcodeIn)
			tokenCount = {'tokencount': numberOfTokens}
			jsonTokenCount = json.dumps(tokenCount)
			return JsonResponse(jsonTokenCount)
		except ValueError:
			return HttpResponse.__init__(content='failure', content_type=text, status=400, reason=None, charset=None)

