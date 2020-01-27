from django.conf.urls import url
from .views import PostComments

urlpatterns = [
    url(r'^(?P<post_id>\d+)/$', PostComments.as_view()),

]