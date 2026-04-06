class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1 if s[0]!='0' else 0

        for ind in range(2,n+1):
            if s[ind-1]!='0':
                dp[ind]+=dp[ind-1]
            if 10<=int(s[ind-2:ind])<=26:
                dp[ind]+=dp[ind-2]
        return dp[n]
        