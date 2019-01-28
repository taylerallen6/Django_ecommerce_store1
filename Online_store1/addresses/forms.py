from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = [
		# 'billing_profile',
		# 'address_type',
		'address_line_1',
		'address_line_2',
		'city',
		'country',
		'state',
		'postal_code'
		]

		widgets = {
            'address_line_1': forms.TextInput(
            	attrs={'class':'form-control','placeholder':'Address line 1'}),
            'address_line_2': forms.TextInput(
            	attrs={'class':'form-control','placeholder':'Address line 2'}),
            'city': forms.TextInput(
            	attrs={'class':'form-control','placeholder':'City'}),
            'country': forms.TextInput(
            	attrs={'class':'form-control','placeholder':'Country'}),
            'state': forms.TextInput(
            	attrs={'class':'form-control','placeholder':'State'}),
            'postal_code': forms.TextInput(
            	attrs={'class':'form-control','placeholder':'Postal code'})
        }