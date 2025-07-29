import math
#learning combinations and permutations using math module
players = 10
teams_of = 3
ways_to_choose = math.comb(players, teams_of)
#math.comb calculates the number of ways to choose a team of players.combinations
# The comb function computes the number of combinations of choosing 'teams_of' players
# from a group of players without regard to the order of selection.
print(f"Ways to choose a team: {ways_to_choose}") # Outputs 120