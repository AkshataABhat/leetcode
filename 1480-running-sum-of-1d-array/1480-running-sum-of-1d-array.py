class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=0
        lst=[]
        for i in nums:
            a=a+i
            lst.append(a)
        return lst