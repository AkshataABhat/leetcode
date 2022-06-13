class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        visited=set()
        
        for num in nums:
            visited.add(num)
        
        for i in range(0,n+1):
            if i not in visited:
                return i
        
        