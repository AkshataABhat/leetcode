class Solution:
    def findSum(self,A,N): 
        #code here
        maxv,minv=float('-inf'),float('inf')
        for i in range(len(A)):
            if A[i]>maxv:
                maxv=A[i]
            if A[i]<minv:
                minv=A[i]
                
        return maxv+minv



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends