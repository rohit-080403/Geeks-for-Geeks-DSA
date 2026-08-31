class Solution:
    def largest(self, arr):
        # code here
        max_num = arr[0]
        
        for num in arr:
            if num > max_num:
                max_num = num
        return max_num
                
        
