# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k  # Initialize k as an instance variable
        
        def dfs(node):
            if not node:
                return None
            
            # Traverse the left subtree
            result = dfs(node.left)
            
            # Check if the kth smallest element has been found
            if self.k == 0:
                return result
            
            # Decrement k as you visit each node
            self.k -= 1
            
            # Check if the current node is the kth smallest element
            if self.k == 0:
                return node.val
            
            # Traverse the right subtree
            return dfs(node.right)
        
        return dfs(root)
