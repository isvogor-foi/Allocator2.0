__author__ = 'Ivan'

import numpy as np
import copy

from scipy import linalg as la

class Calculator:

    def normalize(self, matrix, verbose = False):
        temp = np.array(matrix)
        res = []

        # if more than 3 dimensions, use dimension max
        if(temp.ndim >= 3):
            for depth in temp:
                res.append((depth / (depth.max() * 1.0)).tolist())
        else:
            res.append((temp / (temp.max() * 1.0)).tolist())
            res = res[0]

        if verbose:
            print "Dimensions: " + str(temp.ndim)
            print res

        return res

    #end method normalize

    def eigenvector(self, matrix, verbose = False):
        # calculate eigenvector and eigenvalue
        eigenvalues, eigenvectors = la.eig(matrix)
        # principal eigenvalue is max eigenvalue
        principal_eigenvalue = max(eigenvalues)
        eigenvalue_real_part = principal_eigenvalue.real

        trade_off_vector = []
        for i in range(0, len(eigenvectors[0])):
            trade_off_vector.append(eigenvectors[i][0].real)

        sumVal = sum(trade_off_vector)

        # normalize so the sum equals 1
        trade_off_vector = [trade_off_vector[i] / float(sumVal) for i in range(0, len(trade_off_vector))]

        if verbose:
            print "final vector F: ", trade_off_vector
            print "final eigenvalue: ", eigenvalue_real_part

        return trade_off_vector
    #end method eigenvector

# end class Normalizer