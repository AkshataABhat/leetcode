class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
            l,m,h=0,0,arr_size-1 
    while m<=h:
        if arr[m]==0:
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1 
        elif arr[m]==1:
            m+=1 
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
    
        
    
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
        