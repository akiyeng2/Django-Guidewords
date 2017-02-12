

#This only works if the number of players is even. We have to figure out whether bye handling is done by something else.
def rr_pairings(players):
    rounds = []
    n = len(players)
    #top_out is just all the players with the first removed, to facilitate round-robin pairings, as described on Wikipedia.
    top_out = players[1:]
    for r in range(1,n):
        new_round = []
        for ind in range(n//2-1):
            new_round.append((top_out[ind], top_out[n-ind-2]))
        new_round.append((players[0], top_out[n//2-1]))
        rounds.append(new_round)
        top_out = [top_out[-1]] + top_out[:-1]
    return rounds


print(rr_pairings(["A", "B", "C", "D", "E", "F", "G", "H"]))
