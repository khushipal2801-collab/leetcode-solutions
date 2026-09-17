class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        ans=num
        for x in range(num,num+2*t+1):
            if abs(x-num)<=2*t:
                ans=x
        return ans        
    
        