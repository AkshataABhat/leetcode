class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0  # Initialize instance attribute count
        self.result = None  # Initialize instance attribute result
        
        def inorder_traversal(node):
            if not node or self.count >= k:
                return
            
            # Traverse the left subtree
            inorder_traversal(node.left)
            
            # Process the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
            
            # Traverse the right subtree
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.result
