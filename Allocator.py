__author__ = 'Ivan'

import SASolver as sa
import GASolver as ga
import FSSolver as fs
import RASolver as ra;

class Allocator:

    def init(self, pinit, calculator, nComponents, nUnits, nResources):
        self.initializer = pinit.PlatformInitializer()
        self.initializer.initialize(nUnits, nComponents, nResources, 1, 9, False, True)

        calc = calculator.Calculator()
        self.mat_norm_components = calc.normalize(self.initializer.component_matrix)
        self.mat_norm_resources = calc.normalize(self.initializer.resource_matrix)
        self.mat_norm_units = calc.normalize(self.initializer.platform_matrix)

        #get the rest of the matrices
        self.mat_resource_availability = self.initializer.resource_availabilty_matrix
        #mat_pairwise_comparison = self.initializer.pairwise_matrix
        #mat_bandwidth = self.initializer.bandwith_matrix

        #calculate the eignenvector
        self.vec_trade_off_f = calc.eigenvector(self.initializer.pairwise_matrix, False)

    def solve_by_ga(self, nComponents, nUnits, nResources, filename, i):
        #normalize input matrices
        solver = ga.GASolver()
        solver.set_matrices(nComponents, nUnits, nResources, self.vec_trade_off_f, self.mat_norm_components, self.mat_norm_resources,
                            self.mat_norm_units, self.initializer.resource_matrix, self.mat_resource_availability,
                            self.initializer.platform_matrix)
        solver.set_architectural_constraints(self.initializer.preference_matrix, self.initializer.mandatory_matrix,
                                             self.initializer.forbidden_matrix, self.initializer.synergy_matrix)

        result = solver.solve()

        #print("Consistency ratio:", calc.calculateConsistency(initializer.pairwise_matrix))
        #solver.print_results(result)

        solver.print_results_for_file(result, filename, i)
        return solver.is_solution_valid(result["result"], False)

    def solve_by_sa(self, nComponents, nUnits, nResources, filename, i):
        solver = sa.SASolver([0] * nComponents)

        solver.set_matrices(nComponents, nUnits, nResources, self.vec_trade_off_f, self.mat_norm_components, self.mat_norm_resources,
                            self.mat_norm_units, self.initializer.resource_matrix, self.mat_resource_availability,
                            self.initializer.platform_matrix)
        solver.set_architectural_constraints(self.initializer.preference_matrix, self.initializer.mandatory_matrix,
                                             self.initializer.forbidden_matrix, self.initializer.synergy_matrix)

        result = solver.solve()

        solver.print_results_for_file(result, filename, i)
        return solver.is_solution_valid(result["result"], False)


    def solve_by_fss(self, nComponents, nUnits, nResources, filename, i):
        solver = fs.FSSolver()

        solver.set_matrices(nComponents, nUnits, nResources, self.vec_trade_off_f, self.mat_norm_components, self.mat_norm_resources,
                            self.mat_norm_units, self.initializer.resource_matrix, self.mat_resource_availability,
                            self.initializer.platform_matrix)
        solver.set_architectural_constraints(self.initializer.preference_matrix, self.initializer.mandatory_matrix,
                                             self.initializer.forbidden_matrix, self.initializer.synergy_matrix)

        result = solver.solve()

        solver.print_results_for_file(result, filename, i)
        return solver.is_solution_valid(result["result"], False)

    def solve_by_random(self, nComponents, nUnits, nResources, filename, i):
        solver = ra.RASolver()

        solver.set_matrices(nComponents, nUnits, nResources, self.vec_trade_off_f, self.mat_norm_components, self.mat_norm_resources,
                            self.mat_norm_units, self.initializer.resource_matrix, self.mat_resource_availability,
                            self.initializer.platform_matrix)
        solver.set_architectural_constraints(self.initializer.preference_matrix, self.initializer.mandatory_matrix,
                                             self.initializer.forbidden_matrix, self.initializer.synergy_matrix)

        result = solver.solve()

        solver.print_results_for_file(result, filename, i)
        return solver.is_solution_valid(result["result"], False)
