class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        inds=[[0,1],[0,-1],[-1,0],[1,0]]

        m=len(grid)
        n=len(grid[0])
        count=0
        visited=[[False for _ in range(n)] for _ in range(m)]

        def dfs(r,c):
            q=deque([(r,c)])
            visited[r][c]=True
            while q:
                nr,nc=q.popleft()
                for item in inds:
                    nnr,nnc=item[0]+nr,item[1]+nc
                    if 0<=nnr<m and 0<=nnc<n and grid[nnr][nnc]=='1' and not visited[nnr][nnc]:
                        visited[nnr][nnc]=True
                        q.append((nnr,nnc))


        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1' and not visited[r][c]:
                    dfs(r,c)
                    count+=1
        return count