class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp={}
        def minpath(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            if r==m-1 and c==n-1:
                return grid[r][c]
            if r>=m or c>=n:
                return float('inf')
            
            dp[(r,c)]=grid[r][c]+min(minpath(r+1,c),minpath(r,c+1))
            return dp[(r,c)]
        return minpath(0,0)