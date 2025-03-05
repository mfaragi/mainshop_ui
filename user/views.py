from django.shortcuts import render
from rest_framework.views import APIView
import requests
from user.forms import UserRegisterForm
from utils.constant import USER_REGISTER_VERIFY, USER_TOKEN


class Register(APIView):
    class_form = UserRegisterForm
    @staticmethod
    def get(request):
        return render(request,'user/register.html',
                      {'form':UserRegisterForm})


    @staticmethod
    def post(request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            url=USER_REGISTER_VERIFY

            data = {
                'token': USER_TOKEN,
                'email':email,

            }
            response = requests.post(url,json=data)
            #بررسی وضعیت پاسخ
            if response.status_code == 200:
                # چاپ محتوای پاسخ
                print("verify status", response.json())
            else:
                print("Error:",response.json())
        return render(request,'user/register.html',
                  {'form':form})




