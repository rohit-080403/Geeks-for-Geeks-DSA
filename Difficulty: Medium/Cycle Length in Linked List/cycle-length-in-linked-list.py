''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head
        
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                count = 1
                curr = slow.next
                
                while curr != slow:
                    count += 1
                    curr = curr.next
                return count
        return 0
        