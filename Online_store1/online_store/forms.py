from django import forms
from django.core import validators



class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Fullname'}))
	email = forms.EmailField(validators=[validators.validate_email], widget=forms.EmailInput(
		attrs={'class':'form-control','placeholder':'Email'}))
	content = forms.CharField(widget=forms.Textarea(
		attrs={'class':'form-control','placeholder':'Content'}))