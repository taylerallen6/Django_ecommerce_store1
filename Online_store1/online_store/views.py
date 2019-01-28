from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


def home_page(request):
	context = {
		'title': "Home",
	}

	return render(request, 'online_store/home_page.html', context)


def about_page(request):
	context = {
		'title': "About",
	}

	return render(request, 'online_store/about_page.html', context)


def contact_page(request):
	form = ContactForm(request.POST or None)
	context = {
		'title': "Contact",
		"form": form,
	}
	if form.is_valid():
		print(form.cleaned_data)

	return render(request, 'online_store/contact_page.html', context)