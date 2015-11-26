__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Allocator as alloc
from datetime import *
from random import randint

def append_status(message):
    with open("solutions/status.txt", "a+") as file:
        file.write(message + "\n")

if __name__ == '__main__':
    #local vars

    counter = 0
    start_time = datetime.now()
    append_status("Started at: " + str(start_time))
    append_status("Total files:" + str(7 * 25))
    append_status("Max search space: " + str(7**25))

    # for nComponents in range(5, 30):
    #     for nUnits in range(3, 10):
    #         counter += 1
    #         nResources = randint(3, 9)
    #         # repeat 30 times for one input setup
    #         for i in range(0, 45):
    #             print(i)
    #             allocator = alloc.Allocator();
    #             allocator.init(pinit, calculator, nComponents, nUnits, nResources)
    #             ga_res = allocator.solve_by_ga(nComponents, nUnits, nResources, counter, i)
    #             sa_res = allocator.solve_by_sa(nComponents, nUnits, nResources, counter, i)
    #             fss_res = allocator.solve_by_fss(nComponents, nUnits, nResources, counter, i)

    nComponents = 15
    nUnits = 5
    nResources = 5
    for i in range(0, 50):
        allocator = alloc.Allocator()
        allocator.init(pinit, calculator, nComponents, nUnits, nResources)
        ra_res = allocator.solve_by_random(nComponents, nUnits, nResources, 1, 1)
        ga_res = allocator.solve_by_ga(nComponents, nUnits, nResources, 1, 1)
        sa_res = allocator.solve_by_sa(nComponents, nUnits, nResources, 1, 1)
        #fss_res = allocator.solve_by_fss(nComponents, nUnits, nResources, 1, 1)

        # append_status("Done with: " + str(nComponents) + " and " + str(nUnits) +
        #               "from (5-30) components and (3-10)units")

    end_time = datetime.now()
    append_status("Ended at: " + str(end_time))
    append_status("Total: " + str(end_time-start_time))




