class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        from collections import deque
        inds=[[0,1],[0,-1],[-1,0],[1,0]]

        rows=len(grid)
        cols=len(grid[0])
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited[r][c]=True
            cnt=0

            while q:
                nr,nc=q.popleft()
                for ind in inds:
                    nnr,nnc=nr+ind[0],nc+ind[1]
                    if nnr<0 or nnc<0 or nnr>=rows or nnc>=cols or grid[nnr][nnc]==0:
                        cnt+=1
                    elif not visited[nnr][nnc]:
                        visited[nnr][nnc]=True
                        q.append((nnr,nnc))
            return cnt
        res=0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c]==1:
                    res+=bfs(r,c)
        return res