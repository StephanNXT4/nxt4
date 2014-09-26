from django.conf.urls import include, url
from django.contrib import admin

# email_registration urls

urlpatterns = [
	url(r'^confirm_submission/', 'email_registration.views.confirm_submission', name='confirm_submission'),
]