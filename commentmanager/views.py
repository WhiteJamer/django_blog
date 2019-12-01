from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from postmanager.models import Post
from django.views.generic import View
from .models import Comment
from .forms import CommentForm
from el_pagination.views import AjaxListView
from django.http import JsonResponse, HttpResponse

class CommentList(AjaxListView):
    model = Comment
    context_object_name = 'comments'

    def get_queryset(self):
        if self.request.GET.get('owner'):
            owner = self.request.GET.get('owner')
            queryset = Comment.objects.filter(owner__username__iexact=owner)
            return queryset
        else:
            queryset = Comment.objects.all()
            return queryset


class PostCommentList(View):

    def get(self, request, postslug):
        comments = Comment.objects.filter(post__slug__iexact=postslug)
        context = {'comments': comments}
        return render(request, 'commentmanager/includes/comment_list_page.html', context)


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
        return redirect(reverse('postmanager:post_detail', kwargs={'slug':post.slug}))


class CommentUpdate(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.owner:
            form = CommentForm(instance=comment)
            context = {'comment': comment, 'form': form}
            return render(request, 'commentmanager/includes/comment_update_modal.html', context)
        else:
            data = {'data': 'You is not owner'}
            return JsonResponse(data)

    @method_decorator(login_required)
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.owner:
            form = CommentForm(request.POST, instance=comment)
            form.save()
            data = {'data': 'Comment has been updated'}
            return JsonResponse(data)
        else:
            data = {'data': 'You is not owner'}
            return JsonResponse(data)


class CommentDelete(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.owner:
            context = {'comment': comment}
            return render(request, 'commentmanager/includes/comment_delete_modal.html', context)
        else:
            data = {'data': 'You is not owner'}
            return JsonResponse(data)

    @method_decorator(login_required)
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.owner:
            comment.delete()
            data = {'info': 'Comment has been deleted'}
        else:
            data = {'info': 'You is not owner'}
        return JsonResponse(data)





