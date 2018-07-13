from django.conf.urls import url
from ...reload.reload_sentence import reload_sentence


urlpatterns = [

    url(
        regex=r'^sentence$',
        view=reload_sentence,
        name='reload_sentence'
    ),

]
