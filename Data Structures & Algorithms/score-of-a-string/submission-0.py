class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        ind=1

        while ind < len(s):
            res+=abs(ord(s[ind])-ord(s[ind-1]))
            ind+=1
        return res