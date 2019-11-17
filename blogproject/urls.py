from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^u/', include('uprofile.urls')),
    url(r'^posts/', include('postmanager.urls')),
    url(r'^categories/', include('categorymanager.urls')),
    url(r'^comments/', include('commentmanager.urls')),
    url(r'^auth/', include('customauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
