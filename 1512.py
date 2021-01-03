# 36 ms	14.2 MB
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        for i in range(0,l-1):
            for j in range(i+1,l):
                if nums[i] == nums[j]:
                    ans += 1
        return ans