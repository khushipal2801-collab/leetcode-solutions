class Solution:
    def reverseWords(self, s: str) -> str:
        n=s.split()
        a=" ".join(n[::-1])
        return a
        
        