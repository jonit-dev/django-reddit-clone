
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^posts/', include('posts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
