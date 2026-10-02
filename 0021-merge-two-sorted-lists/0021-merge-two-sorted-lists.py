# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        temp=dummy
        current1=list1
        current2=list2
        while current1 and current2:
            if current1.val>=current2.val:
                temp.next=current2
                temp=temp.next
                current2=current2.next
            else:
                temp.next=current1
                temp=temp.next
                current1=current1.next
        while current1:
                temp.next=current1
                temp=temp.next
                current1=current1.next
        while current2:
                temp.next=current2
                temp=temp.next
                current2=current2.next
        return dummy.next                   

        