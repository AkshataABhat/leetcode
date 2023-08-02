class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        t=len(nums)/2
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
                
            if hashmap[num]>t:
                return num
                
            
        