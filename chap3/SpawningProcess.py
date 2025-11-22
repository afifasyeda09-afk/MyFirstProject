import random
import multiprocessing

def do_something(count, out_list):
    for i in range(count):
        out_list.append(i * 2)

def run():
    out = []
    do_something(6, out)
    print("Spawned process output:", out)

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    p = multiprocessing.Process(target=run)
    p.start()
    p.join()
