import random
from multiprocessing import Process
import time

def do_something(count, out_list):
    for i in range(count):
        out_list.append(i * 2)

def normal_task():
    out = []
    do_something(5, out)
    print("Normal process output:", out)
    time.sleep(3)

if __name__ == "__main__":
    p = Process(target=normal_task)
    p.daemon = False
    p.start()
    p.join()
    print("Finished normal process")
