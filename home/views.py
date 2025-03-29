from django.shortcuts import render
from rest_framework.views import APIView

import requests

from utils.constant import *


# Create your views here.
class HomePageView(APIView):
    @staticmethod
    def get(request):
        url = GET_HOME_CONTENT
        url2 = GET_LIST_PRODUCTS
        data = {
            'token':USER_TOKEN
        }
        data2 = {
            'token': USER_TOKEN,
            'name':'best'
        }
        response = requests.get(url,params=data)
        response2 = requests.get(url2, params=data2)
        top_banners=""
        categories=""
        product_list=""
        if response.status_code ==200:
            top_banners = response.json().get('top_banner')
            categories = response.json().get('categories')
        else:
            pass
        #دریافت شدن لیست محصولات بهترین ها
        if response2.status_code == 200:
            product_list = response.json().get('list_products')
        return render(request,'home/home.html',
                      {'top_banners':enumerate(top_banners), 'categories':categories,
                       'product_list':product_list[:4]})
