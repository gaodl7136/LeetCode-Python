# 32 ms	14.3 MB
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l = len(S)
        s=""
        ans = ""
        for i in range(l):
            if (ord(S[i])>=97 and ord(S[i])<=122) or (ord(S[i])>=65 and ord(S[i])<=90):
                s+=S[i]
        ll = len(s)
        j = ll-1
        for i in range(l):
            if (ord(S[i])>=97 and ord(S[i])<=122) or (ord(S[i])>=65 and ord(S[i])<=90):
                ans+=s[j]
                j-=1
            else:
                ans+=S[i]
        return ans