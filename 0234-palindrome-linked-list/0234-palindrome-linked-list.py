# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        slow=head
        isPalin=True
        while slow!=None:
            stack.append(slow.val)
            slow=slow.next
        while head!=None:
            i=stack.pop()
            if head.val==i:
                isPalin=True
            else:
                isPalin=False
                break
            head=head.next
            
        return isPalin
            
        