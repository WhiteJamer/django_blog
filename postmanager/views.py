from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Post
from .forms import PostForm
from .urls import *
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
class PostDetail(DetailView):
    queryset = Post.objects.all()
class PostCreate(FormView):
    template_name = 'postmanager/post_add_form.html'
    form_class = PostForm
    success_url = reverse_lazy('postmanager:post_list')
    def form_valid(self, form):
        new_post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
        new_post.save()
        return super(PostCreate, self).form_valid(form)
