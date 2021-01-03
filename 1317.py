# 32 ms	14 MB
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 0
        t=1
        while t>0 and a<=n/2:
            a += 1
            b = n-a
            s = str(a)+str(b)
            t = 0
            for i in s:
                if i == '0':
                    t=1
        ans = []
        ans.append(a)
        ans.append(b)
        return ans