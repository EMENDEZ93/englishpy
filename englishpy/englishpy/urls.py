from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('english_py.practise.urls.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
