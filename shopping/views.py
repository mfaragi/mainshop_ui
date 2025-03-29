import requests
from django.shortcuts import render
from rest_framework.views import APIView

from utils.constant import *

# Create your views here.
class ShoppingCart(APIView):
    def get(self,request):
        global data_transaction
        url = GET_CART
        data = {
            'token':USER_TOKEN,
            'token_login':request.session['token'] if 'token' in request.session else None,
        }
        response = requests.get(url,params=data)
        cart = []
        if response.status_code == 200:
            carts = response.json().get('cart')
            total_price = 0
            total_final_price =0
            for cart in carts:
                total_price+=cart['price']
                total_final_price += cart['final_price ']
            data_transaction = {
                'total price':total_price,
                'total_final_price':total_final_price,
                'total_discount':total_price-total_final_price,
            }
        else:
            print(response.json().get('error'))
        return render(request,'shopping/shopping_cart.html',
                      {'carts':cart,
                       'data_transaction':data_transaction})
