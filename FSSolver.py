__author__ = 'Ivan'

from datetime import *
from Solver import Solver
import itertools


class FSSolver(Solver):

    def solve(self, skip_same_platform=True, verbose=False):
        # need to check if solution is valid!!!
        print("Full space search started...")
        min_permutation = []
        min_weight = -1

        start_time = datetime.now()
        for i in itertools.product([i for i in range(0, self.number_of_units)], repeat=self.number_of_components):
            #print ("rezultat: ", i, ";  valid: ", " res: ",  self.manual_fitness(i))
            result = None
            if skip_same_platform:
                if not all(x == i[0] for x in i):
                    result = self.fitness_function(i)[0]
            else:
                result = self.fitness_function(i)[0]

            if result is not None:
                if min_weight > result or min_weight == -1:
                    min_weight = result
                    min_permutation = i

        end_time = datetime.now()

        res = {"result": min_permutation,
               "type": skip_same_platform,
               "time": end_time - start_time,
               "method": "Full space search"}

        return res
#end class BFSolver