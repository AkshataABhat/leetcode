#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        #Write your code here
        count0=0
        count1=0
        cnt=0
        
        for i in range(len(str)):
            if(str[i]=='0'):
                count0+=1
            else:
                count1+=1
                
            if(count0==count1):
                cnt+=1
                
        if count0 !=count1:
            return -1
            
        return cnt




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends