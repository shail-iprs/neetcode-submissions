class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q=deque()
        inds=[[0,1],[0,-1],[-1,0],[1,0]]

        m=len(board)
        n=len(board[0])

        for r in range(m):
            for c in range(n):
                if (r in [0,m-1] or c in [0,n-1]) and board[r][c]=='O':
                    board[r][c]='T'
                    q.append((r,c))

        while q:
            r,c=q.popleft()
            for item in inds:
                nr,nc=item[0]+r,item[1]+c
                if 0<=nr<m and 0<=nc<n and board[nr][nc]=='O':
                    board[nr][nc]='T'
                    q.append((nr,nc))

        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'
            
