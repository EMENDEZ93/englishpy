from django.conf.urls import url, include

from .reload.reload_sentence import reload_sentence
from .views import searcher
from .load_topic.views import topic, topic_delete
from .review.views import home, next_verb, next_sentence
from .reload.views import reload, delete_all_verb, reload_other_time, delete_all_other


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
        regex=r'^topic/(?P<id_topic>\d+)$',
        view=topic,
        name='topic'
    ),
    url(
        regex=r'^topic/(?P<id_topic>\d+)/vaciar$',
        view=topic_delete,
        name='topic_delete'
    ),

    url(
        regex=r'^searcher$',
        view=searcher,
        name='searcher'
    ),

    url(
        regex=r'^sentence$',
        view=reload_sentence,
        name='reload_sentence'
    ),
    url(
        regex=r'^next_sentence$',
        view=next_sentence,
        name='next_sentence'
    ),

]
