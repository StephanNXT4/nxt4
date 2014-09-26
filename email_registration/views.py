from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import EmailForm
from models import Email

# Views

def landingpage(request):
	form = EmailForm()
	return render(request, 'email_registration/index.html', {'form': form})

def confirm_submission(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			e = form.cleaned_data['email']
			test = Email(email=e)
			try:
				emails = Email.objects.get(email = e)
			except Email.DoesNotExist:
				emails = None
			if emails == None or test.email != emails.email:
				test.save()

	return HttpResponseRedirect('/')