# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        current=head
        ans=[]
        while current:
            ans.append(current.val)
            current=current.next
        ans.sort()
        current=head
        for i in range(len(ans)):
            current.val=ans[i]
            current=current.next
        return head     
        