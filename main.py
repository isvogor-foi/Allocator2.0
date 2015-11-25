__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Allocator as alloc
from random import randint

if __name__ == '__main__':
    #local vars

    counter = 0
    for nComponents in range(5, 15):
        for nUnits in range(3, 6):
            counter += 1
            nResources = randint(3, 5)

            ga_res = sa_res = fss_res = False

            # if by any chance the generated configuration has no solution, generate a new one
            while not ga_res and not sa_res and not fss_res:
                allocator = alloc.Allocator()
                allocator.init(pinit, calculator, nComponents, nUnits, nResources)

                ga_res = allocator.solve_by_ga(nComponents, nUnits, nResources, counter)
                sa_res = allocator.solve_by_sa(nComponents, nUnits, nResources, counter)
                fss_res = allocator.solve_by_fss(nComponents, nUnits, nResources, counter)


