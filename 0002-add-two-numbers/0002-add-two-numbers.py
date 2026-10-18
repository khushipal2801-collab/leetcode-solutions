# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        arr1=[]
        current1=l1
        while current1:
            arr1.append(str(current1.val))
            current1=current1.next
        arr2=[]
        current2=l2
        while current2:
            arr2.append(str(current2.val))
            current2=current2.next  
        n1=int("".join(arr1[::-1]))  
        n2=int("".join(arr2[::-1]))  
        total=n1+n2
        dummy=ListNode(0)
        current=dummy
        for digit in str(total)[::-1]:
            current.next=ListNode(int(digit))
            current=current.next
        return dummy.next    

        

        