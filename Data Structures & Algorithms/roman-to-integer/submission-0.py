class Solution:
    def romanToInt(self, s: str) -> int:
        mp={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        res=0
        for ind in range(len(s)):
            if ind+1<len(s) and mp[s[ind]]<mp[s[ind+1]]:
                res-=mp[s[ind]]
            else:
                res+=mp[s[ind]]
        return res