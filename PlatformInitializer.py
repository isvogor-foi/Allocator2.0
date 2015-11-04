__author__ = 'ivan'

import numpy as np

class PlatformInitializer:

    '''
        initialize - used to setup the input matrices, currently has mock data
    '''
    def initialize(self, num_components, num_platforms, min_weight, max_weight, verbose = False):
        self.verbose = verbose;

        if verbose:
            print ("Starting matrix initialization...")


        self.num_components = num_components
        self.num_platforms = num_platforms

        self.component_matrix = self.generate_random_matrix_with_more_zeros(11, 0, 10)
        print("Component matrix:\n" + str(self.component_matrix))

        self.platform_matrix = self.generate_random_matrx(4, 0, 10, diagonal = 1)
        print("Component matrix:\n" + str(self.platform_matrix))

        self.platform_matrix = [[1,5,5,4],
                               [5,1,2,3],
                               [5,2,1,3],
                               [4,3,3,1]]


        self.resource_matrix =  [[ #0 depth - execution time
                                  [10,50,30,10,20,20,90,20,20,20,90],
                                  [90,20,20,40,40,50,20,10,10,15,10],
                                  [90,20,20,40,40,50,20,10,10,15,10],
                                  [55,72,72,72,72,55,15,70,70,70,33]],
                                [ #1 depth - memory
                                  [48,128,64,48,64,64,168,148,48,48,168],
                                  [256,256,256,168,168,168,128,96,32,32,64],
                                  [256,256,256,168,168,168,128,96,32,32,64],
                                  [128,148,148,148,148,64,64,148,148,148,96]],
                                [ #2 depth - energy
                                  [2,10,6,2,4,4,18,4,4,4,18],
                                  [18,4,4,8,8,10,4,2,2,3,2],
                                  [18,4,4,8,8,10,4,2,2,3,2],
                                  [11,14,14,14,14,11,3,14,14,14,7]]]

        self.resource_availabilty_matrix = [[100,150,150,100],
                                    [256,640,640,256],
                                    [50,25,25,15]]

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