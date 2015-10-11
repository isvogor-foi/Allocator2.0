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

    def __init__(self, number_of_components, number_of_units, vec_trade_off_f, component_matrix, mat_norm_components, mat_norm_resources, mat_norm_units, resource_matrix, resource_availability, unit_matrix):
        self.number_of_components = number_of_components
        self.number_of_units = number_of_units
        self.vec_trade_off_f = vec_trade_off_f
        self.component_matrix = component_matrix
        self.mat_norm_components = mat_norm_components
        self.mat_norm_units = mat_norm_units
        self.mat_norm_resources = mat_norm_resources
        self.resource_matrix = resource_matrix
        self.resource_availability = resource_availability
        self.unit_matrix = unit_matrix


    def solve_by_genetic_algorithm(self, skipSamePlatform = True, displayResult = False):
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
        minWeight = ga.bestIndividual().getFitnessScore()

        result = []
        for i in best: result.append(i)

        res = {"result": result, "score": self.fitnessFunctionTester(result), "type":skipSamePlatform,
               "time":endTime-startTime, "method": "Genetic Algorithm"}


        #self.printResult(res)
        print "Checking solution: ", self.solutionValid(result)


        return res
    # end method solve_by_genetic_algorithm

    def fitness_function(self, genome):
        g, resourceWeight, weight, minPermutation, minWeight = 0,0,0,0, -1
        for d in range(0, len(self.vec_trade_off_f) - 1):
            for k in genome:
                resourceWeight += (self.mat_norm_resources[d][int(k)][g] * self.vec_trade_off_f[d])
                g += 1
            g = 0
        communicationWeight = 0
        for m in range(0,len(genome)):
            for n in range (m,len(genome)):
                if m != n and self.component_matrix[m][n] != 0:
                    communicationWeight += self.mat_norm_components[m][n] * self.mat_norm_units[genome[m]][genome[n]]
        weight = (communicationWeight * (self.vec_trade_off_f[len(self.vec_trade_off_f) - 1])) + resourceWeight


        if not self.solutionValid(genome):
            weight = weight + 100000
        return weight
    # end method fitness_function

    def fitnessFunctionTester(self, genome):
        g, resourceWeight, weight, minPermutation, minWeight = 0,0,0,0, -1


        for d in range(0, len(self.vec_trade_off_f) - 1):
            for k in genome:
                resourceWeight += (self.resource_matrix[d][int(k)][g] * self.vec_trade_off_f[d])
                g += 1
            g = 0

        communicationWeight = 0
        for m in range(0,len(genome)):
            for n in range (m,len(genome)):
                    if genome[m] != genome[n] and self.component_matrix[m][n] != 0:
                        communicationWeight += self.component_matrix[m][n] * self.unit_matrix[genome[m]][genome[n]]

        communicationWeight = (communicationWeight * (self.vec_trade_off_f[len(self.vec_trade_off_f) - 1]))
        weight = communicationWeight + resourceWeight

        return [weight,communicationWeight,resourceWeight]

    def solutionValid(self, genome):
        #resourceDemand = [[0 for i in range(4)] for j in range(3)] # hmm.. why 4 and 3?
        resourceDemand = [[0 for i in range(self.number_of_components)] for j in range(len(self.resource_matrix))]
        sw = 0
        for d in range(0, len(self.vec_trade_off_f) - 1):
            for k in genome:
                resourceDemand[d][k] += self.resource_matrix[d][int(k)][sw]
                sw += 1
            sw = 0

        # check if solution valid - resource constraint
        if all(map(le, list(itertools.chain.from_iterable(resourceDemand)), list(itertools.chain.from_iterable(self.resource_availability)))):
            return True
        else:
            return False

#end class Solver

