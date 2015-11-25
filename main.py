__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Allocator as alloc
from datetime import *
from random import randint
import multiprocessing

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

    for nComponents in range(5, 30):
        for nUnits in range(3, 10):
            counter += 1
            nResources = randint(3, 9)
            # repeat 30 times for one input setup
            for i in range(0, 45):
                print(i)
                # if by any chance the generated configuration has no solution, generate a new one
                #ga_res = sa_res = fss_res = False
                #while not ga_res and not sa_res and not fss_res:
                allocator = alloc.Allocator()
                allocator.init(pinit, calculator, nComponents, nUnits, nResources)
                p1 = multiprocessing.Process(target=allocator.solve_by_ga, args=(nComponents, nUnits, nResources, counter, i))
                p2 = multiprocessing.Process(target=allocator.solve_by_sa, args=(nComponents, nUnits, nResources, counter, i))
                p3 = multiprocessing.Process(target=allocator.solve_by_fss, args=(nComponents, nUnits, nResources, counter, i))
                #sa_res = fss_res = True

                p1.start()
                p2.start()
                p3.start()

                    #ga_res = allocator.solve_by_ga(nComponents, nUnits, nResources, counter)
                    #sa_res = allocator.solve_by_sa(nComponents, nUnits, nResources, counter)
                    #fss_res = allocator.solve_by_fss(nComponents, nUnits, nResources, counter)

        append_status("Done with: " + str(nComponents) + " and " + str(nUnits) +
                      "from (5-30) components and (3-10)units")

    end_time = datetime.now()
    append_status("Ended at: " + str(end_time))
    append_status("Total: " + str(end_time-start_time))




