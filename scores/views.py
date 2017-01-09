from django.shortcuts import render
from django.http import HttpResponse

from .models import TourneyRound, Game, Player, Division
from .forms import ScoreForm
from decimal import Decimal
# Create your views here.


def index(request):
    divisions = Division.objects.all()
    context = {'division_list': divisions}
    return render(request, 'scores/index.html', context)


def division(request, div_num):
    rounds = Division.objects.get(divID=div_num).tourneyround_set.all()
    players = Player.objects.filter(division__divID=div_num).order_by('-wins', '-spread')

    context = {
        'round_list': rounds,
        'player_list': players,
        'division_id': div_num
    }

    return render(request, 'scores/division.html', context)


def tourney_round(request, div_num, round_id):

    games = TourneyRound.objects.get(division__divID=div_num, round_number=round_id).game_set.all()

    context = {
        'game_list': games,
        'round_number': round_id,
        'division_number': div_num
    }
    return render(request, 'scores/round.html', context)


def player(request, div_num, player_id):
    player = Player.objects.get(division__divID=div_num, number=player_id)
    context = {
        'player': player
    }

    return render(request, 'scores/player.html', context)


def listPlayers(request, div_num):
    print(div_num)
    players = Player.objects.filter(division__divID=div_num)
    print(players)
    context = {
        'player_list': players
    }

    return render(request, 'scores/listPlayers.html', context)


def game(request, div_num, round_id, board_num):
    game = Game.objects.get(tourney_round__round_number=round_id, tourney_round__division__divID=div_num, board_num = board_num)

    context = {
        'division_number': div_num,
        'round_number': round_id,
        'player1Number': game.player1.number,
        'player2Number': game.player2.number,
        'player1Name': game.player1.name,
        'player2Name': game.player2.name,
        'player1Score': game.player1Score,
        'player2Score': game.player2Score
    }
    return render(request, 'scores/finishedGame.html', context)


def handleScore(request, div_num, round_id, board_num):
    curr_game = Game.objects.get(tourney_round__round_number=round_id, tourney_round__division__divID=div_num, board_num=board_num)

    if curr_game.isEntered:
        print(div_num, round_id, board_num)

        return game(request, div_num, round_id, board_num)

    else:
        if request.method == 'POST':
            form = ScoreForm(request.POST)
            if form.is_valid():
                curr_game.player1Score = form.cleaned_data['player1Score']
                curr_game.player2Score = form.cleaned_data['player2Score']
                p1 = curr_game.player1
                p2 = curr_game.player2
                diff = curr_game.player1Score - curr_game.player2Score
                tie = Decimal(0.5)
                if diff > 0:
                    p1.wins += 1
                    p2.losses += 1
                elif diff < 0:
                    p1.losses += 1
                    p2.wins += 1
                else:
                    p1.wins += tie
                    p1.losses += tie
                    p2.wins += tie
                    p2.losses += tie
                p1.spread += diff
                p2.spread -= diff
                curr_game.isEntered = True
                p1.save()
                p2.save()
                curr_game.save()

            return game(request, div_num, round_id, board_num)
        else:
            form = ScoreForm()
            form.setup(curr_game.player1, curr_game.player2)
            context = {
                'form': form,
                'division_number': div_num,
                'round_number': round_id,
                'game_id': board_num
            }
            return render(request, 'scores/unfinishedGame.html', context)
