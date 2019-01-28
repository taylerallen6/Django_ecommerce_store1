from django.contrib import admin
from .models import ProductDS, UserDS


class ProductDSAdmin(admin.ModelAdmin):
	list_display = ['__str__']

	class Meta:
		model = ProductDS

admin.site.register(ProductDS, ProductDSAdmin)


class UserDSAdmin(admin.ModelAdmin):
	list_display = ['__str__']

	class Meta:
		model = UserDS

admin.site.register(UserDS, UserDSAdmin)