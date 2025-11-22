import random
from multiprocessing import Process, current_process

def do_something(count, out_list):
    for i in range(count):
        out_list.append(i * 2)

def task():
    out = []
    do_something(4, out)
    print("Running:", current_process().name, "| Output:", out)

if __name__ == "__main__":
    p = Process(target=task, name="MyCustomProcess")
    p.start()
    p.join()
