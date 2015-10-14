__author__ = 'Ivan'

import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from datetime import *
from Solver import Solver

class GASolver(Solver):


    # discrete values
    def solve(self, initial_state="" ):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMin)

        toolbox = base.Toolbox()

        # Attribute generator
        toolbox.register("attr_bool", random.randint, 0, 3)

        # Structure initializers
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 11)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", self.evaluate)
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        ###########################

        random.seed(64)

        pop = toolbox.population(n=300)
        hof = tools.HallOfFame(1)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("std", numpy.std)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)

        startTime = datetime.now()
        pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40,stats=stats, halloffame=hof, verbose=False)
        endTime = datetime.now()

        best_ind = tools.selBest(pop, 1)[0]

        res = {"result": best_ind,
               "method": "Genetic Algorithm", "pop" : pop, "log" : log, "hof" : hof,
               "type": "-", "time":endTime - startTime}

        #print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

        return res

    # end method solve_by_genetic_algorithm

    def evaluate(self, individual):
        return self.fitness_function(individual)
        #return self.fitness_function(individual)