''' Structure of Doubly Linked List Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        new_node = Node(x)
        curr = head
        
        for _ in range(p):
            curr = curr.next
            
        new_node.next = curr.next
        new_node.prev = curr
        
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        
        return head