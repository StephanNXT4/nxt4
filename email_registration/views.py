from django.shortcuts import render

# Views

def landingpage(request):
	return render(request, 'email_registration/index.html', {})