import random
from multiprocessing import Process
import time

def do_something(count, out_list):
    for i in range(count):
        out_list.append(i * 2)

def background():
    out = []
    do_something(5, out)
    print("Background data:", out)
    while True:
        print("Running...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=background)
    p.daemon = True  # background
    p.start()

    time.sleep(3)
    print("Main program ends (daemon stops automatically)")
