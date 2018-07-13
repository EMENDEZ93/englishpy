from django.conf.urls import url
from ...reload.views import reload, delete_all_verb, reload_other_time, delete_all_other

urlpatterns = [

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

]