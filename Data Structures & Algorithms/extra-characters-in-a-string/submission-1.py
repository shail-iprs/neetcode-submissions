class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictonary=set(dictionary)
        dp={}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i==len(s):
                return 0
            
            res=1+dfs(i+1)

            for j in range(i+1,len(s)+1):
                temp=s[i:j]
                if temp in dictionary:
                    res=min(res,dfs(j))
            dp[i]=res
            return res
        return dfs(0)