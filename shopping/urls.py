from django.urls import path

from shopping.views import *

app_name = 'shopping'




urlpatterns = [
    path('cart',ShoppingCart.as_view(),name='cart'),


]