from django.conf.urls import url, include

from ..review.views import home, next_verb, next_sentence, learned_word, get_past, get_past_participle, \
    get_sentence_number, get_sentence
from ..reload.views import reload, delete_all_verb, reload_other_time, delete_all_other


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
    url(
        regex=r'^get_past/(?P<present>\w+)$',
        view=get_past,
        name='get_past'
    ),
    url(
        regex=r'^get_past/participle/(?P<present>\w+)$',
        view=get_past_participle,
        name='get_past_participle'
    ),
    url(
        regex=r'^get_sentence_number/(?P<present>\w+)$',
        view=get_sentence_number,
        name='get_sentence_number'
    ),
    url(
        regex=r'^get_sentence/(?P<_id>\d+)/(?P<present>\w+)$',
        view=get_sentence,
        name='get_sentence'
    ),
    url(
        regex=r'^learned_word/(?P<learned_word>\w+)$',
        view=learned_word,
        name='learned_word'
    ),
    url(
        regex=r'^reading$',
        view=reload,
        name='reload'
    ),
    url(
        regex=r'^delete$',
        view=delete_all_verb,
        name='delete_all_verb'
    ),
    url(
        regex=r'^othertime$',
        view=reload_other_time,
        name='reload_other_time'
    ),


    url(
        regex=r'^delete_other$',
        view=delete_all_other,
        name='delete_all_other'
    ),


    url(
        regex=r'^next_sentence$',
        view=next_sentence,
        name='next_sentence'
    ),


]
