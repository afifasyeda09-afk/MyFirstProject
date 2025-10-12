import time
import threading

def do_something(count, out_list):
    # Generate even numbers and store in list
    for i in range(count):
        out_list.append(i * 2)

def run_multithreading():
    size = 100000
    thread_counts = [5, 10, 50]

    print("\n--- Multithreading Test ---")

    for threads in thread_counts:
        out_lists = [[] for _ in range(threads)]
        thread_list = []

        start_time = time.time()

        # Create and start threads
        for i in range(threads):
            t = threading.Thread(target=do_something, args=(size, out_lists[i]))
            thread_list.append(t)
            t.start()

        # Wait for all threads to finish
        for t in thread_list:
            t.join()

        end_time = time.time()

        total_length = sum(len(lst) for lst in out_lists)
        print(f"Threads: {threads}, Total items: {total_length}, Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    run_multithreading()
