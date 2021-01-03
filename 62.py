# 32 ms	14.4 MB
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [[0] * m] * n
        a[0][0] = 1
        for i in range(1,n):
            a[i][0] = 1
        for i in range(1,m):
            a[0][i] = 1
        for i in range(1,n):
            for j in range(1,m):
                a[i][j] = a[i-1][j] + a[i][j-1]
        return a[n-1][m-1]