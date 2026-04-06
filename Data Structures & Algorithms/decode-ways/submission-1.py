class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1]*(n+1)
        def dfs(ind):
            if ind==len(s):
                return 1
            if s[ind]=='0':
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            res=dfs(ind+1)
            if ind+1<len(s) and 10<=int(s[ind:ind+2])<=26:
                res+=dfs(ind+2)
            dp[ind]=res
            return dp[ind]
        return dfs(0)
        