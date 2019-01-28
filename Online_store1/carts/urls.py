from django.urls import path
from . import views


app_name = 'carts'
urlpatterns = [
    path('', views.cart_home, name='home'),
    # path('update/', views.cart_update, name='update'),

    path('add/', views.cart_add, name='add'),
    path('remove/', views.cart_remove, name='remove'),
    path('update/', views.cart_update, name='update'),

    path('checkout/', views.checkout_home, name='checkout'),
    path('checkout/success/', views.checkout_done_view, name='success'),
]
