# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current=head
        ans=[]
        while current:
            ans.append(current.val)
            current=current.next
        current=head
        for i in range(len(ans)-1,-1,-1):
            current.val=ans[i]
            current=current.next
        return   head

        