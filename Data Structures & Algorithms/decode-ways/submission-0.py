class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(ind):
            if ind==len(s):
                return 1
            if s[ind]=='0':
                return 0
            res=dfs(ind+1)
            if ind+1<len(s) and 10<=int(s[ind:ind+2])<=26:
                res+=dfs(ind+2)
            return res
        return dfs(0)