class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={len(s):True}
        def dfs(ind):
            if ind==len(s):
                return True
            if ind in dp:
                return dp[ind]
            for w in wordDict:
                if ind+len(w)<=len(s) and s[ind:ind+len(w)]==w:
                    if dfs(ind+len(w)):
                        dp[ind]=True
                        return dp[ind]
            dp[ind]=False
            return dp[ind]
        return dfs(0)