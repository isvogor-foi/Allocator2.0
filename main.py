__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Allocator as alloc
from datetime import *
from random import randint
import multiprocessing

def run_simulation_for_range(units, n_components_start, n_components_end, filename):
    for n_components in range(n_components_start, n_components_end + 1):
        allocator = alloc.Allocator()
        allocator.init(pinit, calculator, n_components, units, 5)
        ra_res = allocator.solve_by_ga(n_components, units, 5, str(str(filename) + "-fs"), 0)
        for i in range(1, 31):
            ra_res = allocator.solve_by_random(n_components, units, 5, str(filename), i)
            ga_res = allocator.solve_by_ga(n_components, units, 5, str(filename), i)
            sa_res = allocator.solve_by_sa(n_components, units, 5, str(filename), i)

if __name__ == '__main__':
    #local vars
    processes = []
    p1 = multiprocessing.Process(target=run_simulation_for_range, args=(3, 6, 10, 1))
    p2 = multiprocessing.Process(target=run_simulation_for_range, args=(4, 8, 12, 2))
    p3 = multiprocessing.Process(target=run_simulation_for_range, args=(5, 11, 15, 3))
    p4 = multiprocessing.Process(target=run_simulation_for_range, args=(6, 14, 18, 4))

    processes.append(p1)
    processes.append(p2)
    processes.append(p3)
    processes.append(p4)

    for process in processes:
        process.start()





