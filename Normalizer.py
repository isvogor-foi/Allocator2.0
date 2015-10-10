__author__ = 'Ivan'

import numpy as np

class Normalizer:

    def normalize(self, matrix, verbose = False):
        temp = np.array(matrix)
        res = []

        # if more than 3 dimensions, use dimension max
        if(temp.ndim >= 3):
            for depth in temp:
                res.append((depth / (depth.max() * 1.0)).tolist())
        else:
            res.append((temp / (temp.max() * 1.0)).tolist())

        if verbose:
            print "Dimensions: " + str(temp.ndim)
            print res

        return res
    #end method normalize
# end class Normalizer