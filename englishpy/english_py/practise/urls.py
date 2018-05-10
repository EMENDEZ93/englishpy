from django.conf.urls import url, include
from .reload import reload_phrasal
from .views import searcher
from .load_topic.views import topic, topic_delete
from .review.views import home, next_verb, register_learned_word
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
        regex=r'^register_learned_word$',
        view=register_learned_word,
        name='register_learned_word'
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

    #url(
    #    regex=r'^phrasal$',
    #    view=reload_phrasal,
    #    name='reload_l'
    #),

]
