class Solution(object):
    def missingNumber(self, nums):
        
        n=len(nums)
        
        visited=set(nums)
        
        for num in range(0,n+1):
            if num not in visited:        
                 return num
        