import threading
import time

lock = threading.Lock()

counter: int = 0

def increment_count():
    global counter
    for _ in range(5):
        with lock:
            counter += 1
            print(f"{threading.current_thread().name} increment 1 to counter, counter:{counter}")
            time.sleep(1)

thread_1 = threading.Thread(target=increment_count, name="thread_1")
thread_2 = threading.Thread(target=increment_count, name="thread_2")

# start the threads
thread_1.start()
thread_2.start()

# wait for threads to finish
thread_1.join()
thread_2.join()

print(f"Final counter value: {counter}")