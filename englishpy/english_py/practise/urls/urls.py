from django.conf.urls import url, include
from .review.phrasal_verb.review_phrasal_views_urls import urlpatterns as review_phrasal_views_urls
from .review.review_phrasal_views_urls import urlpatterns as review__review_phrasal_views_urls
from .review.review_views_urls import urlpatterns as review_views_urls
from .review.views_urls import urlpatterns as review__views_urls

from .reload.reload_phrasal_urls import urlpatterns as reload_phrasal_urls
from .reload.reload_sentence_urls import urlpatterns as reload_sentence_urls
from .reload.views_urls import urlpatterns as reload_views_urls

from .load_topic.views_urls import urlpatterns as load_topic_views_urls


urlpatterns = [] + \
    review_phrasal_views_urls + \
    review__review_phrasal_views_urls + \
    review_views_urls + \
    review_views_urls + \
    review__views_urls + \
    reload_phrasal_urls + \
    reload_sentence_urls + \
    reload_views_urls + \
    load_topic_views_urls
