#User function Template for python3

class Solution:
        
    def minSwap (self,arr, n, k) : 
        #Complete the function
        count=0
        for i in range(0,n):
            if (arr[i]<=k):
                count+=1
                
        bad=0
        for i in range(0,count):
            if (arr[i]>k):
                bad+=1
        
        ans=bad
        j=count
        for i in range(0,n):
            if j==n:
                break
            if (arr[i]>k):
                bad-=1
                
            if(arr[j]>k):
                bad+=1
                
            ans=min(ans,bad)
            i+=1
            j+=1
            
        return ans
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ob=Solution()
    ans = ob.minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends