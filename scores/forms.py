from django import forms
from .models import Game


class ScoreForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super(ScoreForm, self).__init__(*args, **kwargs)

    player1Score = forms.IntegerField()
    player2Score = forms.IntegerField()

    def setup(self, player1, player2):
        self.fields['player1Score'].label = player1
        self.fields['player2Score'].label = player2