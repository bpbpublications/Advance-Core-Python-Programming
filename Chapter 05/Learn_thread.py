import time
import threading

class Learn_thread(threading.Thread):
    def __init__(self,name,sec):

        #invoke __init__ of base class
        threading.Thread.__init__(self)
        self.name = name
        self.sec = sec
        
        
    #Overriding run()method
    def run(self):
        print('\n thread {} has started'.format(self.getName()),"\n")
        nap(self.sec,self.name)



def nap(sec,name):
    print("\n Hi I am a thread and my name is {}. I am here only to take a nap of {} seconds".format(name,sec),"\n")
    time.sleep(sec)
    print("{} seconds are over {} is up!!".format(sec,name),"\n")


t1 = Learn_thread("King-thread",10)
t2 = Learn_thread("Queen-thread",6)
t3 = Learn_thread("Page-thread",7)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
