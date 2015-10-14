__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import SASolver as sa
import GASolver as ga
import Solver

if __name__ == '__main__':
    #local vars
    nComponents = 11
    nUnits = 4

    #initialize input
    initializer = pinit.PlatformInitializer()
    initializer.initialize(nUnits, nComponents, 1, 9)

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
    vec_trade_off_f = calc.eigenvector(initializer.pairwise_matrix)

    solver = ga.GASolver()

    solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)
    result = solver.solve()

    print(result["result"])

    solver = sa.SASolver([0]*11)

    solver.set_matrices(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)

    something1, something2 = solver.anneal()
    print(something1,"", something2)