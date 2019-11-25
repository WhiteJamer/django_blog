from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from el_pagination.views import AjaxListView


class PostList(AjaxListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'postmanager/post_list.html'
    def get_queryset(self):
        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            query = Q(title__icontains=q)
            query.add(Q(content__icontains=q), Q.OR)

            queryset = Post.objects.filter(query)
            return queryset
        else:
            queryset = Post.objects.all()
            return queryset


class PostDetail(DetailView):
    queryset = Post.objects.all()

class PostCreate(View):

    @method_decorator(login_required)
    def get(self, request):
        context = {'form': PostForm}
        return render(request, 'postmanager/post_add_form.html', context)

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                owner=request.user
            )
            new_post.save()
            new_post.categories.set(form.cleaned_data['categories'])
            new_post.save()
            return redirect(new_post)
        return redirect(reverse_lazy('postmanager:post_add'))
