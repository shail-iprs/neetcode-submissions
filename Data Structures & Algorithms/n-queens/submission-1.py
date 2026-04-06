class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos=set()
        neg=set()
        col=set()
        board=[["." for _ in range(n)] for _ in range(n)]
        res=[]
        def dfs(r):
            if r==n:
                res.append(["".join(x) for x in board])
                return
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue
                board[r][c]='Q'
                col.add(c)
                #path.add((r,c))
                pos.add((r+c))
                neg.add((r-c))

                dfs(r+1)

                board[r][c]='.'
                col.remove(c)
                #path.remove((r,c))
                pos.remove((r+c))
                neg.remove((r-c))

        dfs(0)
        return res