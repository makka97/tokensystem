from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.db import models
import json
from webapp import barcodevalidator
from webapp.models import Vendor, Token, Barcode
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hey!</h2>")

@method_decorator(csrf_exempt, name='dispatch')
class Purchase(View):

	def post(self, request):
		jsonData =  request.read() 
		data = json.loads(jsonData)
		barcodeNumber = data['barcodeNumber']
		vendorName = data['vendorName']
		if barcodevalidator.validateBarcode(barcodeNumber):
			barcodevalidator.insertToken(barcodeNumber, vendorName)
			return HttpResponse(content='success', content_type='text/html', status=200, reason=None, charset=None)
		else:
			return HttpResponse(content='failure', content_type='text/html', status=401, reason=None, charset=None)

	@csrf_exempt
	def get(self, request):
		startDate = request.GET.get('startDate')
		endDate = request.GET.get('endDate')
		barcode = request.GET.get('barcode')
		vendorName = request.GET.get('vendorName')
		
		if vendorName is None:
			jsonTokenCount = json.dumps(tokenCountObject(barcode))
			return JsonResponse(jsonTokenCount, safe=False)

		elif Vendor.objects.filter(vendorName = vendorName).count == 0 :
			return HttpResponse(content='failure', content_type='text/html', status=400, reason=None, charset=None)
		
		else:
			try:
				numberOfTokens = barcodevalidator.countToken(startDate, endDate, barcode, vendorName)
				tokenCount = {'tokencount': numberOfTokens}
				jsonTokenCount = json.dumps(tokenCount)
				return JsonResponse(jsonTokenCount, safe=False)
			except ValueError:
				return HttpResponse(content='failure', content_type='text/html', status=400, reason=None, charset=None)

