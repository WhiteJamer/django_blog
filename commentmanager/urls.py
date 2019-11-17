from django.conf.urls import url
from .views import CommentList, CommentCreate, CommentDelete

app_name = 'commentmanager'

urlpatterns = [
    url(r'^$', CommentList.as_view(), name='comment_list'),
    url(r'^add_comment/(?P<post_slug>[\w-]+)/$', CommentCreate.as_view(), name='comment_add'),

    url(r'^(?P<pk>\d+)/delete$', CommentDelete.as_view(), name='comment_delete'), # fixit
]
