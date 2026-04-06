class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows=len(grid)
        cols=len(grid[0])
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        rotton=0
        fresh=0

        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c,0))
        step=0
        while q:
            r,c,step=q.popleft()
            for item in inds:
                nr,nc=item[0]+r,item[1]+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    q.append((nr,nc,step+1))
                    rotton+=1

        return step if fresh==rotton else -1


