from django.core.management.base import BaseCommand
from scores.models import Game, Player, TourneyRound, Division
import re
class Command(BaseCommand):
    help = "Loads tournament rounds and players"

    def handle(self, *args, **options):
        num_rounds = 2
        div_num = 1
        curr_div = Division(divID=str(div_num))
        curr_div.save()
        with open("entrants-3.txt") as f:
            player_num = 1
            for r in range(1, num_rounds + 1):
                curr_round = TourneyRound(division=curr_div, round_number=r)
                curr_round.save()
            for curr_line in f:
                if not curr_line.strip():
                    div_num += 1
                    player_num = 1
                    curr_div = Division(divID=str(div_num))
                    curr_div.save()
                    for r in range(1, num_rounds + 1):
                        curr_round = TourneyRound(division=curr_div, round_number=r)
                        curr_round.save()
                else:
                    comma_ind = curr_line.index(",")
                    last_name = curr_line[:comma_ind]
                    first_name = curr_line[comma_ind + 2:curr_line.index(" ", comma_ind + 2)]
                    rating_start_ind = re.search("\d", curr_line).start()
                    rating = curr_line[rating_start_ind:curr_line.index(";")]
                    curr_player = Player(number=player_num, name=first_name + " " + last_name, division=curr_div,
                                         initial_rating=rating)
                    player_num += 1
                    curr_player.save()
