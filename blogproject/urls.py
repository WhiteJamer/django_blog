from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^u/', include('uprofile.urls')),
    url(r'^posts/', include('postmanager.urls')),
    url(r'^auth/', include('customauth.urls')),

]
