from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from el_pagination.views import AjaxListView
from django.http import JsonResponse


class PostList(AjaxListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'postmanager/post_list.html'
    def get_queryset(self):
        if self.request.GET.get('owner'):
            owner = self.request.GET.get('owner')
            queryset = Post.objects.filter(owner__username__iexact=owner)
            return queryset
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


class PostUpdate(View):

    @method_decorator(login_required)
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        if request.user == post.owner:
            form = PostForm(instance=post)
            context = {'form':form, 'post':post}
            return render(request, 'postmanager/post_update_form.html', context)
        else:
            return redirect(reverse_lazy('postmanager:post_list.html'))

    @method_decorator(login_required)
    def post(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.categories.set(form.cleaned_data['categories'])
            post.save()
            return redirect(post)
        return redirect(reverse_lazy('postmanager:post_update', kwargs={'slug':post.slug}))


class PostDelete(View):

    @method_decorator(login_required)
    def post(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        if request.user.username == post.owner.username:
            post.delete()
            data = {'done':True}
            return JsonResponse(data)
        else:
            data = {'done': False}
            return JsonResponse(data)


