"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q=[]
        q.append(root)
        while q:
            row=[]
            cnt=len(q)
            while cnt>0:
                cnt-=1 
                node=q.pop(0)
                row.append(node)
                if not node:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            for i in range(len(row)-1):
                row[i].next=row[i+1]

        return root 
            
        