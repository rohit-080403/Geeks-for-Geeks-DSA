class Solution:
    def findUnion(self, a, b):
        # code here 
        hashmap = {}
        lists = []
        
        for num in a :
            if num not in hashmap:
                lists.append(num)
                hashmap[num] = True

                

        for num in b :
            if num not in hashmap:
                lists.append(num)
                
                hashmap[num] = True
                
        lists.sort()
        return lists


                