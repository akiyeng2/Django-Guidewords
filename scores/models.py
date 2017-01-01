from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Division(models.Model):

    divID = models.CharField(max_length=100)
    div_num = models.AutoField(primary_key=True)

    def __str__(self):
        return "Division" + self.divID


class TourneyRound(models.Model):

    round_number = models.IntegerField(default=1)

    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Round" + str(self.round_number)

    class Meta:
        unique_together = ("round_number", "division")


class Player(models.Model):

    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    wins = models.DecimalField(decimal_places=1, max_digits=5, default = 0)
    losses = models.DecimalField(decimal_places=1, max_digits=5, default = 0)
    spread = models.IntegerField(default = 0)
    initial_rating = models.IntegerField(default=1000)


    def __str__(self):
        return "#" + str(self.number) + " " + self.name

    class Meta:
        unique_together = ("number", "division")


class Game(models.Model):

    board_num = models.IntegerField()
    tourney_round = models.ForeignKey(TourneyRound, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, related_name="player1")
    player2 = models.ForeignKey(Player, related_name="player2")
    player1Score = models.IntegerField(default=0)
    player2Score = models.IntegerField(default=0)
    isEntered = models.BooleanField(default=False)

    def clean(self):
        games = self.tourney_round.game_set.all()
        for other_game in games:
            if other_game.player1.number in (self.player1.number, self.player2.number) or other_game.player2.number in (self.player1.number, self.player2.number):
                raise ValidationError(_('One player in two games'), code = 'duplicate')
        if self.player1.number == self.player2.number:
            raise ValidationError(_('Player is playing himself'), code = 'sameplayer')
        if self.tourney_round.division.div_num != self.player1.division.div_num:
            raise ValidationError(_('Player in wrong division'), code = 'wrongdivision')

    def __str__(self):
        return self.player1.name + " vs. " + self.player2.name

    class Meta:
        unique_together = (("board_num", "tourney_round"), ("player1", "tourney_round"), ("player2", "tourney_round"))
