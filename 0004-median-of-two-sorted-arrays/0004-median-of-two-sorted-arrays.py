class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr3=nums1+nums2
        arr3.sort()
        
        n=len(arr3)
        
        if n%2==0:
            z=n//2
            e,q=arr3[z],arr3[z-1]
            ans=(e+q)/2
        else:
            z=n//2
            ans=arr3[z]
        return ans
        