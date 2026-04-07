class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        inds=[[0,1],[0,-1],[1,0],[-1,0]]
        q=deque()
        fresh=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c,0))
        count=0
        t=0
        while q:
            r,c,t=q.popleft()
            for item in inds:
                nr,nc=item[0]+r,item[1]+c
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    q.append((nr,nc,t+1))
                    grid[nr][nc]=2
                    count+=1
        return t if count==fresh else -1