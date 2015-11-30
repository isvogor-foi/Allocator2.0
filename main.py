__author__ = 'ivan'

import PlatformInitializer as pinit
import Calculator as calculator
import Allocator as alloc
import smtplib
import multiprocessing

def run_simulation_for_range(units, n_components_start, n_components_end, filename):
    for n_components in range(n_components_start, n_components_end + 1):
        allocator = alloc.Allocator()
        allocator.init(pinit, calculator, n_components, units, 5)
        for i in range(1, 10):
            ra_res = allocator.solve_by_random(n_components, units, 5, str(filename), i)
            ga_res = allocator.solve_by_ga(n_components, units, 5, str(filename), i)
            sa_res = allocator.solve_by_sa(n_components, units, 5, str(filename), i)

def send_status_email():
    sender = "isvogor@foi.hr"
    receivers = ["isvogor@foi.hr"]

    message = """From: COURSES.FOI.HR <isvogor@foi.hr>
    To: Ivan Svogor <isvogor@foi.hr>
    Subject: Simulation status

    Processing done!
    """

    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receivers, message)
       print("Successfully sent email")
    except Exception:
       print("Error: unable to send email")

if __name__ == '__main__':
    #local vars
    processes = []
    p1 = multiprocessing.Process(target=run_simulation_for_range, args=(10, 20, 30, 1))
    p2 = multiprocessing.Process(target=run_simulation_for_range, args=(15, 30, 40, 2))
    p3 = multiprocessing.Process(target=run_simulation_for_range, args=(20, 40, 50, 3))
    p4 = multiprocessing.Process(target=run_simulation_for_range, args=(25, 50, 60, 4))
    p5 = multiprocessing.Process(target=run_simulation_for_range, args=(30, 60, 70, 5))
    #p5 = multiprocessing.Process(target=run_simulation_for_range, args=(5, 12, 12, 5))

    processes.append(p4)
    processes.append(p3)
    processes.append(p2)
    processes.append(p1)
    processes.append(p5)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    #send_status_email()



