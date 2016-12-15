from django.contrib import admin
from .models import TourneyRound, Game, Player, Division


# Register your models here.


admin.site.register(TourneyRound)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Division)
