import axelrod as axl
from omplayer import OneMemoryPlayer
from cust_player import CustomPlayer

dists = [[1/2, 0, 1/4, 0], [3/4, 1/2, 1/8, 0], [3/4, 0, 7/8, 1/2], [1, 1/2, 3/4, 1/2], [8/9, 1/2, 1/3, 0], [1, 1/2, 1/2, 0],[11/13, 1/2, 7/26, 0]]
players = [OneMemoryPlayer(prob_list=p) for p in dists]

players.append(CustomPlayer())
players.insert(0, axl.Cooperator())
players.insert(0, axl.Defector())
players.insert(0, axl.TitForTat())

tournament = axl.Tournament(players)
results = tournament.play()
plot = axl.Plot(results)
plot.save_all_plots(title_prefix="all_players", filetype="png")
results.write_summary('summary.csv')








