from django.urls import path


from user.views import UserRegister, UserRegisterVerify, UserLogin, UserEditProfile

app_name = 'user'




urlpatterns = [
    path('register', UserRegister.as_view(), name='register'),
    path('register_verify', UserRegisterVerify.as_view(), name='register_verify'),
    path('login', UserLogin.as_view(), name='login'),
    path('edit_profile', UserEditProfile.as_view(), name='edit_profile')

]
