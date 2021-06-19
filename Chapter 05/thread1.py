import time
import threading
names=[]


def getnames():
    guest_name = input("Enter a guest name : ")
    names.append(guest_name)
    confirmation = input("Any more guests? (y/n) : ")
    if(confirmation == 'y'):
        getnames()
    
def welcome_guests(names):
    for name in names:
        print("Welcome to our club",name)
        time.sleep(5)
        
def get_id(names):
    count=1
    for name in names:
        print("The guest_id of ",name,"is :", count)
        count =  count+1
        time.sleep(10)
        
getnames()
t = time.time()

#Create Threads
t1 = threading.Thread(target=welcome_guests, args = (names,))
t2 = threading.Thread(target=get_id, args = (names,))

#Start Threads
t1.start()
time.sleep(2)
t2.start()

#Joined the threads:
t1.join()
t2.join()

print("All Done enjoy")
