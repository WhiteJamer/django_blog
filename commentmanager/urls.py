from django.conf.urls import url
from .views import CommentList, CommentCreate, CommentDelete, CommentUpdate, PostCommentList

app_name = 'commentmanager'

urlpatterns = [
    url(r'^$', CommentList.as_view(), name='comment_list'),
    url(r'^add_comment/(?P<post_slug>[\w-]+)/$', CommentCreate.as_view(), name='comment_add'),

    url(r'^(?P<pk>\d+)/delete/$', CommentDelete.as_view(), name='comment_delete'),
    url(r'^(?P<pk>\d+)/update/$', CommentUpdate.as_view(), name='comment_update'),
    url(r'^(?P<postslug>[\w-]+)/$', PostCommentList.as_view(), name='comment_list'),
]
