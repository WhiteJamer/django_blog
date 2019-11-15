from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    queryset = Post.objects.all()

class PostCreate(View):


    def get(self, request):
        context = {'form': PostForm}
        return render(request, 'postmanager/post_add_form.html', context)


    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            new_post = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                owner=request.user
            )
            new_post.save()
            return redirect(new_post)
        return redirect(reverse_lazy('postmanager:post_add'))
