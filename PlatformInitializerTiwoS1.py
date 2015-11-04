__author__ = 'ivan'


class PlatformInitializer:

    '''
        initialize - used to setup the input matrices, currently has mock data
    '''
    def initialize(self, num_components, num_platforms, min_weight, max_weight, verbose = False):
        self.verbose = verbose;

        if verbose:
            print("Matrix initialization - TiWO Scenario 1...")

        self.num_components = num_components
        self.num_platforms = num_platforms


        ## TODO: Define this part...
        self.component_matrix = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

        self.platform_matrix = [[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]]


        #limitations
        self.resource_matrix = [[ #0 depth - execution time
                                [1.78,4.29,2.29,3.11,10.29,37.55,76.24,50.04,80.43,22.22,185.63],
                                [0.32,1.28,0.6,0.83,5,14.38,19.39,15.12,18.22,5.706666667,6.24],
                                [124.19,0,124.42,125.1,0,0,0,0,0,0,0]],
                                [ #2 depth - power
                                  [2.9639,3.3125,2.9009,3.0382,3.5405,4.4101,9.2339,7.6358,9.1231,2.602533333,7.993533333],
                                  [4.6727,5.4307,4.7375,5.8686,5.9074,9.6826,10.6593,9.9566,11.4692,4.2473,17.30156667],
                                  [2.4345,0,2.4395,2.4348,0,0,0,0,0,0,0]]]

        # no limitations in resources
        self.resource_availabilty_matrix = [[500, 500, 500],
                                    [500, 500, 500]]

        self.trade_off_vector_f =  [10,1] # append

        self.pairwise_matrix = [[1, 3, 0.1429],
                               [0.3333,1,0.1111],
                               [7,9,1,]]

        self.bandwith_matrix = [[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]]

        # 1 if must not be allocated to

        self.preference_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]]

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
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.synergy_matrix = [[ #0 depth - execution time
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                                [ #2 depth - energy
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]

        if verbose:
            print("Matrix initialization done!")
    # end method initialize
# end class ComponentInitializer