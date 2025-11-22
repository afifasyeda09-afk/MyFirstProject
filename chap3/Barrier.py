import random
from multiprocessing import Process, Barrier

def do_something(count, out_list):
    for i in range(count):
        out_list.append(i * 2)

def worker(id, bar):
    out = []
    do_something(3, out)
    print(f"Worker {id} reached barrier with:", out)
    bar.wait()
    print(f"Worker {id} passed barrier")

if __name__ == "__main__":
    bar = Barrier(3)

    processes = [Process(target=worker, args=(i, bar)) for i in range(3)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
