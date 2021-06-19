class MaxHeap:

    def __init__(self):
        self.heap = []

    def push(self,value):
         self.heap.append(value)
         self.float_up(len(self.heap)-1)

    def float_up(self,index):
        if index==0:
            return
        else:
            if index%2==0:
                parent_of_index = (index//2)-1
                if self.heap[index]> self.heap[parent_of_index]:
                    temp = self.heap[parent_of_index]
                    self.heap[parent_of_index] = self.heap[index]
                    self.heap[index] = temp
            else:
                parent_of_index = index//2
                if self.heap[index]> self.heap[parent_of_index]:
                    temp = self.heap[parent_of_index]
                    self.heap[parent_of_index] = self.heap[index]
                    self.heap[index] = temp
            self.float_up(parent_of_index)
            
    def peek(self):
        print(self.heap[0])

    def pop(self):
        if len(self.heap)>=2:
            temp = self.heap[0]
            self.heap[0]=self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1]
            self.heap.pop()
            #print("heap after popping largest value =", self.heap)
            self.down_adj()
        elif len(self.heap)==1:
            self.heap.pop()
        else:
            print("Nothing to pop")

    def down_adj(self):
        print("going here")
        index = 0
        for i in range(len(self.heap)//2):
            left_child = index*2+1
            if left_child > len(self.heap)-1:
                print(self.heap)
                print("End Point")
                return
                  
            right_child = index*2+2
            if right_child > len(self.heap)-1:
                print(self.heap)
                print("right child does not exist")
                if self.heap[index]<self.heap[left_child]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left_child]
                    self.heap[left_child] = temp
                    index = left_child
                return
            if self.heap[index]<self.heap[left_child]:
                if self.heap[left_child]<self.heap[right_child]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[right_child]
                    self.heap[right_child] = temp
                    index = right_child
                else:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left_child]
                    self.heap[left_child] = temp
                    index = left_child
            elif self.heap[index]<self.heap[right_child]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[right_child]
                    self.heap[right_child] = temp
                    index = right_child
            else:
                print("No change ", self.heap[index],self.heap[left_child],self.heap[right_child] )
        #self.down_adj()
        print("readjusting heap after popping = ",self.heap)

             
            
H = MaxHeap()
print("*****pushing values**********")
H.push(165)
print(H.heap)
H.push(60)
print(H.heap)
H.push(179)
print(H.heap)
H.push(400)
print(H.heap)
H.push(6)
print(H.heap)
H.push(275)
print(H.heap)
print("*********popping values*******")
H.pop()
H.pop()
H.pop()
H.pop()
H.pop()
H.pop()
H.pop()
