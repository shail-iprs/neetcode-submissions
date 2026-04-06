class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def check(r,c,visited):
            from collections import deque
            q=deque()
            q.append([r,c])
            visited[r][c]=1
            count=1
            inds=[[0,1],[0,-1],[-1,0],[1,0]]

            while q:
                nr,nc=q.popleft()
                for item in inds:
                    nnr,nnc=nr+item[0],nc+item[1]
                    if 0<=nnr<rows and 0<=nnc<cols and grid[nnr][nnc]==1 and not visited[nnr][nnc]:
                        visited[nnr][nnc]=1
                        count+=1
                        q.append([nnr,nnc])
            return count

        
        #print(rows,cols)
        max_cnt=0
        visited=[[0 for x in range(cols)] for y in range(rows)]
        #print(visited)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and not visited[r][c]:
                    count=check(r,c,visited)
                    max_cnt=max(count,max_cnt)
        return max_cnt