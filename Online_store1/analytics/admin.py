from django.contrib import admin
from .models import TriggeredSignal


class TriggeredSignalAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'user_profile', 'content_type', 'signal_type', 'timestamp']

	class Meta:
		model = TriggeredSignal

admin.site.register(TriggeredSignal, TriggeredSignalAdmin)
