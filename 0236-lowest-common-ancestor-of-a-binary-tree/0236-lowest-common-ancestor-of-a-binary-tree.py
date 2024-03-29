# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if root==p or root==q:
            return root
        
        rl=self.lowestCommonAncestor(root.left,p,q)
        rr=self.lowestCommonAncestor(root.right,p,q)
        
        
        if rl and rr:
            return root
        
        return rl if rl is not None else rr

        