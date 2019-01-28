from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'shipping_address', 'billing_address', 'status']

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)