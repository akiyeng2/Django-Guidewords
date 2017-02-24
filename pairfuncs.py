from copy import deepcopy

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

#WARNING: No Gibsons in here! Again, assumes byes have been taken care of.
def koth_pairings(players):
    return [(players[2*i], players[2*i+1]) for i in range(len(players)//2)]

#This Swiss algorithm copies the one from http://stackoverflow.com/questions/28629235/swiss-tournament-pairing-algorithm . It takes two parameters: players (a list of players, listed in order from highest to lowest in ranking) and opp_dict (each key is a player, and the corresponding value is the list of that player's opponents so far).
def swiss_pairings(players, opp_dict):
    player_copy = deepcopy(players)
    pairings = []
    players_left = len(players)
    while player_copy != []:
        for p in enumerate(player_copy[1:]):
            if p[1] not in opp_dict[player_copy[0]]:
                pairings.append((player_copy[0],p[1]))
                player_copy.remove(p[1])
                player_copy.remove(player_copy[0])
                break
            elif p[0] == players_left-2:
                pairings.append((player_copy[0],player_copy[1]))
                player_copy = player_copy[2:]
                break
            else:
                pass
        players_left -= 2
    return pairings

#Given a list of players, and a number n which divides the length of players, divides the list into snaked groups (as in snake pairings). This is NOT a pairing algorithm, but a subroutine for the snake_pairings algorithm.
def snake(players, n):
    if len(players) % n != 0:
        raise("Sorry, the number of players does not evenly divide the group size.")
    num_groups = len(players)//n
    groups = [[] for g in range(num_groups)]
    for i in range(n):
        if i % 2 == 0:
            for j in range(num_groups):
                groups[j].append(players[i*num_groups+j])
        else:
            for j in range(num_groups):
                groups[num_groups-j-1].append(players[i*num_groups+j])
    return groups

#Given the players, hopefully listed by seed, matches them into groups of n players each, where n must divide the number of players. Uses a snake pairing to make groups evener (Note: There are ways to make groups still evener, but the algorithms might be a little more annoying. But this is possibly worth the annoyance, if enough people want it.)
def snake_pairings(players, n):
    rounds = [[] for r in range(n-1)]
    for group in snake(players,n):
        for r in enumerate(rr_pairings(group)):
            rounds[r[0]] += r[1]
    return rounds



print(rr_pairings(["A", "B", "C", "D", "E", "F"]) == [[('B', 'F'), ('C', 'E'), ('A', 'D')], [('F', 'E'), ('B', 'D'), ('A', 'C')], [('E', 'D'), ('F', 'C'), ('A', 'B')], [('D', 'C'), ('E', 'B'), ('A', 'F')], [('C', 'B'), ('D', 'F'), ('A', 'E')]])
print(koth_pairings(["A", "B", "C", "D", "E", "F"]) == [('A', 'B'), ('C', 'D'), ('E', 'F')])
swissps = ["A", "B", "C", "D", "E", "F", "G", "H"]
swissopps = {"A": ["C"], "B": ["F"], "C": ["A"], "D": ["E"], "E": ["D"], "F": ["B"], "G": ["H"], "H": ["G"]}
print(swiss_pairings(swissps, swissopps) == [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H')])
#Note that the above test case is an example where this Swiss algorithm causes repeats, though this particular scenario couldn't occur in a tournament (G and H are in the last two places despite only having played each other).
print(snake_pairings(list(range(20)), 4) == [[(9, 19), (0, 10), (8, 18), (1, 11), (7, 17), (2, 12), (6, 16), (3, 13), (5, 15), (4, 14)], [(19, 10), (0, 9), (18, 11), (1, 8), (17, 12), (2, 7), (16, 13), (3, 6), (15, 14), (4, 5)], [(10, 9), (0, 19), (11, 8), (1, 18), (12, 7), (2, 17), (13, 6), (3, 16), (14, 5), (4, 15)]])
