from django.conf.urls import url
from ...reload.reload_phrasal import reload_phrasal


urlpatterns = [

    url(
        regex=r'^phrasal$',
        view=reload_phrasal,
        name='reload_phrasal'
    ),

]