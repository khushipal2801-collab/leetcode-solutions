class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for x in nums1:
            if x in nums2:
                ans.append(x)
                nums2.remove(x)
        return ans        
        