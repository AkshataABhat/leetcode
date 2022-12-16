#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		max_ending_here=arr[0]
		min_ending_here=arr[0]
		max_so_far=arr[0]
		
		for i in range(1,n):
		    temp=max(max(arr[i],arr[i]*max_ending_here),arr[i]*min_ending_here)
		    min_ending_here=min(min(arr[i],arr[i]*max_ending_here),arr[i]*min_ending_here)
		    max_ending_here=temp
		    max_so_far=max(max_so_far,max_ending_here)
		    
		return max_so_far


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends