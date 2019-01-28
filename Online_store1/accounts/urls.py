from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_page, name='register'),
    path('register/guest', views.guest_register_view, name='guest_register'),
]