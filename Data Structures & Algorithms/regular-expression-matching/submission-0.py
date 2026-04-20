class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        dp={}
        def check(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j==n:
                return i==m

            res=False
            first_match=(i<m and (s[i]==p[j] or p[j]=='.'))
            if j+1<n and p[j+1]=='*':
                res=check(i,j+2) or (first_match and check(i+1,j))
            else:
                res=first_match and check(i+1,j+1)
            dp[(i,j)]=res
            return res
        return check(0,0)