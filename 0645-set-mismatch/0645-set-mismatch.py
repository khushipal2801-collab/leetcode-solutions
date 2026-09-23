class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        freq=[0] *(len(nums)+1)
        for x in nums:
            freq[x]+=1
        duplicate=0
        missing=0
        for i in range(1,len(nums)+1):
            if freq[i]==2:
                duplicate=i
            if freq[i]==0:
                missing=i
        return [duplicate,missing]                
        