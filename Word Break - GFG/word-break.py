#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    dp=[False]*(len(line)+1)
    dp[len(line)]=True
    
    for i in range(len(line)-1,-1,-1):
        for w in dictionary:
            if(i+len(w))<=len(line) and line[i:len(w)+i]==w:
                dp[i]=dp[i+len(w)]
            if dp[i]:
                break
            
    return dp[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends