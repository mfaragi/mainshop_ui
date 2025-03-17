from django import forms
class UserRegisterForm(forms.Form):
    email=forms.EmailField( label='لطفا ایمیل خود را وارد کنید ',widget=forms.TextInput(attrs={'class':'form-control m-1'}))
    password = forms.CharField(label='لطفا یک رمز عبور برای خود انتخاب نمایید ',widget=forms.PasswordInput(attrs={'class':'form-control m-1'}))
    password2 = forms.CharField(label='لطفا پسورد خود را مجدد وارد نمایید  ', widget=forms.PasswordInput(attrs={'class':'form-control m-1'}))

class UserRegisterVerifyForm(forms.Form):
    code = forms.CharField(label='کد ایمیل شده را وارد کنید',widget=forms.TextInput(attrs={'class':'form-control m-1'}))


class UserLoginForm(forms.Form):
    email=forms.EmailField( label='لطفا ایمیل خود را وارد کنید ',widget=forms.TextInput(attrs={'class':'form-control m-1'}))
    password = forms.CharField(label='لطفارمز عبورخود را وارد  نمایید ',widget=forms.PasswordInput(attrs={'class':'form-control m-1'}))

class UserEditProfileForm(forms.Form):
    name= forms.CharField(label='نام خود را وارد کنید',widget=forms.TextInput(attrs={'class': 'form-control m-1'}))
    username = forms.CharField(label='یوزرنیم خود را وارد کنید', widget=forms.TextInput(attrs={'class': 'form-control m-1'}))
    profile_image = forms.CharField(label='لینک عکس خود را وارد کنید', widget=forms.TextInput(attrs={'class': 'form-control m-1'}))

