from django.shortcuts import render, redirect
from .models import Cart, Item
from products.models import Product
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address

from django.http import JsonResponse
from django.http import HttpResponseRedirect

from analytics.signals import object_carted_signal


def cart_detail_api_view(request):
	cart_obj, is_new_obj = Cart.objects.new_or_get(request)
	products = [{
		"id": x.id,
		"url": x.get_absolute_url(),
		"name": x.name,
		"price": x.price
		}
		for x in cart_obj.products.all()]

	cart_data = {
		"products": products,
		"subtotal": cart_obj.subtotal,
		"total": cart_obj.total
	}
	return JsonResponse(cart_data)


def cart_home(request):
	cart_obj, is_new_obj = Cart.objects.new_or_get(request)
	return render(request, "carts/home.html", {"cart":cart_obj})


def cart_update(request):
	cart_id = request.session.get('cart_id', None)
	cart_obj = Cart.objects.get(id=cart_id)
	request.session['cart_items'] = cart_obj.product_count

	next = request.session.get('cart_update_next', None)
	return HttpResponseRedirect(next)


def cart_add(request):
	product_id = request.POST.get('product_id')
	
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show message to user, product is gone?")
			return redirect("cart:home")
		cart_obj, is_new_obj = Cart.objects.new_or_get(request)
		qs = cart_obj.items.filter(product=product_obj)
		if qs.count() != 0:
			item = qs.first()
			item.quantity += 1
			item.save()

			increased = True
		else:
			new_item = Item.objects.create(product=product_obj)
			cart_obj.items.add(new_item)
			added = True

		request.session['cart_items'] = cart_obj.product_count
		# return redirect(product_obj.get_absolute_url())
		# if request.is_ajax(): # Asynchronous Javascript And XML / JSON
		# 	print("Ajax request")
		# 	json_data = {
		# 		"added": added,
		# 		"removed": not added,
		# 		"cartItemCount": cart_obj.products.count()
		# 	}
		# 	return JsonResponse(json_data)

		object_carted_signal.send(product_obj.__class__, instance=product_obj, request=request)

	next = request.POST.get('next', '/')
	request.session['cart_update_next'] = next
	return redirect("cart:update")
	# return HttpResponseRedirect(next)


def cart_remove(request):
	product_id = request.POST.get('product_id')
	
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show message to user, product is gone?")
			return redirect("cart:home")
		cart_obj, is_new_obj = Cart.objects.new_or_get(request)
		qs = cart_obj.items.filter(product=product_obj)
		if qs.count() != 0:
			item = qs.first()
			cart_obj.items.remove(item)
			item.delete()
			removed = True
		else:
			print("Error removing item. No item of that product found in cart.")

		request.session['cart_items'] = cart_obj.product_count
		# return redirect(product_obj.get_absolute_url())
		# if request.is_ajax(): # Asynchronous Javascript And XML / JSON
		# 	print("Ajax request")
		# 	json_data = {
		# 		"added": added,
		# 		"removed": not added,
		# 		"cartItemCount": cart_obj.products.count()
		# 	}
		# 	return JsonResponse(json_data)

	next = request.POST.get('next', '/')
	request.session['cart_update_next'] = next
	return redirect("cart:update")
	# return HttpResponseRedirect(next)


def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.product_count == 0:
		return redirect("cart:home")

	login_form = LoginForm()
	guest_form = GuestForm()
	address_form = AddressForm()

	billing_address_id = request.session.get("billing_address_id", None)
	shipping_address_id = request.session.get("shipping_address_id", None)

	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	
	address_qs = None
	if billing_profile is not None:
		if request.user.is_authenticated:
			address_qs = Address.objects.filter(billing_profile=billing_profile)
		
		order_obj, order_obj_created = Order.objects.new_or_get(
			billing_profile=billing_profile,
			cart_obj=cart_obj)
		if shipping_address_id:
			order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
			del request.session["shipping_address_id"]
		if billing_address_id:
			order_obj.billing_address = Address.objects.get(id=billing_address_id)
			del request.session["billing_address_id"]
		if billing_address_id or shipping_address_id:
			order_obj.save()

	if request.method == "POST":
		"check that order is done"
		is_done = order_obj.check_done()
		if is_done:
			order_obj.mark_paid()
			request.session['cart_items'] = 0
			del request.session['cart_id']
			return redirect("carts:success")

	context = {
		"object": order_obj,
		"billing_profile": billing_profile,
		"login_form": login_form,
		"guest_form": guest_form,
		"address_form": address_form,
		"address_qs": address_qs,
	}

	return render(request, "carts/checkout.html", context)


def checkout_done_view(request):
	return render(request, "carts/checkout-done.html", {})

