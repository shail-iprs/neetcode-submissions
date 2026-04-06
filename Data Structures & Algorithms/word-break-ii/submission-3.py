class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wd=set(wordDict)
        n=len(s)

        res=[]
        def dfs(ind,curr):
            if ind==n:
                res.append(" ".join(curr[:]))
                return
            for end in range(ind+1,n+1):
                temp=s[ind:end]
                if temp in wd:
                    curr.append(temp)
                    dfs(end,curr)
                    curr.pop()
        dfs(0,[])
        return res