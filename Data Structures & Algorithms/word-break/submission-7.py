class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd=set(wordDict)
        n=len(s)
        visited=set()
        def dfs(ind):
            if ind==n:
                return True
            if ind in visited:
                return  False
            for end in range(ind+1,n+1):
                if s[ind:end] in wd:
                    if dfs(end):
                        return True
                    visited.add(end)
            return False
        return dfs(0)
        