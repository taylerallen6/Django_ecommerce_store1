from django.contrib import admin
from .models import Cart, Item


admin.site.register(Cart)

class ItemAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'quantity']

	class Meta:
		model = Item

admin.site.register(Item, ItemAdmin)