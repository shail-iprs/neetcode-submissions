class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])

        q=deque()
        inds=[[0,1],[0,-1],[-1,0],[1,0]]

        for r in range(m):
            for c in range(n):
                if (r in [0,m-1] or c in [0,n-1]) and board[r][c]=='O':
                    q.append((r,c))
                    board[r][c]='T'
        
        while q:
            r,c=q.popleft()
            for ind in inds:
                nr,nc=ind[0]+r,ind[1]+c
                if 0<=nr<m and 0<=nc<n and board[nr][nc]=='O':
                    q.append((nr,nc))
                    board[nr][nc]='T'
        
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'
