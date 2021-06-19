import threading

def thread_count(count):
    print("I am the thread number ",count,".")

for i in range(1,6):
    t = threading.Thread(target = thread_count,args = (i,))
    t.start()
    t.join()
    
print("Main thread exiting now")    









