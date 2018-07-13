from django.conf.urls import url
from ...review.review_phrasal_views import learning_phrasal, next_phrasal, get_sentence_phrasal_number, \
    get_sentence_phrasal, learned_phrasal

urlpatterns = [

    url(
        regex=r'^learning_phrasal$',
        view=learning_phrasal,
        name='learning_phrasal'
    ),
    url(
        regex=r'^next_phrasal$',
        view=next_phrasal,
        name='next_phrasal'
    ),
    url(
        regex=r'^get_sentence_phrasal_number/([\w ]+)$',
        view=get_sentence_phrasal_number,
        name='get_sentence_phrasal_number'
    ),
    url(
        regex=r'^get_sentence_phrasal/([\w ]+)$',
        view=get_sentence_phrasal,
        name='get_sentence'
    ),
    url(
        regex=r'^learned_phrasal/([\w ]+)$',
        view=learned_phrasal,
        name='learned_phrasal'
    ),

]