class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        for x in nums[0]:
            found=True
            for i in range(1,len(nums)):
                if x not in nums[i]:
                    found=False
                    break
            if found:
                ans.append(x)
        return sorted(ans)                
        