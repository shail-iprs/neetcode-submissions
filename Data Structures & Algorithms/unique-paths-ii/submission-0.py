class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp={}
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1:
            return 0
        def calcpath(r,c):  
            if (r,c) in dp:
                return dp[(r,c)]
            if r==m-1 and c==n-1:
                return 1
            
            if r>=m or c>=n or obstacleGrid[r][c]==1:
                return 0
            dp[(r,c)]=calcpath(r+1,c)+calcpath(r,c+1)
            return dp[(r,c)]
        return calcpath(0,0)