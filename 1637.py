# 920 ms	54.9 MB
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        l = len(points)
        m = 0
        for i in range(1,l):
            if m < points[i][0]-points[i-1][0]:
                m = points[i][0]-points[i-1][0]
        return m