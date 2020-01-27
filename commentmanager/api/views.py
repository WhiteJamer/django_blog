from rest_framework.generics import ListAPIView
from commentmanager.models import Comment
from .serializers import PostCommentsSerializer


class PostComments(ListAPIView):
    '''
    Возвращает комментарии к конкретному посту
    '''
    serializer_class = PostCommentsSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id__exact=post_id)