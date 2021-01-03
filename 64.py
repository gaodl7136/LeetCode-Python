# 92 ms	15.7 MB
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        a = grid
        for i in range(1,n):
            a[i][0] = a[i-1][0] + grid[i][0]
        for j in range(1,m):
            a[0][j] = a[0][j-1] + grid[0][j]
        for i in range(1,n):
            for j in range(1,m):
                mm = a[i-1][j]
                if mm > a[i][j-1]:
                    mm = a[i][j-1]
                a[i][j] = mm + grid[i][j]
        return a[n-1][m-1]