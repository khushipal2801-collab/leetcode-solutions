# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.       q                                       q       

        
        arr=[]
        curr=head
        while curr:
            arr.append(curr)
            curr=curr.next
        left=0
        right=len(arr)-1
        while left<right:
            arr[left].next=arr[right]
            left+=1

            if left==right:
                break
            arr[right].next=arr[left]
            right-=1
        arr[right].next=None
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        current=slow.next
        prev=None
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        slow.next=None    
        p1=head
        p2=prev
        while p1 and p2:
            next1=p1.next
            next2=p2.next
            p1.next=p2
            p2.next=next1
            p1=next1
            p2=next2       

        