from django.conf.urls import url
from .views import PostList, PostDetail, PostCreate, PostDelete

app_name = 'postmanager'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^add/$', PostCreate.as_view(), name='post_add'),

    url(r'^(?P<slug>[\w-]+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^(?P<slug>[\w-]+)/delete$', PostDelete.as_view(), name='post_delete'),
]
