import threading

t = threading.Semaphore(3)
def count():
    t.acquire()
    print("Start")
    for i in range(1, 6):
        print(i)
    t.release()
    
thread1 = threading.Thread(target=count)
thread2 = threading.Thread(target=count)
thread3 = threading.Thread(target=count)
thread4 = threading.Thread(target=count)
thread5 = threading.Thread(target=count)
thread6 = threading.Thread(target=count)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
