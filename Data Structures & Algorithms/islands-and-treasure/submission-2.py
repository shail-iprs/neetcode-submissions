class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        INF=2147483647

        q=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    q.append((r,c))

        while q:
            r,c=q.popleft()
        
            for item in inds:
                nr,nc=item[0]+r,item[1]+c
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==INF:
                    grid[nr][nc]=1+grid[r][c]
                    q.append((nr,nc))