''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        # code here
        prev = None
        curr = head
        
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
            
        curr = prev
        carry = 1
        
        while curr and carry:
            total = curr.data + carry
            curr.data = total % 10
            carry = total // 10
            
            if curr.next is None and carry:
                curr.next = Node(0)
            curr = curr.next
            
        prev2 = None
        curr = prev
        
        while curr :
            new_node = curr.next
            curr.next = prev2
            prev2 = curr
            curr = new_node
            
        return prev2