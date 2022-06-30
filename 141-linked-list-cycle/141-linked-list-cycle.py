# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited={}
        if not head:
            return None
        while head:
            if head not in visited:
                visited[head]=1
                head=head.next
            else:
                return True
        return False