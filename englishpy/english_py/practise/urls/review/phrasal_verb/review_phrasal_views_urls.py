from django.conf.urls import url, include
from ....review.phrasal_verb.review_phrasal_views import review_phrasal


urlpatterns = [
    url(
        regex=r'^review_phrasal$',
        view=review_phrasal,
        name='review_phrasal'
    ),
]