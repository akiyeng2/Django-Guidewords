from scores.models import Game, Player, TourneyRound, Division

#Later, the file name and number of rounds will be values specified by the director when they create a tournament.
f = open("entrants-3.txt", "r")
num_rounds = 2

curr_line = f.readline()
div_num = 1
while curr_line != None:
    curr_div = Division(divID=str(div_num))
    curr_div.save()
    for r in range(1,num_rounds+1):
        curr_round = TourneyRound(division = curr_div, round_number = r)
        curr_round.save()

    player_num = 1
    while curr_line != '\n':
        comma_ind = curr_line.index(",")
        last_name = curr_line[:comma_ind]
        first_name = curr_line[comma_ind+2:curr_line.index(" ", comma_ind+2)]
        rating_start_ind = 0
        for i in range(len(curr_line)):
            if curr_line[i] in [str(i) for i in range(10)]:
                rating_start_ind = i
                break
        rating = curr_line[rating_start_ind :curr_line.index(";")]
        curr_player = Player(number=player_num, name=first_name+" "+last_name, division = curr_div, initial_rating = rating)
        curr_player.save()
        curr_line = f.readline()
        player_num += 1

    curr_line = f.readline()
    div_num += 1

f.close()
