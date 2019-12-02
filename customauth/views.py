from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from uprofile.models import User


class Login(LoginView):
    authentication_form = MyAuthenticationForm
    template_name = 'customauth/login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    template_name = 'customauth/logged_out.html'

class Register(View):

    def get(self, request):
        if request.user.is_anonymous:
            form = RegistrationForm
            context = {'form':form}
            return render(request, 'customauth/register.html', context)
        else:
            return HttpResponse('You already registered')

    def post(self, request):
        if request.user.is_anonymous:
            form = RegistrationForm(request.POST)
            if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm'] \
            and form.cleaned_data['email'] == form.cleaned_data['email_confirm']:

                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()
                user.set_password(user.password)

                return redirect(user)
        else:
            return HttpResponse('You already registered')


class PasswordReset(PasswordResetView):
    form_class = MyPasswordResetForm


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'customauth/password_reset_done.html'


class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'customauth/password_change_form.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'customauth/password_change_done.html'
