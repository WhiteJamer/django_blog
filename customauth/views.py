from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *


class Login(LoginView):
    authentication_form = MyAuthenticationForm
    # redirect_authenticated_user = True


class Logout(LogoutView):
    pass


class PasswordReset(PasswordResetView):
    form_class = MyPasswordResetForm


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'customauth/password_reset_done.html'


class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'customauth/password_change_form.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'customauth/password_change_done.html'
