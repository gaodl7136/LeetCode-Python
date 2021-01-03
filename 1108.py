# 32 ms	14 MB
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = address.replace(".","[.]")
        return ans