import threading
import time

a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()

def thread1calc():
    global
    print('Tread1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    print('Thread1 acquiring lock b')
    b_lock.acquire()