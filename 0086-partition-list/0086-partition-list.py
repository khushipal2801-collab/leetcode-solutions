# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        smallest=ListNode(0)
        largest=ListNode(0)
        s=smallest
        l=largest
        current=head
        while current:
            if current.val<x:
                s.next=current
                s=s.next
            else:
                l.next=current
                l=l.next
            current=current.next
        l.next=None
        s.next=largest.next
        return smallest.next           
        


        