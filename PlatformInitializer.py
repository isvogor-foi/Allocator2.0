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

    # Component matrix
        print(self.num_platforms, self.num_components)
        self.component_matrix = self.generate_random_matrix_with_more_zeros(self.num_components, 0, 10)
        print("Component matrix:\n" + str(self.component_matrix))

    # Platform matrix
        self.platform_matrix = self.generate_random_matrx(self.num_platforms, 0, 10, diagonal = 1)
        print("Platform matrix:\n" + str(self.platform_matrix))

    #resource matrix
        #maybe generate each depth level with different order of magnitude?
        self.resource_matrix = np.random.random_integers(0, 100, size=(self.num_of_resources, self.num_platforms, self.num_components))
        print("Resource matrix: \n", self.resource_matrix)

        # generating with diferent orders of magnitude
        #self.resource_matrix = []
        #for i in range(0, self.num_of_resources):
        #    self.resource_matrix.append(np.random.random_integers(0, 10 * (i + 1), size=(4, 11)))
        #print(self.resource_matrix)

        # sum first row...
        # print(sum(self.resource_matrix[0,0]))

    # resource availability matrix
        self.resource_availabilty_matrix = np.empty([3, self.num_platforms], dtype=(int))

        # make the size less than the sum of all resources!
        # 70% of the sum, just so you cannot place all on one?
        for i in range(0, self.num_of_resources):
            for j in range (0, self.num_platforms):
                self.resource_availabilty_matrix[i,j] = int(sum(self.resource_matrix[i, j] * 0.7))
        print("Resource availability \n", self.resource_availabilty_matrix)

    # vector
        self.trade_off_vector_f =  [10,1] # append

    # TODO: Something is wrong with this matrix (negative results)
    # pairwise matrix (+1 for communication)
        self.pairwise_matrix = self.get_pairwise_submatix(self.num_of_resources + 1)

        # self.pairwise_matrix = [[1, 0.5, 9],
        #                [2, 1, 9],
        #                [0.1111, 0.1111, 1]]

        print("Pairwise matrix: \n", self.pairwise_matrix)


    # bandwith matrix
        self.bandwith_matrix = self.generate_random_matrx(self.num_platforms, 500, 500, 1)
        print("Bandwith matrix: \n", self.bandwith_matrix)

    # preference matrix
        # 1 if must not be allocated to
        self.preference_matrix = self.generate_random_matrix_with_more_zeros(self.num_components, 0, 2, 0.2)[:num_platforms,:num_components]
        print("Preference matrix: \n", self.preference_matrix)

    # mandatory matrix
        # 1 if must be together
        self.mandatory_matrix = self.generate_random_matrix_with_more_zeros(self.num_components,0,2)
        print("Mandatory matrix: \n", self.mandatory_matrix)

    # forbidden matrix
        # fix mandatory & forbidden matrix so they don't contradict
        self.forbidden_matrix = self.check_logic_consistency(self.generate_random_matrix_with_more_zeros(self.num_components,0,2), self.mandatory_matrix)
        print("Forbidden matrix: \n", self.forbidden_matrix)

    # synergy matrix
        self.synergy_matrix = self.generate_synergy_matrix()
        print("Synergy matrix: \n", self.synergy_matrix)

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

    def get_pairwise_submatix(self, size):
        # predefined using http://bpmsg.com/academic/ahp_calc.php?n=10&t=AHP+priorities&c[0]=1&c[1]=2&c[2]=3&c[3]=4&c[4]=5&c[5]=6&c[6]=7&c[7]=8&c[8]=9&c[9]=10
        # CI = 0.73
        pairwise_matrix = [[1,1.00,2.00,4.00,1.00,6.00,4.00,6.00,5.00,9.00],
                           [1.00,1,2.00,4.00,2.00,6.00,4.00,4.00,4.00,9.00],
                           [0.50,0.50,1,2.00,2.00,2.00,4.00,5.00,7.00,4.00],
                           [0.25,0.25,0.50,1,1.00,2.00,1.00,7.00,3.00,9.00],
                           [1.00,0.50,0.50,1.00,1,2.00,1.00,7.00,8.00,6.00],
                           [0.17,0.17,0.50,0.50,0.50,1,1.00,2.00,5.00,4.00],
                           [0.25,0.25,0.25,1.00,1.00,1.00,1,5.00,6.00,7.00],
                           [0.17,0.25,0.20,0.14,0.14,0.50,0.20,1,2.00,3.00],
                           [0.20,0.25,0.14,0.33,0.12,0.20,0.17,0.50,1,3.00],
                           [0.11,0.11,0.25,0.11,0.17,0.25,0.14,0.33,0.33,1]]
        pairwise_matrix = np.array(pairwise_matrix)
        return pairwise_matrix[:size, :size]

    def check_logic_consistency(self, fmatrix, smatrix):
        for i in range(0, len(smatrix)):
            for j in range(0, len(fmatrix)):
                if fmatrix[i,j] == smatrix[i,j] == 1:
                    fmatrix[i,j] = not smatrix[i,j]
        return fmatrix

    def generate_synergy_matrix(self):

        first_line = []
        for i in range(0, self.num_components):
            if i == 0:
                first_line.append(1)
            else:
                first_line.append( 0.15 * i)

        synergy_matrix = []
        for j in range (0, self.num_of_resources):
            resource_mx = []
            for i in range(0, self.num_platforms):
                resource_mx.append(first_line)
            synergy_matrix.append(resource_mx)

        return np.array(synergy_matrix)


# end class ComponentInitializer