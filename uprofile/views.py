from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View, UpdateView
from .models import User
from .forms import ProfileForm
from django.core.files.storage import FileSystemStorage
from base64 import b64decode
from django.core.files.base import ContentFile
from el_pagination.views import AjaxListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class UserList(AjaxListView):
    model = User
    queryset = User.objects.all()


class UserDetail(DetailView):
    context_object_name = 'auser' # another user not request.user
    queryset = User.objects.all()


class ProfileUpdate(View):

    @method_decorator(login_required())
    def post(self, request, slug):

        user = get_object_or_404(User, slug__iexact=slug)

        if request.user.username == user.username:
            format, imgstr = request.POST.get('avatar').split(';base64,')
            avatar_data = ContentFile(b64decode(imgstr), request.POST.get('filename'))

            user.avatar = avatar_data
            user.save()
            data = {'avatar_path': user.avatar.url}
        else:
            data = {'failed':True}
        return JsonResponse(data)



