from django.shortcuts import render
from django.http import HttpResponse

from .models import Round, Game, Player
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

def player(request, player_id):
    player = Player.objects.get(pk=player_id)
    context = {
        'player': player
    }

    return render(request, 'scores/player.html', context)

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


def handleScore(request, round_id, board_num):
    curr_game = Game.objects.get(round_id = round_id, board_num = board_num)

    if curr_game.isEntered:
        return game(request, round_id, board_num)

    else:
        if request.method == 'POST':
            form = ScoreForm(request.POST)
            if form.is_valid():
                curr_game.player1Score = form.cleaned_data['player1Score']
                curr_game.player2Score = form.cleaned_data['player2Score']
                p1 = curr_game.player1
                p2 = curr_game.player2
                diff = curr_game.player1Score - curr_game.player2Score

                if diff > 0:
                    p1.wins += 1
                    p2.losses += 1
                elif diff < 0:
                    p1.losses += 1
                    p2.wins += 1
                else:
                    p1.wins += .5
                    p1.losses += .5
                    p2.wins += .5
                    p2.losses += .5
                p1.spread += diff
                p2.spread -= diff
                curr_game.isEntered = True
                p1.save()
                p2.save()
                curr_game.save()

            return game(request, round_id, board_num)
        else:
            form = ScoreForm()
            form.setup(curr_game.player1, curr_game.player2)
            context = {
                'form': form,
                'round_id': round_id,
                'game_id': board_num
            }
            return render(request, 'scores/unfinishedGame.html', context)
