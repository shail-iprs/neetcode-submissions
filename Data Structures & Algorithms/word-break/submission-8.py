class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        n=len(s)
        visited=set()
        def get(ind):
            if ind==n:
                return True
            if ind in visited:
                return False
            
            for end in range(ind+1,n+1):
                temp=s[ind:end]
                if temp in wordDict:
                    if get(end):
                        return True
                    visited.add(end)
            return False
        return get(0)