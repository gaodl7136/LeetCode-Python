# 208 ms	14.1 MB
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        v = []
        ans = []
        
        n = len(groupSizes)
        for i in range(n):
            v.append(0)
        for i in range(n):
            if (v[i]<1):
                size = groupSizes[i]
                t = 1
                temp = []
                temp.append(i)
                v[i]=1
                for j in range(i,n):
                    if groupSizes[j]==size and v[j]<1 and t<size:
                        v[j]=1
                        temp.append(j)
                        t+=1
                ans.append(temp)
        return ans