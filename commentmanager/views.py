from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from postmanager.models import Post
from django.views.generic import View
from .models import Comment
from .forms import CommentForm
from el_pagination.views import AjaxListView
from django.http import JsonResponse

class CommentList(AjaxListView):
    model = Comment
    queryset = Comment.objects.all()
    context_object_name = 'comments'


class CommentCreate(View):

    @method_decorator(login_required)
    def post(self, request, post_slug):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=post_slug)
        if form.is_valid():
            new_comment = Comment(
                body = form.cleaned_data['body'],
                post = post,
                owner = request.user
            )
            new_comment.save()
            redirect(post)
        return redirect(reverse('postmanager:post_detail', kwargs={'slug':post.slug}) + '?message=Not valid data')


class CommentDelete(View):

    @method_decorator(login_required)
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.owner:
            comment.delete()
            data = {'info': 'Comment has been deleted'}
        else:
            data = {'info':'You is not owner'}
        return JsonResponse(data)




