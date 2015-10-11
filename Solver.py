__author__ = 'Ivan'

from pyevolve import *
from pyevolve import G1DList
from pyevolve import GSimpleGA
from datetime import *
import itertools
from operator import le


class Solver:

    @property
    def number_of_components(self): return self
    @property
    def number_of_units(self): return self
    @property
    def vec_trade_off_f(self): return self
    @property
    def component_matrix(self): return self
    @property
    def mat_norm_components(self): return self
    @property
    def mat_norm_units(self): return self
    @property
    def mat_norm_resources(self): return self
    @property
    def resource_matrix(self): return self
    @property
    def resource_availability(self): return self
    @property
    def unit_matrix(self): return self

    def __init__(self, number_of_components, number_of_units, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, resource_matrix, resource_availability, unit_matrix):
        self.number_of_components = number_of_components
        self.number_of_units = number_of_units
        self.vec_trade_off_f = vec_trade_off_f
        self.mat_norm_components = mat_norm_components
        self.mat_norm_units = mat_norm_units
        self.mat_norm_resources = mat_norm_resources
        self.resource_matrix = resource_matrix
        self.resource_availability = resource_availability
        self.unit_matrix = unit_matrix


    def solve_by_genetic_algorithm(self, skip_same_platform = True, verbose = False):
        startTime = datetime.now();

        genome = G1DList.G1DList(self.number_of_components)
        genome.setParams(rangemin = 0, rangemax = self.number_of_units - 1)
        genome.evaluator.set(self.fitness_function)

        ga = GSimpleGA.GSimpleGA(genome)
        ga.setMinimax(Consts.minimaxType["minimize"])
        #ga.setInteractiveMode(False)
        ga.setGenerations(50)
        ga.setMutationRate(0.05)
        ga.setCrossoverRate(0.95)
        ga.setPopulationSize(50)
        ga.selector.set(Selectors.GRouletteWheel)

        #ga.setMultiProcessing(True)
        ga.evolve(freq_stats = 0)
        # end time measuring
        endTime = datetime.now()
        best = ga.bestIndividual()
        #minWeight = ga.bestIndividual().getFitnessScore()

        result = []
        for i in best:
            result.append(i)

        res = {"result": result,
               "score": self.fitness_function(result, False),
               "type":skip_same_platform,
               "time":endTime-startTime,
               "method": "Genetic Algorithm"}

        return res
    # end method solve_by_genetic_algorithm

    def fitness_function(self, result, shorter=True):
        g, resource_weight, communication_weight, weight = 0, 0, 0, 0

        #resources
        for d in range(0, len(self.vec_trade_off_f) - 1):
            for k in result:
                resource_weight += (self.mat_norm_resources[d][int(k)][g] * self.vec_trade_off_f[d])
                g += 1
            g = 0

        # communication
        for m in range(0,len(result)):
            for n in range (m,len(result)):
                if m != n and self.mat_norm_components[m][n] != 0:
                    communication_weight += self.mat_norm_components[m][n] * self.mat_norm_units[result[m]][result[n]]

        # communication * trade off
        communication_weight = (communication_weight * (self.vec_trade_off_f[len(self.vec_trade_off_f) - 1]))

        if shorter:
            weight = communication_weight + resource_weight
            if not self.is_solution_valid(result):
                weight += 1000000
            return weight
        else:
            weight = communication_weight + resource_weight
            return [weight, communication_weight, resource_weight]
    # end method fitness_function

    def manual_fitness(self, result):
        g, resource_weight, communication_weight = 0, 0, 0

        #resources
        for component, allocated_to in enumerate(result):
            for resource in range(len(self.vec_trade_off_f) - 1):
                resource_weight += self.mat_norm_resources[resource][allocated_to][component] * self.vec_trade_off_f[resource]

        # communication
        for m in range(0, len(result)):
            for n in range (m, len(result)):
                if m != n and self.mat_norm_components[m][n] != 0:
                    communication_weight += self.mat_norm_components[m][n] * self.mat_norm_units[result[m]][result[n]]

        # communication * trade off
        communication_weight = (communication_weight * (self.vec_trade_off_f[len(self.vec_trade_off_f) - 1]))

        print resource_weight
        print communication_weight

    def is_solution_valid(self, solution, verbose=False):
        number_of_resources = len(self.vec_trade_off_f) - 1
        resource_demand = [[0 for col in range(self.number_of_units)] for row in range(number_of_resources)]

        for component, allocated_to in enumerate(solution):
            for resource in range(number_of_resources):
                resource_demand[resource][allocated_to] += self.resource_matrix[resource][allocated_to][component]

        if verbose:
            print "\n Resource demand: ", resource_demand
            print " Resource availability: ", self.resource_availability

        if all(map(le, list(itertools.chain.from_iterable(resource_demand)),
                   list(itertools.chain.from_iterable(self.resource_availability)))):
            return True
        else:
            return False

    def architectural_constraints_valid(self, solution):

        pass



#end class Solver

