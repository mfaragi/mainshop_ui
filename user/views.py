from django.contrib import messages

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import requests
from requests import Response
from rest_framework.views import APIView

from user.forms import *
from user.models import MyToken
from utils.constant import *
from utils.utils import my_login

#این کلاس برای پیش ثبت نام واعتبار سنجی است
class UserRegister(APIView):
    class_form = UserRegisterForm

    @staticmethod
    def get(request):
        return render(request, 'user/register.html',
                      {'form': UserRegisterForm(),
                       'form_header': 'ثبت نام',
                       'form_submit': 'ارسال کد فعالسازی'})

    @staticmethod
    def post(request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if password != password2:
                messages.error(request, 'رمز های عبور شما یکسان نیست')
                messages.success(request, 'رمز های عبور شما یکسان نیست')
                form = UserRegisterForm
                return render(request, 'user/register.html', {'form': form})

            url = USER_REGISTER_VERIFY

            data = {
                'token': USER_TOKEN,
                'email': email,

            }

            response: Response = requests.post(url, json=data)
            #بررسی وضعیت پاسخ
            if response.status_code == 200:
                # چاپ محتوای پاسخ
                messages.success(request, f"ایمیل فعالسازی به ایمیل شما به ادرس{email}ارسال شد")
                request.session['user_data'] = {'email': email, 'password': password}
                return redirect('user:register_verify')

            else:
                messages.error(request, response.json()[ERROR_NAME])

                print(response.text)

        messages.error(request, 'مشکل در بار گذاری فرم')

        return render(request, 'user/register.html',
                      {'form': form,
                       'form_header': 'ثبت نام',
                       'form_submit': 'ارسال کد فعالسازی'})


# ثبت نام کامل کاربر بعد از اعتبار سنجی ایمیل
class UserRegisterVerify(APIView):

    @staticmethod
    def get(request):
        my_value = request.session.post('user_data')  #اگر کلید موجود نباشد مقدار پیش فرض را بر میگرداند
        email = my_value['email']

        password = my_value['password']
        form = UserRegisterVerifyForm()
        return render(request, 'user/register_verify.html', {'form': form,
                                                             'data': {'email': email},
                                                             'form_header': 'اعتبار سنجی',
                                                             'form_submit': 'تکمیل ثبت نام'})

    @staticmethod
    def post(request):
        my_value = request.session.post('user_data')
        email = my_value['email']
        password = my_value['password']

        form = UserRegisterVerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            url = USER_REGISTER

            data = {
                'token': USER_TOKEN,
                'email': email,
                'code': code,
                'name': "",
                'phone': "",
                'password': password,
                'user_name': email,
                'profile_image': "",
            }
            response = requests.post(url, json=data)
            if response.status_code == 201:
                messages.success(request, 'ثبت نام شما با موفقیت انجام شد')


                my_login(request, email, password, token_login, response.json()['server_user_id'])
                return redirect('home:home')
            else:

                messages.error(request, response.json()[ERROR_NAME])
                form = UserRegisterVerifyForm()
                return render(request, 'user/register_verify.html', {'form': form,
                                                                     'data': {'email': email, 'password': password},
                                                                     'form_header': 'اعتبار سنجی',
                                                                     'form_submit': 'تکمیل ثبت نام'})


# لاگین از طریق ایمیل
class UserLogin(APIView):
    @staticmethod
    def get(request):
        form = UserLoginForm()
        return render(request,'user/login.html',{'form':form,
                                                 'form_header': 'ورود به حساب کاربری ',
                                                 'form_submit': 'ورود '})

    @staticmethod
    def post(request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            url = USER_LOGIN
            data = {
                'token': USER_TOKEN,
                'email': email,
                'password':password,
            }
            response = requests.post(url,json=data)
            if response.status_code == 200:

                #اینجا لاگین اتفاق افتاده است
                my_login(request, email, password, response.json()['token_login'], response.json()['server_user_id'])
                messages.success(request,response.json()['status'])
                return redirect('home:home')
            else:
                #لاگین با خطا موجه شده است
                messages.error(request,response.json()[ERROR_NAME])
                return redirect('user:login')


# برای ویرایش حساب کاربری
class UserEditProfile(APIView):
    @staticmethod
    def get(request):
        form=UserEditProfileForm()
        return render(request,'user/edit_profile.html',{'form':form,
                                                        'form_header': ' ویرایش پروفایل ',
                                                        'form_submit':'انجام '})
    @staticmethod
    def post(request):
        form =UserEditProfileForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            user_name = form.cleaned_data.get('user_name')
            profile_image=form.cleaned_data.get('profile_image')

            url =USER_EDIT_PROFILE
            token_login = request.session['token']
            data = {
                'token': USER_TOKEN,
                'name': name,
                'user_name': user_name,
                'profile_image':profile_image,
                'token_login':token_login
            }

            response = requests.post(url,json=data)
            if response.status_code == 200:
                messages.success(request, response.json()['status'])
                return redirect('user:register')
            else:
                messages.error(request, response.json()[ERROR_NAME])

        return render(request,'user/edit_profile.html',{'form':form,
                                                        'form_header': ' ویرایش پروفایل ',
                                                        'form_submit': 'انجام '})















