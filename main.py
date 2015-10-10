__author__ = 'Ivan'

import PlatformInitializer as pinit
import Calculator as calculator

if __name__ == '__main__':

    verbose = True

    #local vars
    nComponents = 10
    nUnits = 3

    #initialize input
    initializer = pinit.ComponentInitializer()
    initializer.initialize(nUnits, nComponents, 1, 9)

    #normalize input matrices
    calc = calculator.Calculator()
    mat_norm_components = calc.normalize(initializer.component_matrix, True)
    mat_norm_resources = calc.normalize(initializer.resource_matrix, True)
    mat_norm_units = calc.normalize(initializer.platform_matrix, True)

    #get the rest of the matrices
    mat_resource_availability = initializer.resource_availabilty_matrix
    mat_pairwise_comparison = initializer.pairwise_matrix
    mat_bandwidth = initializer.bandwith_matrix

    #calculate the eignenvector
    e = calc.eigenvector(initializer.pairwise_matrix)



