class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        total=len(original)
        
        if m*n !=total:
            return []
        
        
        itr=0
        ans=[]
        for iterations in range(1,m+1):
            arr=[]
            
            while itr<iterations *n:
                arr.append(original[itr])
                itr+=1
             
            ans.append(arr)
            
        return ans