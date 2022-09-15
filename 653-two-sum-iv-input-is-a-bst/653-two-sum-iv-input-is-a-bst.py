# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values=[]
        self.inorder(root,values)
        l,r=0,len(values)-1
        
        
        while l<r:
        
            if values[l]+values[r]<k:
                l+=1
            
            elif values[l]+values[r]>k:
                r-=1 
            
            else:
                return True 
        
        return False         
        
        
    def inorder(self,root,res):
        if not root:
            return 
        
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)