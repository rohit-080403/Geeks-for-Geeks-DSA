class Solution:
	def nextSmallerEle(self, arr):
		# code here
		stack = []
		res = [-1] * len(arr)
		
		for i in range(len(arr)):
		    while stack and arr[i] < arr[stack[-1]]:
		        popped_index = stack.pop()
		        res[popped_index] = arr[i]
		    stack.append(i)
	    return res