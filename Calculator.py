__author__ = 'ivan'

import numpy as np
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
            print ("Dimensions: " + str(temp.ndim))
            print (res)

        return res

    #end method normalize

    def eigenvector(self, matrix, verbose = False):
        # calculate eigenvector and eigenvalue
        eigenvalues, eigenvectors = la.eig(matrix)

        # principal eigenvalue is max eigenvalue
        principal_eigenvalue = max(eigenvalues)
        principal_eigenvalue_index = np.where(eigenvalues == principal_eigenvalue)[0][0]
        self.eigenvalue_real_part = principal_eigenvalue.real

        trade_off_vector = []
        # take the vector of the principal value position !!!
        for i in range(0, len(eigenvectors[principal_eigenvalue_index])):
            #print("Real: ", eigenvectors[i][principal_eigenvalue_index].real)
            trade_off_vector.append(eigenvectors[i][principal_eigenvalue_index].real)

        sumVal = sum(trade_off_vector)

        # normalize so the sum equals 1
        trade_off_vector = [trade_off_vector[i] / float(sumVal) for i in range(0, len(trade_off_vector))]

        if verbose:
            print ("Eigenvalues: ", eigenvalues)
            print ("Eigenvector: \n", eigenvectors)
            print ("final vector F: ", trade_off_vector)
            print ("Principal eigenvalue: ", self.eigenvalue_real_part)

        return trade_off_vector
    #end method eigenvector

    def calculateConsistency(self, pairwiseMatrix):
        # hardcoded AHP table... yes... :)
        RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
        CI = (self.eigenvalue_real_part - len(pairwiseMatrix)) / (len(pairwiseMatrix) - 1)
        if CI < 0:
            CI = 0
        self.consistencyRatio = CI / RI[len(pairwiseMatrix) - 1]
        return self.consistencyRatio
