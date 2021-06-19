#Define Stack Class
class Stack:
    #declare constructor
    def __init__(self, n):
        self.stack = []
        self.size = n
        
    #push operation
    def push(self,element):
        if(len(self.stack)== self.size):
            print("no more elements can be appended as the stack is full")
        else:
            self.stack.append(element)
            
    #pop operation
    def pop(self):
        if self.stack == []:
            print("Stack is empty. Nothing to POP!!")
        else:
 #           print("Here")
            self.stack.pop()
                    


s = Stack(3)
s.push(6)
s.push(2)
print(s.stack)
s.pop()
print(s.stack)


