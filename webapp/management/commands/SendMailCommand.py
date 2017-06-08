from django.contrib import admin
from webapp.models import Vendor, Barcode, Token
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
import datetime
from datetime import datetime

class Command(BaseCommand):
	help = 'Sends monthly mail to Admin'

 	def handle(self, *args, **options):
 		email = EmailMessage(
			'Monthly Update',
			'Token Count for the Month',
			'user@gmail.com',
			to = ['malavika.manojkumar@viasat.com'],
		)
		currentMonth = datetime.now().strftime('%m')
		currentYear = datetime.now().year
		email.attach_file('C:/Users/mmanojkumar/Desktop/TokenSystem/%s-%s.xls' %(currentMonth,currentYear)) 
 		email.send()
