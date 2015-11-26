__author__ = 'Ivan'

import numpy as np
from Solver import Solver

# RANDOM SOLVER
class RASolver(Solver):

    def solve(self, skip_same_platform=False, verbose=False):
        random_allocation = np.random.randint(self.number_of_units, size = self.number_of_components).tolist()
        res = {
            "result": random_allocation,
            "method": "Random",
            "time": 0}
        return res
#end class RASolver