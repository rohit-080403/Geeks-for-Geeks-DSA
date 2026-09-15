''' Structure of doubly linked list Node
 class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteHead(self, head):
        # code here
        if not head:
            return None
        head = head.next
        
        if head:
            head.prev = None
        return head