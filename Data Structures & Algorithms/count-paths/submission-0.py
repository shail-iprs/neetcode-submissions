class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        def calcpath(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            if r==m-1 and c==n-1:
                return 1
            if r>=m or c>=n:
                return 0
            
            dp[(r,c)]=calcpath(r+1,c)+calcpath(r,c+1)
            return dp[(r,c)]

        return calcpath(0,0)