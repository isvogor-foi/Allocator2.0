__author__ = 'ivan'


class PlatformInitializer:

    '''
        initialize - used to setup the input matrices, currently has mock data
    '''
    def initialize(self, num_components, num_platforms, min_weight, max_weight, verbose = False):
        self.verbose = verbose;

        if verbose:
            print("Matrix initialization - TiWO Scenario 2...")

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
                                [1.78,26.91,42.31,31.74,52.8,3.32,37.55,67.07,4.04,80.43,185.63],
                                [0.32,8.49,14.41,13.67,17.43,1.16,14.38,16.87,1.49,18.22,6.24],
                                [124.19,0,0,0,0,125.47,0,0,124.62,0,0]],
                                [ #2 depth - power
                                [2.9639,5.4504,3.8794,3.9846,7.249,3.1493,4.4101,8.2373,3.3966,9.1231,7.993533333],
                                [4.6727,6.483,5.5632,6.7314,9.4641,6.0381,9.6826,9.9184,6.2688,11.4692,17.30156667],
                                [2.4345,0,0,0,0,2.4352,0,0,2.4383,0,0]]]

        # no limitations in resources
        self.resource_availabilty_matrix = [[500, 500, 500],
                                    [500, 500, 500]]

        self.trade_off_vector_f =  [10,1] # append

        self.pairwise_matrix = [[1, 0.5, 9],
                               [2, 1, 9],
                               [0.1111, 0.1111, 1]]

        self.bandwith_matrix = [[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]]

        # 1 if must not be allocated to

        self.preference_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1]]

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
                          [1, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 1, 1],
                          [1, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 1, 1],
                          [1, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 1, 1]],
                        [ #2 depth - energy
                          [1, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 1, 1],
                          [1, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 1, 1],
                          [1, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 1, 1]]]

        if verbose:
            print("Matrix initialization done!")
    # end method initialize
# end class ComponentInitializer