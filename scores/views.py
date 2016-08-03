from django.shortcuts import render
from django.http import HttpResponse

from .models import Round, Game
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

def game(request, round_id, game_id):
    game = Game.objects.get(pk=game_id)
    context = {
        'player1Number': game.player1.number,
        'player2Number': game.player2.number,
        'player1Name': game.player1.name,
        'player2Name': game.player2.name,
        'player1Score': game.player1Score,
        'player2Score': game.player2Score
    }
    return render(request, 'scores/finishedGame.html', context)


def enterScore(request, round_id, game_id):
    game = Game.objects.get(pk=game_id)
    context = {
        'round_id': round_id,
        'game_id': game_id,
        'player1': game.player1,
        'player2': game.player2
    }

    return render(request, 'scores/unfinishedGame.html', context)