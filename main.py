__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Solver as slv

if __name__ == '__main__':

    verbose = True

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

    solver = slv.Solver(nComponents, nUnits, vec_trade_off_f, mat_norm_components, mat_norm_resources, mat_norm_units, initializer.resource_matrix, mat_resource_availability, initializer.platform_matrix)
    solver.set_architectural_constraints(initializer.preference_matrix, initializer.mandatory_matrix, initializer.forbidden_matrix, initializer.synergy_matrix)

    results = []
    for i in range(0, 5):
        result = solver.solve_by_genetic_algorithm()
        results.append([result["result"], result["time"]])
        print("- %s -", i)
    #result = solver.solve_by_genetic_algorithm(True, True)

    f = open('results_deap.txt','w')
    for r in results:
        string = str(r[0]) + ", " + str(r[1]) + ", " + str(result["score"][0]) + "\n"
        f.write(string) # python will convert \n to os.linesep
    f.close()

    #solver.manual_fitness(result["result"])

    mock_solution_good = [0, 2, 2, 0, 0, 0, 3, 1, 1, 2, 1]
    mock_solution_bad = [3, 2, 2, 0, 0, 0, 3, 1, 1, 1, 1]

    solver.manual_fitness(result["result"])

    # print result
    print ("****************** R E S U L T ********************")
    print ("Method: ", result["method"])
    print ("Result: ", result["result"])
    print ("Score: ", result["score"][0], ", communication ", result["score"][1], ", res ", result["score"][2])
    print ("Skipping all on one: ", result["type"])
    print ("Runtime: ", result["time"])
    print ("Solution space: ", nUnits, "^", nComponents, " = ", pow(nUnits, nComponents))
    print ("----------- VALIDITY ----------")
    print ("Solution valid: ", solver.is_solution_valid(result["result"]))
    print ("Architectural validity\n", solver.is_architectural_valid(result["result"], True))
    print ("Mandatory - forbidden consistency: ", solver.mandatory_forbidden_consistency_check())
    print ("***************************************************")

    #1.15539650222
    #2.13983685843
    #0.29119198373
    #****************** R E S U L T ********************
    #Method:  Genetic Algorithm
    #Result:  array('b', [0, 1, 0, 0, 1, 0, 3, 1, 1, 2, 1])