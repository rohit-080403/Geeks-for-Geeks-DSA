'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        if not head or not head.next:
            return head
            
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
            
        left = self.segregate(head)
        right = self.segregate(mid)
        
        dummy = Node(0)
        curr = dummy
        
        while left and right:
            if left.data < right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
            
        if left:
            curr.next = left
        if right :
            curr.next = right
        
        return dummy.next
    
    