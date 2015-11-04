__author__ = 'ivan'

import numpy as np

class PlatformInitializer:

    '''
        initialize - used to setup the input matrices, currently has mock data
    '''
    def initialize(self, num_platforms, num_components, min_weight, max_weight, verbose = False):
        self.verbose = verbose;

        if verbose:
            print ("Starting matrix initialization...")

        self.num_components = num_components
        self.num_platforms = num_platforms
        self.num_of_resources = 3

        print(self.num_platforms, self.num_components)
        self.component_matrix = self.generate_random_matrix_with_more_zeros(11, 0, 10)
        print("Component matrix:\n" + str(self.component_matrix))

        self.platform_matrix = self.generate_random_matrx(4, 0, 10, diagonal = 1)
        print("Component matrix:\n" + str(self.platform_matrix))

        #maybe generate each depth level with different order of magnitude?
        self.resource_matrix = np.random.random_integers(0, 100, size=(self.num_of_resources, self.num_platforms, self.num_components))
        print(self.resource_matrix)

        # generating with diferent orders of magnitude
        #self.resource_matrix = []
        #for i in range(0, self.num_of_resources):
        #    self.resource_matrix.append(np.random.random_integers(0, 10 * (i + 1), size=(4, 11)))
        #print(self.resource_matrix)

        # sum first row...
        # print(sum(self.resource_matrix[0,0]))

        self.resource_availabilty_matrix = np.empty([3, self.num_platforms], dtype=(int))

        # make the size less than the sum of all resources!
        # 70% of the sum, just so you cannot place all on one?
        for i in range(0, self.num_of_resources):
            for j in range (0, self.num_platforms):
                self.resource_availabilty_matrix[i,j] = int(sum(self.resource_matrix[i, j] * 0.7))
        print("Matrix \n", self.resource_availabilty_matrix)

        # HERE!
        self.trade_off_vector_f =  [10,1] # append

        self.pairwise_matrix = [[1, 3, 0.1429, 3],
                               [0.3333,1,0.1111,3],
                               [7,9,1,9],
                               [0.3333,0.3333,0.1111,1]]

        self.bandwith_matrix = [ [1, 50, 50, 50],
                                [50, 1, 50, 50],
                                [50, 50, 1, 50],
                                [50, 50, 50, 1]]

        # 1 if must not be allocated to

        self.preference_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]]

        # 1 if must be together

        self.mandatory_matrix = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # 1 if must be separated

        self.forbidden_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.synergy_matrix = [[ #0 depth - execution time
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2]],
                                [ #1 depth - memory
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2]],
                                [ #2 depth - energy
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2],
                                  [1, 0.2, 0.3, 0.4, 0.5, 0.9, 1, 1.1, 1.2, 1.5, 2]]]

        if verbose:
            print("Matrix initialization done!")
    # end method initialize

    def generate_random_matrx(self, size, min, max, diagonal = 0):
        matrix = np.random.random_integers(min, max, size=(size, size))
        # diagonalize...
        np.fill_diagonal(matrix, diagonal)
        result = ((matrix + matrix.T) / 2).astype(int)
        np.fill_diagonal(matrix, diagonal)

        return result

    def generate_random_matrix_with_more_zeros(self, size, min, max, ratio = 0.5, diagonal = 0):
        prob = [(1 - ratio)/(size - 1) for i in range(0, size)]
        prob[0] = ratio
        # we want nonlinear distribution
        # with less connectivity between components which
        matrix = np.random.choice(size, size=(size, size), p = prob)

        # since size must be = to len(p) randomize from min to max
        for x in np.nditer(matrix, op_flags=['readwrite']):
            if x > 0:
                x[...] = np.random.randint(min, max, 1)

        # diagonalize...
        np.fill_diagonal(matrix, diagonal)
        result = ((matrix + matrix.T) / 2).astype(int)
        np.fill_diagonal(matrix, diagonal)

        return result

# end class ComponentInitializer