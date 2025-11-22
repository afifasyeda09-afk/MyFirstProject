import random
from multiprocessing import Process
import time

def do_something(count, out_list):
    for i in range(count):
        out_list.append(i * 2)

def worker():
    data = []
    do_something(5, data)
    print("Process data:", data)
    time.sleep(10)

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()

    time.sleep(2)
    print("Killing process...")
    p.terminate()
    p.join()
    print("Process killed.")
