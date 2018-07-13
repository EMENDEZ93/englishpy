from django.conf.urls import url
from ...load_topic.views import topic, topic_delete

urlpatterns = [

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

]
