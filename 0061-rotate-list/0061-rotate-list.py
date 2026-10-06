# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or  head.next is None:
            return head
        current=head
        count=0
        while current.next:
            count+=1
            current=current.next
        count+=1    
        k=k%count
        if k==0:
            return head
        current.next=head
        s=count-k
        temp=head
        for i in range(s-1):
            temp=temp.next
        newhead=temp.next    
    
        temp.next=None
        return newhead    





        