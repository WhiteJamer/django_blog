from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from uprofile.models import User

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=("Username"),
                               widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=("Email"),
                             widget=forms.EmailInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'Email'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"),
                                   widget=forms.PasswordInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'Password'}))
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New password'}))
    new_password2 = forms.CharField(label=("New password confirmation"),

                                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New password again'}))


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    email_confirm = forms.EmailField()

