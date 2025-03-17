from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class ProductListView(APIView):
    @staticmethod
    def get(request):
        return render(request,'product/product_list.html')


class ProductDetailView(APIView):
    @staticmethod
    def get(request):
        return render(request,'product/product_detail.html')