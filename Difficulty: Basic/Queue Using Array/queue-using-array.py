from collections import deque
class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.deque = deque()
        self.capacity = n

    
    def isEmpty(self):
        # Check if queue is empty
        return len(self.deque) == 0

    
    def isFull(self):
        # Check if queue is full
        return len(self.deque) == self.capacity


    
    def enqueue(self, x):
        # Enqueue
        if not self.isFull():
            self.deque.append(x)
            return True
        return False
            

    
    def dequeue(self):
        # Dequeue
        if not self.isEmpty():
            self.deque.popleft()
            return True
        return False

    
    def getFront(self):
        # Get front element
        if not self.isEmpty():
            return self.deque[0]
        return -1
       
    
    def getRear(self):
        # Get rear element 
        if not self.isEmpty():
            return self.deque[-1]
        return -1
        
        
        