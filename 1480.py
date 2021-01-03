# 32 ms	14.3 MB
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sums.append(nums[0])
        l = len(nums)
        for i in range(1,l):
            sums.append(sums[i-1] + nums[i])
        return sums