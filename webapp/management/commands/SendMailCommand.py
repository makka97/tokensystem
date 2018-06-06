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
			'barcodesystem@viasat.com',
			to = ['dinesh.gaglani@viasat.com','dinesh.ramalingam@viasat.com'],
		)
		currentMonth = datetime.now().strftime('%m')
		currentYear = datetime.now().year
		currentDay = datetime.now().strftime('%d')
		email.attach_file('C:/Users/dgaglani/tokensystem/%s-%s-%s.txt' %(currentMonth,currentDay,currentYear)) 
 		email.send()
