class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m=len(points)
        n=len(points[0])
        dp={}
        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]

            if r==m-1:
                return 0
            ans=0
            for col in range(n):
                ans=max(ans,points[r+1][col]-abs(col-c)+dfs(r+1,col))
            dp[(r,c)]=ans
            return dp[(r,c)]
        res=0
        for c in range(n):
            res=max(res,points[0][c]+dfs(0,c))
        return res