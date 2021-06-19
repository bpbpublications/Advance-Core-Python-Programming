import threading
x = 0
y = 0

def thread_sync1(number):

    global x
    global y
    print("thread_sync1 acquiring lock\n")
    lock.acquire()
    x = number*2
    print("thread_sync1 acquiring lock\n")
    lock.acquire()
    z = x+y
    print("z =",z)
    print("thread_sync1 releasing lock\n")
    lock.release()
    print("thread_sync1 releasing lock\n")
    lock.release()
    print("thread_sync1 done\n")
    

def thread_sync2(number):
    global x
    global y
    print("thread_sync2 acquiring lock\n")
    lock.acquire()
    y = number*4
    print("thread_sync2 acquiring lock\n")
    lock.acquire()
    v = y - x
    print("v = ",v)
    print("thread_sync2 releasing lock\n") 
    lock.release()
    print("thread_sync2 releasing lock\n") 
    lock.release()
    print("thread_sync2 done\n")

lock = threading.RLock()    
t1 = threading.Thread(target = thread_sync1, args =(2,))
t2 = threading.Thread(target = thread_sync2, args =(3,))
                      
t1.start()
t2.start()
t1.join()
t2.join()

print("Final x = ",x)
print("Final y = ",y)
