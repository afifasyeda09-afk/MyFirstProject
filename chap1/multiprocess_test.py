import time
import multiprocessing

def do_something(count):
    result = [i * 2 for i in range(count)]  # Create even numbers
    return result

def run_multiprocessing():
    size = 100000
    process_counts = [5, 10, 50]

    print("\n--- Multiprocessing Test ---")

    for procs in process_counts:
        start_time = time.time()

        with multiprocessing.Pool(processes=procs) as pool:
            results = pool.map(do_something, [size] * procs)

        end_time = time.time()

        total_length = sum(len(r) for r in results)
        print(f"Processes: {procs}, Total items: {total_length}, Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    multiprocessing.freeze_support()  # Needed for Windows
    run_multiprocessing()
