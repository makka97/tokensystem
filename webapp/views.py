from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.list import ListView
from django.db import models
import json
from webapp import barcodevalidator
from webapp.models import Vendor, Token, Barcode, DailyCountOfToken
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from webapp import BarcodeView
from BarcodeView import addBarcodeNumber

import logging

logging.basicConfig(filename = 'test.log', level = logging.DEBUG)
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hey!</h2>")

@method_decorator(csrf_exempt, name='dispatch')
class Purchase(View):

	@csrf_exempt
	def post(self, request):
		jsonData =  request.read() 
		data = json.loads(jsonData)
		barcodeNumber = data['barcodeNumber']
		vendorId = data['vendorId']
		logger.info('Finished decoding Json POST request')

		if barcodevalidator.validateBarcode(barcodeNumber):
			barcodevalidator.insertToken(barcodeNumber, vendorId)
			logger.info('Validating and inserting done')
			return HttpResponse(content='success', content_type='text/html', status=200, reason=None, charset=None)
		else:
			logger.error('Could not validate barcode ' + str(barcodeNumber))
			return HttpResponse(content='failure', content_type='text/html', status=401, reason=None, charset=None)

	@csrf_exempt
	def get(self, request):
		startDate = request.GET.get('startDate')
		endDate = request.GET.get('endDate')
		barcode = request.GET.get('barcode')
		vendorId = request.GET.get('vendorId')
		logger.info('Finished decoding Json GET request')

		if vendorId is None:
			jsonTokenCount = barcodevalidator.countAllVendorTokens(barcode)
			logger.info('Vendor field is blank')
			return JsonResponse(jsonTokenCount, safe=False)

		elif Vendor.objects.filter(id = vendorId).count == 0 :
			logger.info('Invalid vendor')
			return HttpResponse(content='failure', content_type='text/html', status=400, reason=None, charset=None)
		
		else:
			logger.info('Vendor given')
			try:
				numberOfTokens = barcodevalidator.countToken(startDate, endDate, barcode, vendorId)
				logger.info('No error thrown')
				tokenCount = {'tokencount': str(numberOfTokens)}
				jsonTokenCount = json.dumps(tokenCount)
				logger.info('Coded to json')
				return JsonResponse(jsonTokenCount, safe=False)
			except ValueError:
				return HttpResponse(content='failure', content_type='text/html', status=400, reason=None, charset=None)

@method_decorator(csrf_exempt, name='dispatch')
class BarcodeView(View):

	@csrf_exempt
	def post(self, request):
		jsonData =  request.read() 
		data = json.loads(jsonData)
		barcodeNumber = data['barcodeNumber']
		name = data['Name']
		logger.info('Json decoded while adding barcode')
		
		if addBarcodeNumber(barcodeNumber,name):
			logger.info('Positive status')
			return HttpResponse(content='success', content_type='text/html', status=200, reason=None, charset=None)
		else:
			logger.info('Negative status')
			return HttpResponse(content='failure', content_type='text/html', status=400, reason=None, charset=None)


