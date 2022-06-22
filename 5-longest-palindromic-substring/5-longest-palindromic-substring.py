class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        
        for i in range(len(s)):
            right=left=i
            while left>=0 and right<len(s) and s[right]==s[left]:
                if(right-left+1)>resLen:
                    res=s[left:right+1]
                    resLen=right-left+1
                right+=1
                left-=1
                    
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[right]==s[left]:
                if(right-left+1)>resLen:
                    res=s[left:right+1]
                    resLen=right-left+1
                right+=1
                left-=1
                    
        return res