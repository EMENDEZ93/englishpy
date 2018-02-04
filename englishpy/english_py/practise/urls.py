from django.conf.urls import url, include
from review.views import home, next_verb

urlpatterns = [
    url(
        regex=r'^home$',
        view=home,
        name='home'
    ),
    url(
        regex=r'^next_verb$',
        view=next_verb,
        name='next_verb'
    ),
]
