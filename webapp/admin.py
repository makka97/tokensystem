from django.contrib import admin

# Register your models here.
from webapp.models import Vendor, Barcode,Token


class BarcodeList(admin.ModelAdmin):
	list_display = ('barcode', 'barcodeName')

class TokenList(admin.ModelAdmin):
	list_display = ('vendor_name', 'barcodeNumber', 'tokenDateTime')

	def vendor_name(self, obj):
		return obj.vendor.vendorName

	def barcodeNumber(self, obj):
		return obj.barcode.barcode


admin.site.register(Barcode, BarcodeList)
admin.site.register(Token, TokenList)