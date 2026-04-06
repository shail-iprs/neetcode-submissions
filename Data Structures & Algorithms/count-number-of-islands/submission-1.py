class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        def check(r,c,visited):
            from collections import deque
            q=deque()
            q.append([r,c])
            visited[r][c]=1
            inds=[[0,1],[0,-1],[-1,0],[1,0]]
            while q:
                nr,nc=q.popleft()
                for item in inds:
                    nnr,nnc=nr+item[0],nc+item[1]
                    if 0<=nnr<rows and 0<=nnc<cols and grid[nnr][nnc]=='1' and not visited[nnr][nnc]:
                        visited[nnr][nnc]=1
                        q.append([nnr,nnc])
            
        count=0
        visited=[[0 for x in range(cols)] for x in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and not visited[r][c]:
                    check(r,c,visited)
                    count+=1
        return count