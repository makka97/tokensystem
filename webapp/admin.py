from django.contrib import admin

# Register your models here.
from webapp.models import Vendor, Barcode, Token, DailyCountOfTokens
from django.db.models import Count

from import_export import resources
from import_export.admin import ImportExportModelAdmin
import logging

logging.basicConfig(filename = 'test.log', level = logging.DEBUG)
logger = logging.getLogger(__name__)

class BarcodeList(admin.ModelAdmin):
	list_display = ('barcode', 'employee_name', 'employee_id')

	def employee_name(self, obj):
		return obj.barcodeName

	def employee_id(self, obj):
		return obj.employeeId

class TokenAdminWithImportExport(ImportExportModelAdmin):

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

	#resource_class = TokenAdminResource

class DailyCountOfTokensAdmin(admin.ModelAdmin):

	list_display = ('vendor_name', 'token_date', 'num_count')

	def vendor_name(self, obj):
		return self._vendor_cache.vendorName

	def token_date(self, obj):
		return self.tokenDateTime

	def num_count(self, obj):
		return self.num_count

	def get_queryset(self, request):
		qs = DailyCountOfTokens.objects.all()
		#return super(DailyCountOfTokensAdmin, self).get_queryset(request)
		return qs


class VendorAdmin(admin.ModelAdmin):
	list_display = ('vendor_name', 'vendor_id')

	def vendor_name(self, obj):
		return obj.vendorName

	def vendor_id(self, obj):
		return obj.id

admin.site.register(Barcode, BarcodeList)
admin.site.register(Token, TokenAdminWithImportExport)
admin.site.register(DailyCountOfTokens, DailyCountOfTokensAdmin)
admin.site.register(Vendor, VendorAdmin)
