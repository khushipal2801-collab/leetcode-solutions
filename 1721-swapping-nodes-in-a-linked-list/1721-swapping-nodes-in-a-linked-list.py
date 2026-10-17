# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left=head
        count=1
        while count<k:
            left=left.next
            count+=1
        current=head
        count=0
        while current:
            current=current.next
            count+=1
        length=count-k
        current=head
        while length>0:
            current=current.next
            length-=1
        right=current
        left.val,right.val=right.val,left.val
        return head



        