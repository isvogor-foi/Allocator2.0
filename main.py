__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Allocator as alloc
from random import randint

if __name__ == '__main__':
    #local vars


    allocator = alloc.Allocator()
    counter = 0
    for nComponents in range(5, 15):
        for nUnits in range(3, 6):
            nResources = randint(3, 5)
            counter += 1
            allocator.solve_by_ga(pinit, calculator, nComponents, nUnits, nResources, counter)
            allocator.solve_by_sa(pinit, calculator, nComponents, nUnits, nResources, counter)
            allocator.solve_by_fss(pinit, calculator, nComponents, nUnits, nResources, counter)


    # nComponents = 11
    # nUnits = 3
    # nResources = 3
    #
    # #initialize input
    # initializer = pinit.PlatformInitializer()
    # initializer.initialize(nUnits, nComponents, nResources, 1, 9, False)
    #
    # #normalize input matrices
    # calc = calculator.Calculator()
    # mat_norm_components = calc.normalize(initializer.component_matrix)
    # mat_norm_resources = calc.normalize(initializer.resource_matrix)
    # mat_norm_units = calc.normalize(initializer.platform_matrix)
    #
    # #get the rest of the matrices
    # mat_resource_availability = initializer.resource_availabilty_matrix
    # mat_pairwise_comparison = initializer.pairwise_matrix
    # mat_bandwidth = initializer.bandwith_matrix
    #
    # #calculate the eignenvector
    # vec_trade_off_f = calc.eigenvector(initializer.pairwise_matrix, True)
    # print("Consistency ratio:", calc.calculateConsistency(initializer.pairwise_matrix))
    #
    # solver = ga.GASolver()
    #
    # solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    # solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)
    #
    # result = solver.solve()
    # solver.print_results(result)

    # solver = sa.SASolver([0]*11)
    #
    # solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    # solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)
    #
    # result = solver.solve()
    # solver.print_results(result)
    #
    # solver = fs.FSSolver()
    #
    # solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    # solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)
    #
    # result = solver.solve()
    # solver.print_results(result)

