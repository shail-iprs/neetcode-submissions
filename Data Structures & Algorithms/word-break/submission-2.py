class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)

        dp[n]=True

        for ind in range(n-1,-1,-1):
            for w in wordDict:
                if ind+len(w)<=n and s[ind:ind+len(w)]==w:
                    dp[ind]=dp[ind+len(w)]
                if dp[ind]:
                    break
        return dp[0]