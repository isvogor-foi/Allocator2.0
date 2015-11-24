__author__ = 'Ivan'

import GASolver as ga

class Allocator:
    def solve_by_ga(self, pinit, calculator, nComponents, nUnits, nResources):

        initializer = pinit.PlatformInitializer()
        initializer.initialize(nUnits, nComponents, nResources, 1, 9, False)

        #normalize input matrices
        calc = calculator.Calculator()
        mat_norm_components = calc.normalize(initializer.component_matrix)
        mat_norm_resources = calc.normalize(initializer.resource_matrix)
        mat_norm_units = calc.normalize(initializer.platform_matrix)

        #get the rest of the matrices
        mat_resource_availability = initializer.resource_availabilty_matrix
        mat_pairwise_comparison = initializer.pairwise_matrix
        mat_bandwidth = initializer.bandwith_matrix

        #calculate the eignenvector
        vec_trade_off_f = calc.eigenvector(initializer.pairwise_matrix, False)

        solver = ga.GASolver()

        solver.set_matrices(nComponents, nUnits, nResources, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
        solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)

        result = solver.solve()
        #print("Consistency ratio:", calc.calculateConsistency(initializer.pairwise_matrix))
        #solver.print_results(result)
        solver.print_results_for_file(result)