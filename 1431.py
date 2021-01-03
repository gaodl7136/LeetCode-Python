# 32 ms	14.3 MB
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        b = []
        m = max(candies)
        l = len(candies)
        for i in range(l):
            if (candies[i]+extraCandies >= m):
                b.append(True)
            else:
                b.append(False)
        return b