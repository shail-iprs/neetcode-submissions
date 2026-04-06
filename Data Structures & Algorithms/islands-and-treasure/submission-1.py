class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        #visited=[[False for _ in range(n)] for _ in range(m)]
        INF=2147483647
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        
        q=deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    q.append((r,c))
        
        while q:
            nr,nc=q.popleft()
            for ind in inds:
                nnr,nnc=nr+ind[0],nc+ind[1]
                if 0<=nnr<m and 0<=nnc<n and grid[nnr][nnc]==INF:
                    grid[nnr][nnc]=1+grid[nr][nc]
                    q.append((nnr,nnc))
