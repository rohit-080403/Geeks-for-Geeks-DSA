''' class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

class Solution:
    def createDLL(self, arr):
       # code here
        if not arr:
            return None
        
        head = Node(arr[0])
        curr = head
        
        for value in arr[1:]:
            new_node = Node(value)
            
            curr.next = new_node
            new_node.prev = curr
            
            curr = new_node
        return head