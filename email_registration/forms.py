from django import forms

# Email Registration forms

class EmailForm(forms.Form):
	email = forms.EmailField(label='', min_length=4, max_length=50)