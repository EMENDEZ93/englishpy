from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from review.views import home

urlpatterns = [
    url(
        regex=r'^home$',
        view=home,
        name='home'
    ),
]
