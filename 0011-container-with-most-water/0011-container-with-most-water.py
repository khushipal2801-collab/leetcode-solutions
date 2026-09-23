class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        maxarea=0
        while l<r:
            ht=min(height[l],height[r])
            wd=r-l
            area=ht*wd
            maxarea=max(area,maxarea)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxarea      
