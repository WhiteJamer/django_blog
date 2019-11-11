from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^u/', include('uprofile.urls')),
    url(r'^posts/', include('postmanager.urls')),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^auth/', include('django.contrib.auth.urls')),
]
