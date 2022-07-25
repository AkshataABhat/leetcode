class Solution(object):
    def isPalindrome(self, s):
        
        
        newStr=""
        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        return newStr==newStr[::-1]
    
        """
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.alphanum(s[l]):
                l+=1
            while r>l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower() !=s[r].lower():
                return False
        return True
    def alphanum(self, c):
        return (ord('A')<=ord(c)<=ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9'))
    
    
          """
   
        