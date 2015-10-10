__author__ = 'Ivan'


class ComponentInitializer:

    @property
    def componentMatrix(self): return self
    @property
    def platformMatrix(self): return self
    @property
    def resourceMatrix(self): return self
    @property
    def numberOfComponents(self): return self
    @property
    def numberOfPlatforms(self): return self
    @property
    def qu(self): return self
    @property
    def tradeOffMatrixF(self): return self
    @property
    def resourceAvailabilty(self): return self
    @property
    def verbose(self): return self

    '''
    initialize - used to setup the input matrices
    '''
    def initialize(self, numberOfComponents, numberOfPlatforms, minWeight, maxWeight, verbose = False):
        self.verbose = verbose;

        if verbose:
            print "Starting matrix initialization..."

        self.numberOfPlatforms = numberOfPlatforms
        self.numberOfComponents = numberOfComponents

        self.componentMatrix = [[0,1,0,0,0,0,0,0,0,0,0],
                                [1,0,5,0,3,0,0,0,0,0,0],
                                [0,5,0,5,3,0,0,0,0,0,0],
                                [0,0,5,0,0,1,3,7,0,0,0],
                                [0,3,3,0,0,9,9,3,0,0,0],
                                [0,0,0,1,9,0,0,0,7,7,0],
                                [0,0,0,3,9,0,0,0,0,0,7],
                                [0,0,0,7,3,0,0,0,0,0,0],
                                [0,0,0,0,0,7,0,0,0,0,0],
                                [0,0,0,0,0,7,0,0,0,0,0],
                                [0,0,0,0,0,0,7,0,0,0,0]]

        self.platformMatrix = [[1,5,5,4],
                               [5,1,2,3],
                               [5,2,1,3],
                               [4,3,3,1]]


        self.resourceMatrix =  [[ #0 depth - execution time
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

        self.resourceAvailabilty = [[100,150,150,100],
                                    [256,640,640,256],
                                    [50,25,25,15]]

        ##self.tradeOffMatrixF =  [10,1] # append

        self.pairwiseMatrix = [[1, 3, 0.1429, 3],
                               [0.3333,1,0.1111,3],
                               [7,9,1,9],
                               [0.3333,0.3333,0.1111,1]]

        self.bandwithMatrix = [ [1, 50, 50, 50],
                                [50, 1, 50, 50],
                                [50, 50, 1, 50],
                                [50, 50, 50, 1]]

        if verbose:
            print "Matrix initialization done!"
    # end method initialize
# end class ComponentInitializer