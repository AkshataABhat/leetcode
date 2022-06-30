# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        #iterative TC:O(n) SC:O(1)
        
        prev,cur=None, head
        
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev */
        """
        #recursive TC:O(n) SC:O(n)
        
        if not head:
            return None
        newHead=head
        if head.next:
            newHead=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return newHead