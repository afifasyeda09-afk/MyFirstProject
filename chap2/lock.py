import threading
import time
import random

def do_something(count, out_list, lock):
    for i in range(count):
        num = i * 2  # even number
        with lock:   # lock to prevent race condition
            out_list.append(num)

def run_threads_with_lock():
    size = 100000
    thread_counts = [5, 10, 50]

    print("\n--- Multithreading with Lock Test ---")

    for threads in thread_counts:
        out_list = []
        lock = threading.Lock()
        jobs = []

        start_time = time.time()

        # Create threads
        for i in range(threads):
            t = threading.Thread(target=do_something, args=(size, out_list, lock))
            jobs.append(t)
            t.start()

        # Wait for all threads to finish
        for t in jobs:
            t.join()

        end_time = time.time()
        print(f"Threads: {threads}, Total items: {len(out_list)}, Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    run_threads_with_lock()
