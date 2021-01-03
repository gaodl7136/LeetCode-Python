# 	32 ms	14 MB
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        for c in s:
            if c == 'R':
                r += 1
            else:
                l += 1
            if r == l:
                ans += 1
                r = 0
                l = 0
        return ans