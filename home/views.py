from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class HomePageView(APIView):
    @staticmethod
    def get(request):
        return render(request, 'home/home.html')
