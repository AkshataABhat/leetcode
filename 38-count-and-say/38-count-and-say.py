class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        prev=self.countAndSay(n-1)
        res=""
        ctr=1
        for i in range(len(prev)):
            if i==len(prev)-1 or prev[i] !=prev[i+1]:
                res+=str(ctr)+prev[i]
                ctr=1
            else:
                ctr+=1
        return res
                