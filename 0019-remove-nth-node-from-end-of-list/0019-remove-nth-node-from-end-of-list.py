# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        a=count-n
        if a==0:
            return head.next
        current=head
        for i in range(1,a):
            current=current.next
        current.next=current.next.next
        return head        
        