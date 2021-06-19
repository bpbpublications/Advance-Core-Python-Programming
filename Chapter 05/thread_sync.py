import threading

x = 0
range_val = int(input("Enter the range : "))


def thread_sync(lock):
    global x
    for i in range(range_val):
       # lock.acquire()
        x += 1
        lock.release()
        
    
lock = threading.Lock()
t1 = threading.Thread(target = thread_sync, args = (lock,))
t2 = threading.Thread(target = thread_sync, args = (lock,))
t1.start()
t2.start()
t1.join()
t2.join()

print(x)
