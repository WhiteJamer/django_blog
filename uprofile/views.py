from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, View, UpdateView
from .models import User
from .forms import ProfileForm
from django.core.files.storage import FileSystemStorage

class UserList(ListView):
    model = User


class UserDetail(DetailView):
    context_object_name = 'auser' # another user not request.user
    queryset = User.objects.all()


class ProfileUpdate(View):

    def get(self, request, slug):
        user = get_object_or_404(User, slug__iexact=slug)
        form = ProfileForm(instance=user)
        context = {'form': form}
        return render(request, 'uprofile/profile_update.html', context)

    def post(self, request, slug):
        user = get_object_or_404(User, slug__iexact=slug)
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['avatar']
            fs = FileSystemStorage()
            avatar = fs.save(image.name, image)
            user.avatar = avatar
            user.save()
            return redirect(user)
        return redirect(reverse('uprofile:profile_update', kwargs={'slug':slug}))



