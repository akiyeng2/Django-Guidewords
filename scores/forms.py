from django import forms
from .models import Game

class ScoreForm(forms.Form):
    player1Score = forms.IntegerField(label = "happy")
    player2Score = forms.IntegerField(label = "christmas")
