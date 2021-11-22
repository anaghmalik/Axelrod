from axelrod import Player, Action
from random import choices

C, D = Action.C, Action.D

class CustomPlayer(Player):
    def __init__(self, prob_list=[1,1,1,1]):
        super().__init__()
        self.state_nums = [0,0,0,0]
        self.next_state_cooperate_nums = [0,0,0,0]

    def reset_nums(self):
        self.state_nums = [0,0,0,0]
        self.next_state_cooperate_nums = [0,0,0,0]

    def strategy(self, opponent):
        """ Begins by playing 'C': This strategy simply has a distribution of actions conditioned on the last state"""
        if len(self.history) == 0 or len(self.history) == 1:
            action = choices([C, D], [0.5, 0.5])[0]
            self.reset_nums()
            return action


        elif len(self.history)>1:

            #update probabilities
            second_last_run = (self.history[-2], opponent.history[-2])
            possible_runs = [(C, C), (C, D), (D, C), (D, D)]
            second_last_run_index = possible_runs.index(second_last_run)
            self.state_nums[second_last_run_index] += 1
            if opponent.history[-1] == C:
                self.next_state_cooperate_nums[second_last_run_index] += 1

            #sample action
            last_run = (self.history[-1], opponent.history[-1])
            possible_runs = [(C, C), (C, D), (D, C), (D, D)]
            last_run_index = possible_runs.index(last_run)

            #with prob 0.1 choose random action
            which_action = choices(["probs", "random"], [0.9, 0.1])[0]
            if which_action == "probs" and len(self.history)>20:
                try:
                    cooperate_prob = self.next_state_cooperate_nums[last_run_index]/self.state_nums[last_run_index]
                    action = choices([C, D], [cooperate_prob, 1 - cooperate_prob])[0]
                    return action
                except:
                    #here if not enough observations to find probability
                    action = choices([C, D], [0.5, 0.5])[0]
                    return action
            else:
                action = choices([C, D], [0.5, 0.5])[0]
                return action

    def __repr__(self):
        """ The string method for the strategy. """
        return 'CustomPlayer'
