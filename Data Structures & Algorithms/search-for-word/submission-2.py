class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        n=len(word)
        path=set()

        def dfs(r,c,ind):
            if ind==n:
                return True
            
            if r<0 or r>=rows or c<0 or c>=cols or word[ind]!=board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))

            res=(dfs(r,c+1,ind+1) or dfs(r,c-1,ind+1) or dfs(r+1,c,ind+1) or dfs(r-1,c,ind+1))

            path.remove((r,c))
            return res
        ind=0
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,ind):
                    return True
        return False

