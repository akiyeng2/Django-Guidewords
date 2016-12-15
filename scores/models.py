from django.db import models

class Division(models.Model):

    divID = models.CharField(max_length=100)
    div_num = models.AutoField(primary_key=True)

    def __str__(self):
        return "Division" + self.divID

class Round(models.Model):

    round_number = models.IntegerField(default=1)

    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Round" + str(self.round_number)


class Player(models.Model):

    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    wins = models.DecimalField(decimal_places=1, max_digits=5, default = 0)
    losses = models.DecimalField(decimal_places=1, max_digits=5, default = 0)
    spread = models.IntegerField(default = 0)

    def __str__(self):
        return "#" + str(self.number) + " " + self.name


class Game(models.Model):

    board_num = models.IntegerField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, related_name="player1")
    player2 = models.ForeignKey(Player, related_name="player2")
    player1Score = models.IntegerField(default = 0)
    player2Score = models.IntegerField(default = 0)
    isEntered = models.BooleanField(default = False)

    def __str__(self):
        return self.player1.name + " vs. " + self.player2.name
