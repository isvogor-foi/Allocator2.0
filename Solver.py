__author__ = 'ivan'

import itertools

from operator import le
from abc import ABCMeta, abstractmethod

class Solver:

    @abstractmethod
    def solve(self): pass

    def set_matrices(self, number_of_components, number_of_units, number_of_resources, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, resource_matrix, resource_availability, unit_matrix):
        self.number_of_components = number_of_components
        self.number_of_units = number_of_units
        self.vec_trade_off_f = vec_trade_off_f
        self.mat_norm_components = mat_norm_components
        self.mat_norm_units = mat_norm_units
        self.mat_norm_resources = mat_norm_resources
        self.resource_matrix = resource_matrix
        self.resource_availability = resource_availability
        self.unit_matrix = unit_matrix
        self.number_of_resources = number_of_resources

    def set_architectural_constraints(self, preference_matrix, mandatory_matrix, forbidden_matrix, synergy_matrix):
        self.preference_matrix = preference_matrix
        self.mandatory_matrix = mandatory_matrix
        self.forbidden_matrix = forbidden_matrix
        self.synergy_matrix = synergy_matrix


    def fitness_function(self, result, shorter=True, use_synergy = True):
        resource_weight, communication_weight, weight = 0, 0, 0

        for component, allocated_to in enumerate(result):
            for resource in range(len(self.vec_trade_off_f) - 1):
                #print("res:", resource, "allo: ", allocated_to, "comp: ", component)
                if use_synergy:
                    resource_weight += self.mat_norm_resources[resource][allocated_to][component] * self.vec_trade_off_f[resource]
                else:
                    resource_weight += self.mat_norm_resources[resource][allocated_to][component] \
                                         * self.vec_trade_off_f[resource] \
                                         * self.synergy_matrix[resource][allocated_to][(result.count(allocated_to) - 1)]

        # communication
        for m in range(0, len(result)):
            for n in range(m, len(result)):
                if m != n and self.mat_norm_components[m][n] != 0:
                    communication_weight += self.mat_norm_components[m][n] * self.mat_norm_units[result[m]][result[n]]

        # communication * trade off
        communication_weight = (communication_weight * (self.vec_trade_off_f[len(self.vec_trade_off_f) - 1]))

        if shorter:
            weight = communication_weight + resource_weight
            if not self.is_solution_valid(result):
                weight += 1000000
            return weight, # must return a touple
        else:
            weight = communication_weight + resource_weight
            return [weight, communication_weight, resource_weight]
    # end method fitness_function


    #TODO: update fitness_function when this is done
    #TODO: try simulated annealing scipy.optimize
    def manual_fitness(self, result, verbose = False):
        resource_weight, communication_weight = 0, 0
        resource_weight_2 = 0

        #resources
        for component, allocated_to in enumerate(result):
            for resource in range(len(self.vec_trade_off_f) - 1):
                resource_weight += self.mat_norm_resources[resource][allocated_to][component] * self.vec_trade_off_f[resource]
                #print(self.vec_trade_off_f[resource], "resource: ", resource)
                resource_weight_2 += self.mat_norm_resources[resource][allocated_to][component] \
                                     * self.vec_trade_off_f[resource] \
                                     * self.synergy_matrix[resource][allocated_to][(result.count(allocated_to) - 1)]

                # print (round(self.mat_norm_resources[resource][allocated_to][component], 4), " * ", \
                #     round(self.vec_trade_off_f[resource], 4), " * ", \
                #     self.synergy_matrix[resource][allocated_to][result.count(allocated_to) - 1],"\t", allocated_to, "\t| hosts ", result.count(allocated_to), " -> resource: ", resource, ", allocated to: ", allocated_to)

        # communication
        for m in range(0, len(result)):
            for n in range (m, len(result)):
                if m != n and self.mat_norm_components[m][n] != 0:
                    communication_weight += self.mat_norm_components[m][n] * self.mat_norm_units[result[m]][result[n]]

        # communication * trade off
        communication_weight = (communication_weight * (self.vec_trade_off_f[len(self.vec_trade_off_f) - 1]))
        if verbose:
            print("res: ", resource_weight, ", comm: ", communication_weight, " = ", resource_weight + communication_weight, " -> res2: ", resource_weight_2)

        return [resource_weight, communication_weight, resource_weight_2]

    #end manual fitness

    def is_solution_valid(self, solution, verbose=False):
        result = False

        number_of_resources = len(self.vec_trade_off_f) - 1
        resource_demand = [[0 for col in range(self.number_of_units)] for row in range(number_of_resources)]

        for component, allocated_to in enumerate(solution):
            for resource in range(number_of_resources):
                resource_demand[resource][allocated_to] += self.resource_matrix[resource][allocated_to][component]

        if verbose:
            print ("\n Resource demand: ", resource_demand)
            print (" Resource availability: ", self.resource_availability)

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
            print ("Preference valid: ", preference_valid)
            print ("Mandatory valid: ", mandatory_valid)
            print ("Forbidden valid: ", forbidden_valid)

        return preference_valid and mandatory_valid and forbidden_valid

    def is_preference_valid(self, solution, verbose=False):
        preference_sum = 0
        for component, allocated_to in enumerate(solution):
            preference_sum += self.preference_matrix[allocated_to][component]

        if verbose:
            print ("Preference sum: ", (preference_sum == 0))

        return preference_sum == 0
    # end is_preference_valid

    def is_mandatory_valid(self, solution, verbose=False):
        mandatory_sum = 0
        components = range(0, self.number_of_components, 1)

        for combination in itertools.combinations(components, 2):
            #print("Mandatory: ", self.mandatory_matrix[combination[0]][combination[1]])
            if not(not(self.mandatory_matrix[combination[0]][combination[1]]) or solution[combination[0]] == solution[combination[1]]):
                mandatory_sum += 1

        if verbose:
            print ("Mandatory sum: ", (mandatory_sum == 0))

        return mandatory_sum == 0
    #end is_mandatory_valid

    def is_forbidden_valid(self, solution, verbose=False):
        forbidden_sum = 0
        components = range(0, self.number_of_components, 1)

        for combination in itertools.combinations(components, 2):
            forbidden_sum += (self.forbidden_matrix[combination[0]][combination[1]] and (solution[combination[0]] == solution[combination[1]]))

        if verbose:
            print ("Forbidden sum: ", (forbidden_sum == 0))
        return forbidden_sum == 0

    # check if mandatory_matrix and forbidden_matrix are consistent
    def mandatory_forbidden_consistency_check(self):
        invalid = 0
        for i in range(0, self.number_of_components, 1):
            for j in range (0, self.number_of_components, 1):
                if self.mandatory_matrix[i][j] == 1 and self.forbidden_matrix[i][j] != 0:
                    invalid += 1
        return invalid == 0

    def print_results(self, solution):
        print("************************", solution["method"], "************************")
        print(solution["result"])
        print("Time: ", solution["time"])
        print("Architectural validity: ", self.is_architectural_valid(solution["result"], False))
        print("Vector: ", self.vec_trade_off_f)
        print("Fitness: ")
        self.manual_fitness(solution["result"])

    def print_results_for_file(self, solution):
        # output format:
        # method; nComponents ; nUnits ; nResources ; resPerformance ; commPerformance ; overall ; time ; solution
        #
        result = solution["method"] + ";"
        result += str(self.number_of_components) + ";" + str(self.number_of_units) + ";" + str(self.number_of_resources)
        allocation_performance = self.manual_fitness(solution["result"])
        result += ";" + str(allocation_performance[2])+ ";" + str(allocation_performance[1])
        result += ";" + str(allocation_performance[0]) + ";" + str(allocation_performance[2] + allocation_performance[1])
        result += ";" + str(solution["time"])
        result += ";" + str(solution["result"].tolist())
        print(result)

#end class Solver

