import threading
import time


def work_for_t1():
    
    print('Starting of thread :', threading.current_thread().name)
    for i in range(0,11):
        print("Printing Number : ",i," \n")
        time.sleep(2)
    print('Finishing of thread :', threading.current_thread().name," \n")


t1 = threading.Thread(target=work_for_t1, name='Thread1')
t1.setDaemon(True)
t1.start()
time.sleep(5)
print("Finishing thread: ", threading.current_thread().name," \n")
t1.join()
