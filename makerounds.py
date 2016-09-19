from scores.models import Game, Player, Round

r1 = Round()
r1.save()
r2 = Round()
r2.save()

p1 = Player(number = 1, name = "Rafi Stern")
p1.save()
p2 = Player(number = 2, name = "Amalan Igengar")
p2.save()
p3 = Player(number = 3, name = "Noah Walton")
p3.save()
p4 = Player(number = 4, name = "Kevin Bolerman")
p4.save()

g1 = Game(board_num = 1, round = r1, player1 = p1, player2 = p2)
g1.save()
g2 = Game(board_num = 2, round = r1, player1 = p3, player2 = p4)
g2.save()
g3 = Game(board_num = 1, round = r2, player1 = p1, player2 = p3)
g3.save()
g4 = Game(board_num = 2, round = r2, player1 = p2, player2 = p4)
g4.save()
