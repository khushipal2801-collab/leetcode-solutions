# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        current=head
        count=0
        while current and count<k:
            count+=1
            current=current.next
            
            
        if count==k:
            prev=current
            current=head
            for i in range(k):
                next=current.next
                current.next=prev
                prev=current
                current=next
            head.next=self.reverseKGroup(current,k)    
            head=prev 
        return head



            


        