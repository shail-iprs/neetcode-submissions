class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp={}
        n=len(s)
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==j:
                return 1
            if i==n or j==0 or i>j:
                return 0
            if s[i]==s[j]:
                dp[(i,j)]=2+dfs(i+1,j-1)
            else:
                dp[(i,j)]=max(dfs(i+1,j),dfs(i,j-1))
            return dp[(i,j)]
        
        #print(s_rev)
        return dfs(0,len(s)-1)