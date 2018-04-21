from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from sixerrapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('sixerrapp.urls')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
