class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp={}
        def checkstring(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==m or j==n:
                return 1 if j==n else 0


            res=0
            if s[i]==t[j]:
                res=checkstring(i+1,j+1)+checkstring(i+1,j)
            else:
                res=checkstring(i+1,j)
            dp[(i,j)]=res
            return dp[(i,j)]
        return checkstring(0,0)