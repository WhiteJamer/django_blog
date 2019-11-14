from django.conf.urls import url
from .views import CategoryCreate, CategoryList, CategoryDetail, CategoryUpdate, CategoryDelete

app_name = 'categorymanager'

urlpatterns = [
    url(r'^add/$', CategoryCreate.as_view(), name='category_add'),
    url(r'^$', CategoryList.as_view(), name='category_list'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', CategoryUpdate.as_view(), name='category_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CategoryDelete.as_view(), name='category_delete'),
]
