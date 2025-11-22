import random
from multiprocessing import Pool

def do_something(count, out_list):
    for i in range(count):
        out_list.append(i * 2)

def process_job(n):
    out = []
    do_something(n, out)
    return out

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        result = pool.map(process_job, [3, 4, 5])
        print(result)
