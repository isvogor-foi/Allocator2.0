__author__ = 'Ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Solver as slv

if __name__ == '__main__':

    verbose = True

    #local vars
    nComponents = 11
    nUnits = 3

    #initialize input
    initializer = pinit.ComponentInitializer()
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
    vec_trade_off_f = calc.eigenvector(initializer.pairwise_matrix, True)

    solver = slv.Solver(nComponents, nUnits, vec_trade_off_f, initializer.component_matrix, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    result = solver.solve_by_genetic_algorithm(True, True)

    # print result
    print "****************** R E S U L T ********************"
    print "Method: ", result["method"]
    print "Result: ", result["result"]
    print "Score: - final:", result["score"][0], ", communication ", result["score"][1], ", res ", result["score"][2]
    print "Skipping all on one: ", result["type"]
    print "Runtime: ", result["time"]
    print "Solution space: ", nUnits, "^", nComponents, " = ", pow(nUnits, nComponents)
    print "***************************************************"



