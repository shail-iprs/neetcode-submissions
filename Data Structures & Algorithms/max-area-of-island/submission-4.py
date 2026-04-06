class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        inds=[[0,1],[0,-1],[-1,0],[1,0]]

        m=len(grid)
        n=len(grid[0])
        count=0
        visited=[[False for _ in range(n)] for _ in range(m)]
        max_arr=0
        def dfs(r,c):
            cnt=1
            q=deque([(r,c)])
            visited[r][c]=True

            while q:
                nr,nc=q.popleft()
                for item in inds:
                    nnr,nnc=item[0]+nr,item[1]+nc
                    if 0<=nnr<m and 0<=nnc<n and grid[nnr][nnc]==1 and not visited[nnr][nnc]:
                        q.append((nnr,nnc))
                        cnt+=1
                        visited[nnr][nnc]=True
            return cnt
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1 and not visited[r][c]:
                    arr=dfs(r,c)
                    max_arr=max(max_arr,arr)
        return max_arr