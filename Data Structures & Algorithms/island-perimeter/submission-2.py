class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        visited=[[False for _ in range(n)] for _ in range(m)]
        res=0
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        def bfs(r,c):
            q=deque()
            count=0
            q.append((r,c))
            visited[r][c]=True
            while q:
                nr,nc=q.popleft()
                for item in inds:
                    nnr=nr+item[0]
                    nnc=nc+item[1]
                    if nnr<0 or nnc<0 or nnr>=m or nnc>=n or grid[nnr][nnc]==0:
                        count+=1
                    elif not visited[nnr][nnc]:
                        visited[nnr][nnc]=True
                        q.append((nnr,nnc))
            return count

        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c]==1:
                    res+=bfs(r,c)
        return res