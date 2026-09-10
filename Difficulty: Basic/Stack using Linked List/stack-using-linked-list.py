''' Structure of linked list Node
 class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 
'''

class myStack:

    def __init__(self):
        # Initialize your data members
        self.head = None
        self._size = 0
        

    def isEmpty(self):
        # Check if the stack is empty
        return self.head is None
        
        

    def push(self, x):
        # Adds element x to the top of the stack
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
            
        
        

    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return -1
        popped_val = self.head.data  # Grab the data
        self.head = self.head.next   # Move head to the next node
        self._size -= 1              # Reduce size count
        return popped_val
        


    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.isEmpty():
            return -1
        return self.head.data


    def size(self):
        # Returns the current size of the stack
        return self._size