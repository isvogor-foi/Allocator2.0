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

        if verbose:
            print "Dimensions: " + str(temp.ndim)
            print res

        return res
    #end method normalize

    def eigenvector(self, matrix):

        eigenvalues, eigenvectors = la.eig(matrix)
        b = max(eigenvalues)

        index = -1
        for i in range(0, len(eigenvalues)):
            if eigenvalues[i] == b:
                index = i

        self.eigenvalue = b.real

        self.tradeOffMatrixF = []
        for j in range(0, len(eigenvectors[0])):
            self.tradeOffMatrixF.append(eigenvectors[j][0].real)

        self.eigenvector = copy.deepcopy(self.tradeOffMatrixF)

        sumVal = sum(self.tradeOffMatrixF)

        # normalize (sum = 1)
        for i in range(0,len(self.tradeOffMatrixF)):
            self.tradeOffMatrixF[i] = self.tradeOffMatrixF[i] / float(sumVal)

        print "final vector F: ", self.tradeOffMatrixF
        print "final eigenvalue: ", self.eigenvalue
    #end method eigenvector

# end class Normalizer