import requests
from django.shortcuts import render
from rest_framework.views import APIView

from utils.constant import GET_LIST_PRODUCTS, USER_TOKEN, GET_PRODUCT_DETAIL


# Create your views here.
class ProductListView(APIView):
    @staticmethod
    def get(request,slug):
        products=""
        url = GET_LIST_PRODUCTS
        if 'category' in slug:
            category_id = int(slug[8:])
            data = {
                'category_id':category_id,
                'token':USER_TOKEN,
            }
        else:
            data = {
                'name':slug,
                'token':USER_TOKEN,
            }
        response = requests.get(url,params=data)
        if response.status_code ==200:
            products = response.json().get('list_products')
        return render(request,'product/product_list.html',
                      {'product_list': products,
                       'slug':slug})



class ProductDetailView(APIView):
    @staticmethod
    def get(request,slug):
        url = GET_PRODUCT_DETAIL
        data = {
            'token':USER_TOKEN,
            'product_id':int(slug),
        }
        response = request.Get.get(url,params=data)
        product=""
        if response.status_code == 200:
            product = response.json().get('product')

            # در این قسمت من بنر ها را جدا و صحیح به صفحه ارسال میکنم
            banners = product['banners']
            video_url = ""
            img_urls = []
            if banners['video'] is not None:
                video_url = banners['video']
            for key,value in banners.items():
                if 'image' in key and value is not None:
                    img_urls.append(value)

            data = {
                'video_url':video_url,
                'img_urls':enumerate(img_urls),
            }
        else:
            pass
        return render(request,'product/product_detail.html',
                      {'product':product,'banners':data,})


