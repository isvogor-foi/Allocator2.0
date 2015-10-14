__author__ = 'ivan'

from Solver import Solver
from simanneal import Annealer
import random

class SASolver(Annealer, Solver):

    Tmax = 1000000.0
    Tmin = 0.5
    steps = 15000
    updates = 0  # number of outputs
    copy_strategy = 'deepcopy'
    user_exit = False
    save_state_on_exit = True

    def move(self):
        self.state = []
        for i in range(0, 11):
            self.state.append(random.randint(0, 3))

    def energy(self):
        evaluated = self.fitness_function(self.state)[0]
        return evaluated

#end class SASolver