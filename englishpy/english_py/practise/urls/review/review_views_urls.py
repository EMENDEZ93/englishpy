from django.conf.urls import url
from ...review.review_views import review

urlpatterns = [

    url(
        regex=r'^review$',
        view=review,
        name='review'
    ),

]