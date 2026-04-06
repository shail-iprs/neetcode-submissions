class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        rcount=[0]*m
        ccount=[0]*n

        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    rcount[r]+=1
                    ccount[c]+=1

        res=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1 and max(rcount[r],ccount[c])>1:
                    res+=1
        return res