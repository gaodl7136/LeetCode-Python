# 24 ms	14.4 MB
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1,n):
            t = start + 2 * i
            ans = ans ^ t
        return ans