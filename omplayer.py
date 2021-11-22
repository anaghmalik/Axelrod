from axelrod import Player, Action
from random import choices


C, D = Action.C, Action.D

class OneMemoryPlayer(Player):
    def __init__(self, prob_list=[1,1,1,1]):
        super().__init__()
        self.prob_list = prob_list

    def strategy(self, opponent):
        """ Begins by playing 'C': This strategy simply has a distribution of actions conditioned on the last state"""
        if len(self.history) == 0:
            action = choices([C, D], [0.5, 0.5])[0]
            return action
        else:
            last_run = (self.history[-1], opponent.history[-1])
            possible_runs = [(C, C), (C, D), (D, C), (D, D)]
            last_run_index = possible_runs.index(last_run)
            cooperate_prob = self.prob_list[last_run_index]
            action = choices([C, D], [cooperate_prob, 1-cooperate_prob])[0]
            return action


    def __repr__(self):
        """ The string method for the strategy. """
        return 'OneMemoryPlayer'
