from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed

User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)

def post_save_user_receiver(sender, instance, *args, **kwargs):
	qs = UserProfile.objects.filter(user=instance)
	if qs.count() == 0:
		user_profile = UserProfile.objects.create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)