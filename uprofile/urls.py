from django.conf.urls import url
from .views import UserList, UserDetail, ProfileUpdate

app_name = 'uprofile'

urlpatterns = [
    url(r'^$', UserList.as_view(), name='user_list'),
    url(r'^(?P<slug>[\w-]+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ProfileUpdate.as_view(), name='profile_update'),
]
