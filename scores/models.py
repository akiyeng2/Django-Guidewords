from django.db import models

# Create your models here.


class Round(models.Model):
    round_number = models.AutoField(primary_key=True)

    def __str__(self):
        return "Round" + str(self.round_number)


class Player(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    wins = models.DecimalField(decimal_places=1, max_digits=5)
    losses = models.DecimalField(decimal_places=1, max_digits=5)
    spread = models.IntegerField()

    def __str__(self):
        return "#" + str(self.number) + " " + self.name

class Game(models.Model):

    board_num = models.IntegerField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, related_name="player1")
    player2 = models.ForeignKey(Player, related_name="player2")
    player1Score = models.IntegerField()
    player2Score = models.IntegerField()
    isEntered = models.BooleanField(default = False)

    def __str__(self):
        return self.player1.name + " vs. " + self.player2.name
