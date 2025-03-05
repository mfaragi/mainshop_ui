from django import forms
class UserRegisterForm(forms.Form):
    email=forms.EmailField()
