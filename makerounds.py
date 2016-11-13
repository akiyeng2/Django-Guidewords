from scores.models import Game, Player, Round, Division

d1 = Division(divID = "1")
d1.save()
d2 = Division(divID = "2")
d2.save()

r1d1 = Round(division = d1, round_number=1)
r1d1.save()
r2d1 = Round(division = d1, round_number=2)
r2d1.save()
r1d2 = Round(division = d2, round_number=1)
r1d2.save()
r2d2 = Round(division = d2, round_number=2)
r2d2.save()

p1d1 = Player(number = 1, name = "Rafi Stern", division = d1)
p1d1.save()
p2d1 = Player(number = 2, name = "Amalan Igengar", division = d1)
p2d1.save()
p1d2 = Player(number = 3, name = "Noah Walton", division = d2)
p1d2.save()
p2d2 = Player(number = 4, name = "Kevin Bolerman", division = d2)
p2d2.save()

g1d1 = Game(board_num = 1, round = r1d1, player1 = p1d1, player2 = p2d1)
g1d1.save()
