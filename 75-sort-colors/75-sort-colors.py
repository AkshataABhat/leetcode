class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f,s,t=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                f+=1
            elif nums[i]==1:
                s+=1
            else:
                t+=1
        for i in range(0,f):
            nums[i]=0
        for i in range(f,f+s):
            nums[i]=1
        for i in range(f+s,f+s+t):
            nums[i]=2
        return nums
        