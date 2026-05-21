class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        n=len(s)
        visited=set()
        dp={}
        def get(ind):
            if ind==n:
                return True
            if ind in visited:
                return False
            if ind in dp:
                return dp[ind]
            res=False
            for end in range(ind+1,n+1):
                temp=s[ind:end]
                if temp in wordDict:
                    if get(end):
                        res=True
                    visited.add(end)
            dp[ind]=res
            return dp[ind]
        return get(0)