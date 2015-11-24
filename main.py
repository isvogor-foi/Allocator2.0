__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import SASolver as sa
import GASolver as ga
import FSSolver as fs

if __name__ == '__main__':
    #local vars
    nComponents = 11
    nUnits = 3

    #initialize input
    initializer = pinit.PlatformInitializer()
    initializer.initialize(nUnits, nComponents, 1, 9, True)

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
    vec_trade_off_f = calc.eigenvector(initializer.pairwise_matrix, True)
    print("Consistency ratio:", calc.calculateConsistency(initializer.pairwise_matrix))


    solver = ga.GASolver()

    solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)

    result = solver.solve()
    solver.print_results(result)

    solver = sa.SASolver([0]*11)

    solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)

    result = solver.solve()
    solver.print_results(result)

    solver = fs.FSSolver()

    solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)

    result = solver.solve()
    solver.print_results(result)

    print("****************************************************************")
    manual_scenario_1 = [2, 0, 2, 2, 0, 0, 1, 0, 1, 1, 1]
    manual_scenario_2 = [2, 1, 1, 0, 1, 2, 0, 1, 2, 1, 1]

    print("Manual - Scenario 1")
    solver.manual_fitness(manual_scenario_1)

    print("Manual - Scenario 2")
    solver.manual_fitness(manual_scenario_2)
