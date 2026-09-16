class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
            sum=0
            for i in range(len(numbers)+1):
                for j in range(i+1,len(numbers)+1):
                    sum=numbers[i]+numbers[j]
                if sum==target:
                return [i+1,j+1] """
        left=0
        right=len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            if numbers[left]+numbers[right]>target:
                right-=1
            if numbers[left]+numbers[right]<target:
                left+=1                        
             


        