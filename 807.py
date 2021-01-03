# 72 ms	14.3 MB
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top = []
        left = []
        ans = 0
        n = len(grid[0])
        for i in range(n):
            max = 0
            for j in range(n):
                if grid[i][j] > max:
                    max = grid[i][j]
            left.append(max)
        n = len(grid[0])
        for i in range(n):
            max = 0
            for j in range(n):
                if grid[j][i] > max:
                    max = grid[j][i]
            top.append(max)
        for i in range(n):
            for j in range(n):
                min = top[i]
                if min > left[j]:
                    min = left[j]
                ans += (min - grid[i][j])
        
        return ans