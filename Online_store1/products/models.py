from django.db import models
import random
import os
from online_store.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.db.models import Q


def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1, 23050923134)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(
		new_filename=new_filename,
		ext=ext
		)

	return "products/{new_filename}/{final_filename}".format(
		new_filename=new_filename, 
		final_filename=final_filename
		)


class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def search(self, query):
		lookups = (
			Q(title__icontains=query) | 
			Q(description__icontains=query) |
			Q(price__icontains=query) |
			Q(tags__icontains=query)
			)
		return self.filter(lookups).distinct()


class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def active(self):
		return self.get_queryset().active()

	def search(self, query):
		return self.get_queryset().active().search(query)


class Product(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(blank=True, unique=True)
	tags = models.TextField(null=True, blank=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	stock = models.IntegerField(default=0)
	image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = ProductManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse('products:detail', kwargs={"slug": self.slug})



def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)