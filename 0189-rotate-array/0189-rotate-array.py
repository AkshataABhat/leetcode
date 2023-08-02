class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        i=0
        d=deque(nums)
        
        while i<k:
            tmp=d.pop()
            d.appendleft(tmp)
            i+=1
        nums[:]=d