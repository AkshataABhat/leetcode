#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        ans=arr[n-1]-arr[0]
        smallest=arr[0]+k
        biggest=arr[n-1]-k
        
        for i in range(1,n):
            if arr[i] < k:
                continue
            small=min(smallest,arr[i]-k)
            big=max(biggest,arr[i-1]+k)
            ans=min(ans,big-small)
            
        return ans
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends