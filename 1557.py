# 	1120 ms	53.3 MB
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        temp = []
        for i in range(n):
            temp.append(0)
        for f,t in edges:
            temp[t] = 1
        for i in range(n):
            if temp[i] == 0:
                ans.append(i)
        return ans