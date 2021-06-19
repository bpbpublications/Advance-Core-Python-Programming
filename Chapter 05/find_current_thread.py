import threading

def thread_count(count):
    print("I am the thread number ",count,".")
    print("My name is ",threading.currentThread().getName())
    print("active coutn",threading.activeCount())
    l1 = threading.enumerate()
    for i in l1:
        print(i)
    #print(threading.enumer)

for i in range(1,6):
    t = threading.Thread(target = thread_count,args = (i,))
    t.start()
    t.join()
