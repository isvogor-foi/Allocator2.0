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

    # architectural constraints
    @property
    def preference_matrix(self): return self
    @property
    def mandatory_matrix(self): return self
    @property
    def forbidden_matrix(self): return self

    # synergy effect matrix
    @property
    def synergy_matrix(self): return self

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

    def set_architectural_constraints(self, preference_matrix, mandatory_matrix, forbidden_matrix, synergy_matrix):
        self.preference_matrix = preference_matrix
        self.mandatory_matrix = mandatory_matrix
        self.forbidden_matrix = forbidden_matrix
        self.synergy_matrix = synergy_matrix

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
    #end manual fitness

    def is_solution_valid(self, solution, verbose=False):
        result = False

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
            result = True
        else:
            result = False

        return result and self.is_architectural_valid(solution)
    #end is_solution_valid

    def is_architectural_valid(self, solution, verbose=False):
        preference_valid = self.is_preference_valid(solution)
        mandatory_valid = self.is_mandatory_valid(solution)
        forbidden_valid = self.is_forbidden_valid(solution)

        if verbose:
            print "Preference valid: ", preference_valid
            print "Mandatory valid: ", mandatory_valid
            print "Forbidden valid: ", forbidden_valid

        return preference_valid and mandatory_valid and forbidden_valid

    def is_preference_valid(self, solution, verbose=False):
        preference_sum = 0
        for component, allocated_to in enumerate(solution):
            preference_sum += self.preference_matrix[allocated_to][component]

        if verbose:
            print "Preference sum: ", (preference_sum == 0)

        return preference_sum == 0
    # end is_preference_valid

    def is_mandatory_valid(self, solution, verbose=False):
        mandatory_sum = 0
        components = range(0, self.number_of_components, 1)

        for combination in itertools.combinations(components, 2):
            #print (not(self.mandatory_matrix[combination[0]][combination[1]]) or solution[combination[0]] == solution[combination[1]]), " - ", self.mandatory_matrix[combination[0]][combination[1]] and solution[combination[0]] != solution[combination[1]]
            #print self.mandatory_matrix[combination[0]][combination[1]] and solution[combination[0]] != solution[combination[1]]
            if not(not(self.mandatory_matrix[combination[0]][combination[1]]) or solution[combination[0]] == solution[combination[1]]):
                mandatory_sum += 1

        if verbose:
            print "Mandatory sum: ", (mandatory_sum == 0)

        return mandatory_sum == 0
    #end is_mandatory_valid

    def is_forbidden_valid(self, solution, verbose=False):
        forbidden_sum = 0
        components = range(0, self.number_of_components, 1)

        for combination in itertools.combinations(components, 2):
            #print combination, "->\t mat: ", self.forbidden_matrix[combination[0]][combination[1]], \
            #    "tog: ", (solution[combination[0]] == solution[combination[1]]), "->\t", \
            #    (self.forbidden_matrix[combination[0]][combination[1]] and (solution[combination[0]] == solution[combination[1]]))
            forbidden_sum += (self.forbidden_matrix[combination[0]][combination[1]] and (solution[combination[0]] == solution[combination[1]]))

        if verbose:
            print "Forbidden sum: ", (forbidden_sum == 0)
        return forbidden_sum == 0

    # check if mandatory_matrix and forbidden_matrix are consistent
    def mandatory_forbidden_consistency_check(self):
        invalid = 0
        for i in range(0, self.number_of_components, 1):
            for j in range (0, self.number_of_components, 1):
                if self.mandatory_matrix[i][j] == 1 and self.forbidden_matrix[i][j] != 0:
                    invalid += 1
        return invalid == 0
#end class Solver

