class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]

        from collections import deque
        q=deque()
        fresh=0
        rotton=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append([r,c,0])
        if fresh==0:
            return 0
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        while q:
            r,c,t=q.popleft()
            # if rotton==fresh:
            #     return t
            for item in inds:
                nr,nc=item[0]+r,item[1]+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    rotton+=1
                    q.append([nr,nc,t+1])
        return t if rotton==fresh else -1