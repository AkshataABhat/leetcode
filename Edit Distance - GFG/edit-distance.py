class Solution:
	def editDistance(self, s, t):
		# Code here
		cache=[[0 for j in range(len(t)+1)]for i in range(len(s)+1)]
		for i in range(len(s)+1):
		    cache[i][len(t)]=len(s)-i
		    
		for j in range(len(t)+1):
		    cache[len(s)][j]=len(t)-j
		    
		for i in range(len(s)-1,-1,-1):
		    for j in range(len(t)-1,-1,-1):
		        if(s[i]==t[j]):
		            cache[i][j]=cache[i+1][j+1]
		        else:
		            cache[i][j]=1+min(cache[i+1][j],cache[i][j+1],cache[i+1][j+1])
		return cache[0][0]
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends