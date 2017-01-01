from scores.models import Game, Player, TourneyRound, Division

d1=Division(divID="1")
d1.save()
d2=Division(divID="2")
d2.save()

r1d1=TourneyRound(division=d1, round_number=1)
r1d1.save()
r2d1=TourneyRound(division=d1, round_number=2)
r2d1.save()
r1d2=TourneyRound(division=d2, round_number=1)
r1d2.save()
r2d2=TourneyRound(division=d2, round_number=2)
r2d2.save()

p1d1=Player(number=1, name="Rafi Stern", division=d1)
p1d1.save()
p2d1=Player(number=2, name="Amalan Igengar", division=d1)
p2d1.save()
p1d2=Player(number=3, name="Noah Walton", division=d2)
p1d2.save()
p2d2=Player(number=4, name="Kevin Bolerman", division=d2)
p2d2.save()

g1r1d1=Game(board_num=1, tourney_round=r1d1, player1=p1d1, player2=p2d1)
g1r1d1.save()
g1r2d1=Game(board_num=1, tourney_round=r2d1, player1=p2d1, player2=p1d1)
g1r2d1.save()

g1r1d2=Game(board_num=1, tourney_round=r1d2, player1=p1d2, player2=p2d2)
g1r1d2.save()
g2r2d2=Game(board_num=1, tourney_round=r2d2, player1=p2d2, player2=p1d2)
g2r2d2.save()
