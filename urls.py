from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^songs/$' , views.song_list ),
    url(r'^songs/(?P<pk>[0-9]+)/$' , views.song_detail),
    url(r'^predict/$' , views.predict )
]