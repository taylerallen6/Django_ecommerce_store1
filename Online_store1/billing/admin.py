from django.contrib import admin
from.models import BillingProfile


class BillingProfileAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'user', 'email', 'active']

	class Meta:
		model = BillingProfile

admin.site.register(BillingProfile, BillingProfileAdmin)