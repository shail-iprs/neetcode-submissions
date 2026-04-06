class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        n=len(s)
        wordDict=set(wordDict)
        def dfs(start,curr):
            if start==n:
                res.append(" ".join(curr[:]))
                return
            
            for end in range(start+1,n+1):
                pre=s[start:end]
                if pre in wordDict:
                    curr.append(pre)
                    dfs(end,curr)
                    curr.pop()
        dfs(0,[])
        return res