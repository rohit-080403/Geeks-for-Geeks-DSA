class Solution:
    def getSecondLargest(self, arr):
        # code here
        if len(arr) < 2:
            return -1
            
        largest = float("-inf")
        second_largest = float("-inf")
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        return second_largest if second_largest != float("-inf") else -1