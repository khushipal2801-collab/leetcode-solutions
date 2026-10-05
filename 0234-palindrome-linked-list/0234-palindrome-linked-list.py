# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        current=slow
        prev=None
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        
        p1=head
        p2=prev
        while p2:
            if p1.val !=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True             
        