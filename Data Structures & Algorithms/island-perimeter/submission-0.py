class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        from collections import deque
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        def bfs(r,c):
            q=deque()
            q.append([r,c])

            visited[r][c]=1
            cnt=0
            while q:
                nr,nc=q.popleft()
                for item in inds:
                    nnr,nnc=item[0]+nr,item[1]+nc
                    if nnr<0 or nnc<0 or nnr>=rows or nnc>=cols or grid[nnr][nnc]==0:
                        cnt+=1
                    elif not visited[nnr][nnc]:
                        visited[nnr][nnc]=1
                        q.append([nnr,nnc])
            return cnt

        res=0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c]==1:
                    res+=bfs(r,c)
        return res