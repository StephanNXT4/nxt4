from django.test import TestCase
from email_registration.models import Email
from email_registration.forms import EmailForm
from email_registration.views import confirm_submission

# Create your tests here.

class EmailRegistrationTests(TestCase):

	def no_duplicates_allowed(self):
		self.client = Client()
		e = Email(email = 'duplicate1@gmail.com')

		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

		response = self.client.post('/email_registration/confirm_submission/', {'email':e})
		self.assertEqual(response.status_code, 302)

		response = self.client.post('/email_registration/confirm_submission/', {'email':e})
		self.assertEqual(response.status_code, 302)

		email_list = Email.objects.all()

		self.assertEqual(len(email_list), 1)
