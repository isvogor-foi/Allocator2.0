__author__ = 'ivan'

from simanneal import Annealer
import random

class SASolver(Annealer):

    Tmax = 1000000.0
    Tmin = 0.5
    steps = 15000
    updates = 20
    copy_strategy = 'deepcopy'
    user_exit = False
    save_state_on_exit = True

    def setup_solver(self, solver):
        self.solver = solver

    def move(self):
        self.state = []
        for i in range(0, 11):
            self.state.append(random.randint(0, 3))
        #print(self.state)

    def energy(self):
        evaluated = self.solver.eval_one_min(self.state)[0]
        return evaluated

#end class SASolver