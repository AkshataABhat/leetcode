class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        
        #l,r=0,len(s)-1
        #while l<r:
        #   s[l],s[r]=s[r],s[l]
        #    l,r=l+1,r-1
        
        """
        stack=[]
        for c in s:
            stack.append(c)
        i=0
        while stack:
            s[i]=stack.pop()
            i+=1
            
        """
        def reverse(l,r):
            while l<r:
                s[l],s[r]=s[r],s[l]
            return reverse(l+1,r-1)
        reverse(0,len(s)-1)
        """