from django.urls import path
from user.views import Register

app_name = 'user'
urlpatterns = [
    path('register',Register.as_view(),name='register'),


]