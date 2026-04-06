class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for _ in range(n)] for _ in range(n)]
        pos=set()
        neg=set()
        cols=set()
        res=[]
        def dfs(r):
            if r==n:
                res.append(["".join(x) for x in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg or board[r][c]!='.':
                    continue
                
                board[r][c]='Q'
                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)

                dfs(r+1)

                board[r][c]='.'
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)

        dfs(0)
        return res