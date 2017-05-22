from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from webapp import barcodevalidator
from webapp.models import Vendor, Token, Barcode
import datetime

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hey!</h2>")


