class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])

        visited=[[False for _ in range(n)] for _ in range(m)]
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        from collections import deque

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited[r][c]=True

            while q:
                nr,nc=q.popleft()
                for ind in inds:
                    nnr,nnc=nr+ind[0],nc+ind[1]

                    if 0<=nnr<m and 0<=nnc<n and not visited[nnr][nnc] and grid[nnr][nnc]=='1':
                        visited[nnr][nnc]=True
                        q.append((nnr,nnc))


        res=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1' and not visited[r][c]:
                    bfs(r,c)
                    res+=1
        return res