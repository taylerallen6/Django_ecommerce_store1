from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed
from decimal import Decimal

from django.db.models import Sum

User = settings.AUTH_USER_MODEL


class Item(models.Model):
	product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return str(self.product)


class CartManager(models.Manager):
	def new_or_get(self, request):
		cart_id = request.session.get("cart_id", None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			is_new_obj = False
			cart_obj = qs.first()
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=request.user)
			is_new_obj = True
			request.session['cart_id'] = cart_obj.id
		return cart_obj, is_new_obj

	def new(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated:
				user_obj = user
		return self.model.objects.create(user=user_obj)


# class Cart(models.Model):
# 	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
# 	products = models.ManyToManyField(Product, blank=True)
# 	subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
# 	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
# 	updated = models.DateTimeField(auto_now=True)
# 	timestamp = models.DateTimeField(auto_now_add=True)

# 	objects = CartManager()

# 	def __str__(self):
# 		return str(self.id)

class Cart(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	items = models.ManyToManyField(Item, blank=True)
	product_count = models.PositiveIntegerField(default=0)
	subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)






# def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
# 	if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
# 		products = instance.products.all()
# 		total = 0
# 		for x in products:
# 			total += x.price
# 		if instance.subtotal != total:
# 			instance.subtotal = total
# 			instance.save()

# m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)

# def pre_save_cart_receiver(sender, instance, *args, **kwargs):
# 	if instance.subtotal > 0:
# 		new_total = Decimal(instance.subtotal) * Decimal(1.08)
# 		formatted_total = format(new_total, '.2f')
# 		instance.total = formatted_total
# 	else:
# 		instance.total = 0.00


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
	if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
		items = instance.items.all()
		total_quantity = 0
		total = 0
		for x in items:
			total_quantity += x.quantity
			total += (Decimal(x.product.price) * Decimal(x.quantity))
		if instance.product_count != total_quantity:
			instance.product_count = total_quantity
			instance.save()
		if instance.subtotal != total:
			instance.subtotal = total
			instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.items.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
	if instance.id:
		items = instance.items.all()
		total_quantity = 0
		total = 0
		for x in items:
			total_quantity += x.quantity
			total += (Decimal(x.product.price) * Decimal(x.quantity))
		if instance.product_count != total_quantity:
			instance.product_count = total_quantity
		if instance.subtotal != total:
			instance.subtotal = total

	if instance.subtotal > 0:
		new_total = Decimal(instance.subtotal) * Decimal(1.08)
		formatted_total = format(new_total, '.2f')
		instance.total = formatted_total
	else:
		instance.total = 0.00

pre_save.connect(pre_save_cart_receiver, sender=Cart)


def post_save_item_receiver(sender, instance, *args, **kwargs):
	carts = instance.cart_set.all()

	for cart in carts:
		items = cart.items.all()
		total_quantity = 0
		total = 0
		for x in items:
			total_quantity += x.quantity
			total += (Decimal(x.product.price) * Decimal(x.quantity))

		if cart.product_count != total_quantity:
			cart.product_count = total_quantity
		if cart.subtotal != total:
			cart.subtotal = total

		if cart.subtotal > 0:
			new_total = Decimal(cart.subtotal) * Decimal(1.08)
			formatted_total = format(new_total, '.2f')
			cart.total = formatted_total
		else:
			cart.total = 0.00

		cart.save()

post_save.connect(post_save_item_receiver, sender=Item)