__author__ = 'ivan'

from simanneal import Annealer
import Solver as solver
import random

class SASolver(Annealer):

    def move(self):
        for i in range(0, 11):
            self.state.append(random.randint(0,3))

    def energy(self):
        return sum(self.state)


#end class SASolver