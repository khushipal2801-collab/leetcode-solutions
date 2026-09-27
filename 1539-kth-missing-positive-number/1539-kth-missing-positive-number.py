class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        count=0
        n=len(arr)
        for i in range(1,n+k+1):
            if i not in arr:
                count+=1
            if count==k:
                return i    
        
        