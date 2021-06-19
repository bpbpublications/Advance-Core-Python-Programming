import threading
import time

def task(event, sec):
  print("Started thread but waiting for event...")
  # make the thread wait for event with timeout set
  internal_set = event.wait(sec)
  print("waiting")
  if internal_set:
    print("Event set")
  else:
    print("Time out,event not set")
    
    
# initializing the event object
e = threading.Event()
print("Event is set.")
# starting the thread
t1 = threading.Thread(name='Event-Blocking-Thread', target=task, args=(e,10))
t1.start()
t1.join()
e.set()

  
  
  
