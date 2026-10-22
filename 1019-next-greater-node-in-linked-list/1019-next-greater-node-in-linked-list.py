# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        ans=[0]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[i]>arr[stack[-1]]:
                index=stack.pop()
                ans[index]=arr[i]
            stack.append(i)
        return ans    


        