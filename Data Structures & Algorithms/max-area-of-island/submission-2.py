class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]

        from collections import deque

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited[r][c]=True
            cnt=1
            inds=[[0,1],[0,-1],[-1,0],[1,0]]
            while q:
                nr,nc=q.popleft()
                for ind in inds:
                    nnr,nnc=nr+ind[0],nc+ind[1]
                    if 0<=nnr<m and 0<=nnc<n and not visited[nnr][nnc] and grid[nnr][nnc]==1:
                        cnt+=1
                        q.append((nnr,nnc))
                        visited[nnr][nnc]=True
            return cnt
        max_res=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1 and not visited[r][c]:
                    res=bfs(r,c)
                    max_res=max(max_res,res)
        return max_res