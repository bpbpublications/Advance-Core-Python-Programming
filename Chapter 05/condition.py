import threading
import time
lst = []

def buy():
    c.acquire()
    for i in range (1,6):
        item = input("Enter the item bought : ")
        lst.append(item)
    print("Notifying t2")
    c.notify()
    c.release()



def billing():
    c.acquire()
    c.wait(timeout = 0)
    c.release()
    print("you are billed for:")
    for item in lst:
        print(item)

c = threading.Condition()
t1 = threading.Thread(target = buy)
t2 = threading.Thread(target = billing)

t1.start()
time.sleep(5)
t2.start()
t1.join()
t2.join()
