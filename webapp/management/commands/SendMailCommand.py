from django.contrib import admin
from webapp.models import Vendor, Barcode, Token
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
import datetime
from datetime import datetime

class Command(BaseCommand):
	help = 'Sends daily mail to Admin'

 	def handle(self, *args, **options):
 		email = EmailMessage(
			'Daily Update',
			'Token Count for the Day',
			'user@gmail.com',
			to = ['dinesh.gaglani@viasat.com'],
		)
		currentMonth = datetime.now().strftime('%m')
		currentYear = datetime.now().year
		#email.attach_file('C:/Users/mmanojkumar/Desktop/TokenSystem/%s-%s-%s.xls' %(currentdate,currentMonth,currentYear)) 
 		email.send()
