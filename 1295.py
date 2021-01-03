# 52 ms	14.1 MB
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            l = len(str(i))
            if l % 2 ==0:
                ans += 1
        return ans