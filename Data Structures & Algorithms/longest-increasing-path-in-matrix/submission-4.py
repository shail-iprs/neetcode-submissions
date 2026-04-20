class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        import sys
        sys.setrecursionlimit(10**6)
        m=len(matrix)
        n=len(matrix[0])
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        dp={}

        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            res=1
            for item in inds:
                nr,nc=item[0]+r,item[1]+c
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                    res=max(res,1+dfs(nr,nc))
            dp[(r,c)]=res
            return dp[(r,c)]
        max_len=0
        for r in range(m):
            for c in range(n):
                max_len=max(max_len,dfs(r,c))
        return max_len