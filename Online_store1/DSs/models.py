from django.db import models
from django.conf import settings
from products.models import Product
from analytics.models import TriggeredSignal
from user_profile.models import UserProfile
from django.db.models.signals import pre_save, post_save, m2m_changed

from decimal import Decimal


User = settings.AUTH_USER_MODEL


# Demographic Statistics -----------------#

class ProductDS(models.Model):
	product = models.OneToOneField(Product, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	gender_female = models.DecimalField(default=50.0, max_digits=15, decimal_places=5)
	gender_male = models.DecimalField(default=50.0, max_digits=15, decimal_places=5)

	age_18to24 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_25to34 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_35to44 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_45to54 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_55to64 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_65plus = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	rs_single = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	rs_in_a_relationship = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	rs_engaged = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	rs_married = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	edu_high_school = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	edu_college = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	edu_grad_school = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	jt_administrative_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_architecture_and_enginerring = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_art_entertainment_sports_and_media = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_business_and_finance = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_cleaning_and_maintenance_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_community_and_social_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_computation_and_mathematics = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_construction_and_extraction = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_education_and_libraries = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_farming_fishing_and_forestry = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_food_and_restaurants = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_government_employees_global = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_healthcare_and_medical_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_installation_and_repair_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_it_and_technical_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_legal_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_life_physical_and_social_sciences = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_management = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_military_global = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_production = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_protective_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_sales = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_transportation_and_moving = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_veterans_us = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	def __str__(self):
		return str(self.product)


class UserDS(models.Model):
	user_profile = models.OneToOneField(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	gender_female = models.DecimalField(default=50.0, max_digits=15, decimal_places=5)
	gender_male = models.DecimalField(default=50.0, max_digits=15, decimal_places=5)

	age_18to24 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_25to34 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_35to44 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_45to54 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_55to64 = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	age_65plus = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	rs_single = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	rs_in_a_relationship = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	rs_engaged = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	rs_married = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	edu_high_school = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	edu_college = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	edu_grad_school = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	jt_administrative_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_architecture_and_enginerring = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_art_entertainment_sports_and_media = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_business_and_finance = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_cleaning_and_maintenance_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_community_and_social_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_computation_and_mathematics = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_construction_and_extraction = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_education_and_libraries = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_farming_fishing_and_forestry = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_food_and_restaurants = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_government_employees_global = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_healthcare_and_medical_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_installation_and_repair_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_it_and_technical_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_legal_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_life_physical_and_social_sciences = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_management = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_military_global = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_production = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_protective_services = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_sales = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_transportation_and_moving = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)
	jt_veterans_us = models.DecimalField(default=0.0, max_digits=15, decimal_places=5)

	def __str__(self):
		return str(self.user_profile)





# Signals: Create DSs -------------------------- #

def post_save_user_profile_receiver(sender, instance, *args, **kwargs):
	qs = UserDS.objects.filter(user_profile=instance)
	if qs.count() == 0:
		user_ds = UserDS.objects.create(user_profile=instance)

post_save.connect(post_save_user_profile_receiver, sender=UserProfile)


def post_save_product_receiver(sender, instance, *args, **kwargs):
	qs = ProductDS.objects.filter(product=instance)
	if qs.count() == 0:
		product_ds = ProductDS.objects.create(product=instance)

post_save.connect(post_save_product_receiver, sender=Product)



# Signals: Update DSs -------------------------- #

def pre_save_product_ds_receiver(sender, instance, *args, **kwargs):
	instance.gender_male = (100 - instance.gender_female)

pre_save.connect(pre_save_product_ds_receiver, sender=ProductDS)


def post_save_product_ds_receiver(sender, instance, *args, **kwargs):
	triggered_signals = TriggeredSignal.objects.filter(
		content_type__model='product',
		object_id=instance.id)

	for triggered_signal in triggered_signals:
		triggered_signal.save()

post_save.connect(post_save_product_ds_receiver, sender=ProductDS)


def post_save_triggered_signal_receiver(sender, instance, *args, **kwargs):
	user_ds = UserDS.objects.get(user_profile=instance.user_profile)
	
	fieldVals = [0] * (len(UserDS._meta.get_fields())- 4)
	fieldNames = [f.name for f in ProductDS._meta.get_fields()]
	fieldNames = fieldNames[4:]


	triggered_signals = TriggeredSignal.objects.filter(
		user_profile=instance.user_profile,
		content_type__model='product',
		signal_type='object_viewed_signal')
	viewedCount = triggered_signals.count()

	if triggered_signals.count() != 0:
		for triggered_signal in triggered_signals:
			product = triggered_signal.content_object
			product_dss = ProductDS.objects.filter(product=product)
			if product_dss.count() != 0:
				product_ds = product_dss.first()

				for i in range(len(fieldVals)):
					fieldVals[i] += getattr(product_ds, fieldNames[i])


	triggered_signals = TriggeredSignal.objects.filter(
		user_profile=instance.user_profile,
		content_type__model='product',
		signal_type='object_carted_signal')
	cartedCount = (triggered_signals.count() * 2)

	if triggered_signals.count() != 0:
		for triggered_signal in triggered_signals:
			product = triggered_signal.content_object
			product_dss = ProductDS.objects.filter(product=product)
			if product_dss.count() != 0:
				product_ds = product_dss.first()

				for i in range(len(fieldVals)):
					fieldVals[i] += (getattr(product_ds, fieldNames[i]) * 2)


	totalCount = viewedCount + cartedCount
	if totalCount != 0:
		for i in range(len(fieldVals)):
			fieldVals[i] /= totalCount
			user_ds.__dict__[fieldNames[i]] = fieldVals[i]

		user_ds.save()

post_save.connect(post_save_triggered_signal_receiver, sender=TriggeredSignal)






# 100v + 50v /2 = 75
# 50v + 10v /2 = 30

# 100v + 25v /2 = 62.5

# 100v + (25b * 2) /
# (v.count + (b.count*2)) = 