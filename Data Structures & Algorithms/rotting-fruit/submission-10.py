class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruit=0
        m=len(grid)
        n=len(grid[0])
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        q=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh_fruit+=1
                elif grid[r][c]==2:
                    q.append((r,c,0))
        print(fresh_fruit)
        t=0
        while q:
            r,c,t=q.popleft()
            # if fresh_fruit==0:
            #     return t
            for ind in inds:
                nr,nc=r+ind[0],c+ind[1]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    q.append((nr,nc,t+1))
                    fresh_fruit-=1
        return -1 if fresh_fruit!=0 else t
