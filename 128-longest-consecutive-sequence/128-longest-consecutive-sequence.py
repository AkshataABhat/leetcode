class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #can use sorting but it takes O(n^2) Time Complexity
        #so use sets
        nums_set=set(nums)
        max_len=0
        for i in nums:
            length=0
            if i-1 not in nums_set:
                while (i+length) in nums_set:
                    length+=1
                max_len=max(max_len,length)
        return max_len