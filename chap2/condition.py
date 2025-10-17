import threading
import random

condition = threading.Condition()

def do_something(count, out_list):
    for i in range(count):
        with condition:
            out_list.append(i * 2)
            if i in (5, 10, 50):  # when i reaches 5, 10, or 50
                print(f"Reached {i}, notifying...")
                condition.notify_all()  # signal other threads
            else:
                condition.wait(timeout=0.1)  # wait briefly before next iteration

if __name__ == "__main__":
    output = []
    t = threading.Thread(target=do_something, args=(60, output))
    t.start()
    t.join()

    print("Done. Output length:", len(output))
