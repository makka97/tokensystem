from django.contrib import admin

# Register your models here.
from webapp.models import Vendor, Barcode, Token
from django.db.models import Count

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BarcodeList(admin.ModelAdmin):
	list_display = ('barcode', 'employee_name', 'employee_id')

	def employee_name(self, obj):
		return obj.barcodeName

	def employee_id(self, obj):
		return obj.employeeId

class TokenAdmin(admin.ModelAdmin):

	list_display = ('vendor_name', 'barcodeNumber', 'tokenDateTime', 'employee_id')

	list_filter = ('vendor__vendorName', 'barcode__barcode',)

	date_hierarchy = 'tokenDateTime'
	
	def vendor_name(self, obj):
		return obj.vendor.vendorName

	def barcodeNumber(self, obj):
		return obj.barcode.barcode

	def employee_id(self, obj):
		return obj.barcode.employeeId

	def has_add_permission(self, request, obj=None):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

class TokenAdminResource(resources.ModelResource):	

	class Meta:
		model = Token
		fields = ('vendor__vendorName', 'barcode__barcode', 'tokenDateTime', 'barcode__employeeId',)

class TokenAdmin2(ImportExportModelAdmin):

	list_display = ('vendor_name', 'barcodeNumber', 'tokenDateTime', 'employee_id')

	list_filter = ('vendor__vendorName', 'barcode__employeeId',)

	date_hierarchy = 'tokenDateTime'
	
	def vendor_name(self, obj):
		return obj.vendor.vendorName

	def barcodeNumber(self, obj):
		return obj.barcode.barcode

	def employee_id(self, obj):
		return obj.barcode.employeeId

	def has_add_permission(self, request, obj=None):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	resource_class = TokenAdminResource

class VendorAdmin(admin.ModelAdmin):
	list_display = ('vendor_name', 'vendor_id')

	def vendor_name(self, obj):
		return obj.vendorName

	def vendor_id(self, obj):
		return obj.id

admin.site.register(Barcode, BarcodeList)
admin.site.register(Token, TokenAdmin2)
admin.site.register(Vendor, VendorAdmin)
