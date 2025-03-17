from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from user.models import MyToken


def my_login(request,username,password,token_login=None):
    user = authenticate(request,username=username, password=password)
    if token_login is not None:
        my_user = MyToken.objects.get(user=user)
        my_user.token = token_login
        my_user.save()
    login(request,user)
