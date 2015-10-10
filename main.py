__author__ = 'Ivan'

import PlatformInitializer as pinit
import Normalizer as norm

if __name__ == '__main__':

    verbose = True

    #initialize input
    initializer = pinit.ComponentInitializer()
    initializer.initialize(3, 10, 1, 9)

    #normalize input matrices
    normalizer = norm.Normalizer()

    normalizer.normalize(initializer.componentMatrix, True)
    normalizer.normalize(initializer.resourceMatrix, True)


