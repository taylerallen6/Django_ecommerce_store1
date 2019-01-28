from django.db import models
from django.conf import settings
from products.models import Product
# from DSs.models import PorductDS, UserDS
from user_profile.models import UserProfile
from django.db.models.signals import pre_save, post_save, m2m_changed

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .signals import (
	object_viewed_signal,
	object_carted_signal)
from .utils import get_client_ip


User = settings.AUTH_USER_MODEL


class TriggeredSignal(models.Model):
    user_profile = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    # ip_address = models.CharField(max_length=220, blank=True, null=True)
    signal_type = models.CharField(max_length=120)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content_object)

    class Meta:
        ordering = ['-timestamp'] # most recent saved show up first


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender) # instance.__class__
    triggered_signal = TriggeredSignal.objects.create(
                user_profile = UserProfile.objects.get(user=request.user),
                signal_type= 'object_viewed_signal',
                content_type=c_type,
                object_id=instance.id,
                # ip_address = get_client_ip(request)
        )

object_viewed_signal.connect(object_viewed_receiver)



def object_carted_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender) # instance.__class__
    triggered_signal = TriggeredSignal.objects.create(
                user_profile = UserProfile.objects.get(user=request.user),
                signal_type= 'object_carted_signal',
                content_type=c_type,
                object_id=instance.id,
                # ip_address = get_client_ip(request)
        )

    # print(sender)
    # print(instance)
    # print(request)
    # print(request.user)

object_carted_signal.connect(object_carted_receiver)
