from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}

        left = 0
        have = 0
        required = len(need)

        ans = ""
        ans_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if right - left + 1 < ans_len:
                    ans = s[left:right + 1]
                    ans_len = right - left + 1

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        return ans
        