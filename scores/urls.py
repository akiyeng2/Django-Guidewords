from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^division/(?P<divNum>[0-9]+)/$', views.division, name='division'),
    url(r'^division/(?P<divNum>[0-9]+)/round/(?P<round_id>[0-9]+)/$', views.round, name='round'),
    url(r'^division/playerlist', views.listPlayers, name='playerlist'),
    url(r'^division/playerview/(?P<player_id>[0-9]+)/$', views.player, name='player'),
    url(r'^division/(?P<divNum>[0-9]+)/round/(?P<round_id>[0-9]+)/games/score/(?P<board_num>[0-9]+)/$', views.handleScore, name='handleScore'),
]
