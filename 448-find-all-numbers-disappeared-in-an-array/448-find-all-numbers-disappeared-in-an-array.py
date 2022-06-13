class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        visited=set(nums)
        
        missing=[]
        
        for num in range(1,n+1):
            if num not in visited:
                missing.append(num)
        return missing