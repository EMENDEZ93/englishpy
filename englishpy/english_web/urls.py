from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from views import home


urlpatterns = [
    url(r'^', home, name='home'),
]
