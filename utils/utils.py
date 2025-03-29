from django.contrib.auth import login
from django.contrib.auth.models import User


def my_login(request,username,password,token_login=None,server_userid=None):
    user = User.objects.filter(username=username)
    if user.exists():
        user.delete()
    user = User.objects.create_user(username=username, password=password)
    login(request,user)
    request.session['token'] =token_login
    request.session['server_user_id'] =server_userid

