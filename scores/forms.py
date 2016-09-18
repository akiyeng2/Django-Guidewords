from django import forms

# Defines a form to be used for entering the score of a game


class ScoreForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)

    player1Score = forms.IntegerField()
    player2Score = forms.IntegerField()

    # Sets the form labels to the player number and name
    def setup(self, player1, player2):
        self.fields['player1Score'].label = player1
        self.fields['player2Score'].label = player2
