__author__ = 'ivan'

import random

from Solver import Solver
from simanneal import Annealer
from datetime import *

class SASolver(Annealer, Solver):

    # algorithm settings
    Tmax = 1000000.0
    Tmin = 0.5
    steps = 20000
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

    def solve(self):
        start_time = datetime.now()
        solution, weight = self.anneal()
        end_time = datetime.now()

        res = {
            "result": solution,
            "method": "Simulated annealing",
            "time": end_time - start_time}
        return res

#end class SASolver