class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[]
        for x in nums:
            square=x*x
            ans.append(square)
            ans=sorted(ans)
        return ans       
        