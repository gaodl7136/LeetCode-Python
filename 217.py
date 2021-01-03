# 120 ms	18.9 MB
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        ans = False
        l = len(nums)
        for i in range(1,l):
            if nums[i]==nums[i-1]:
                ans = True
                break
        return ans