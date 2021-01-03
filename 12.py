# 48 ms	14.4 MB
class Solution:
    def intToRoman(self, num: int) -> str:
        l = len(str(num))
        s = 1
        match1 = ["I","II","III","IV","V","VI","VII","VIII","IX"]
        match10 = ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        match100 = ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        match1000 = ["M","MM","MMM"]
        ans = ""
        for ii in range(l):
            i = l - ii - 1
            n = int(str(num)[i])
            if s == 1 and n>0:
                ans = match1[n-1] + ans
            if s == 10 and n>0:
                ans = match10[n-1] + ans
            if s == 100 and n>0:
                ans = match100[n-1] + ans
            if s == 1000 and n>0:
                ans = match1000[n-1] + ans
            s = s * 10
        return ans