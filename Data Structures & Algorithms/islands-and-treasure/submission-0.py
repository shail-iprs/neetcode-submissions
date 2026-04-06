class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        rows=len(grid)
        cols=len(grid[0])
        #visited=[[0 for _ in range(cols)] for _ in range(rows)]

        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    #visited[r][c]=1
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        while q:
            r,c=q.popleft()

            for item in inds:
                nr,nc=r+item[0],c+item[1]
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==2147483647:
                    grid[nr][nc]=grid[r][c]+1
                    q.append([nr,nc])


