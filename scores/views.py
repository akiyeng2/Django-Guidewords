from django.shortcuts import render
from django.http import HttpResponse

from .models import Round, Game
from .forms import ScoreForm
# Create your views here.


def index(request):
    rounds = Round.objects.all()
    context = {'round_list': rounds}
    return render(request, 'scores/index.html', context)


def round(request, round_id):
    games = Round.objects.get(pk=round_id).game_set.all()
    context = {
        'game_list': games,
        'round_number': round_id
    }
    return render(request, 'scores/round.html', context)

def game(request, round_id, board_num):
    game = Game.objects.get(round_id = round_id, board_num = board_num)
    context = {
        'player1Number': game.player1.number,
        'player2Number': game.player2.number,
        'player1Name': game.player1.name,
        'player2Name': game.player2.name,
        'player1Score': game.player1Score,
        'player2Score': game.player2Score
    }
    return render(request, 'scores/finishedGame.html', context)


def enterScore(request, round_id, board_num):
    game = Game.objects.get(round_id = round_id, board_num = board_num)

    
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            game.player1Score = form.cleaned_data['player1Score']
            game.player2Score = form.cleaned_data['player2Score']
            game.save()

        context = {
            'player1Number': game.player1.number,
            'player2Number': game.player2.number,
            'player1Name': game.player1.name,
            'player2Name': game.player2.name,
            'player1Score': game.player1Score,
            'player2Score': game.player2Score,
        }
        return render(request, 'scores/finishedGame.html', context)
    else:
        form = ScoreForm()
        form.setup(game.player1, game.player2)
        context = {
            'form': form,
            'round_id': round_id,
            'game_id': board_num
        }
        return render(request, 'scores/unfinishedGame.html', context)
