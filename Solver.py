__author__ = 'Ivan'

import SolutionVerifier as sv
import GASolver as ga
import SASolver as sa

class Solver:

    def __init__(self):
        self.solution_verifier = sv.SolutionVerifier()

    def solve(self, method="SASolver"):
        initial_state = [0] * 11
        return{
            "SASolver" : sa.SASolver(initial_state),
            "GASolver" : ga.GASolver().solve()
        }[method]