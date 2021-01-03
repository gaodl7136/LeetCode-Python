# 188 ms	14.5 MB
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        x = []
        y = []
        for i in range(n):
            x.append(0)
        for j in range(m):
            y.append(0)
        for i in range(n):
            for j in range(m):
                x[i] += mat[i][j]
                y[j] += mat[i][j]
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and x[i] == 1 and y[j] == 1:
                    ans += 1
        return ans