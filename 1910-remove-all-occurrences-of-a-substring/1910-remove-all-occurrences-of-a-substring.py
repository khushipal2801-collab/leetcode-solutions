class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans=[]
        for ch in s:
            ans.append(ch)
            if len(ans)>=len(part):
                if "".join(ans[-len(part):])==part:
                    for i in range(len(part)):
                        ans.pop()
        return "".join(ans)               