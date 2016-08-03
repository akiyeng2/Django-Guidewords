from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<round_id>[0-9]+)/$', views.round, name='round'),
    url(r'^(?P<round_id>[0-9]+)/games/view/(?P<game_id>[0-9]+)/$', views.game, name='game'),
    url(r'^(?P<round_id>[0-9]+)/games/score/(?P<game_id>[0-9]+)/$', views.enterScore, name='enterScore'),
]