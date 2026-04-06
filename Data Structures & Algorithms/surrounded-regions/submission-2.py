class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        rows=len(board)
        cols=len(board[0])

        def capture():
            q=deque()
            for r in range(rows):
                for c in range(cols):
                    if (r in [0,rows-1] or c in [0,cols-1]) and board[r][c]=='O':
                        q.append([r,c])
            
            while q:
                r,c=q.popleft()
                if board[r][c]=='O':
                    board[r][c]='T'
                
                    for item in inds:
                        nr,nc=item[0]+r,item[1]+c

                        if 0<=nr<rows and 0<=nc<cols:
                            q.append([nr,nc])

        capture()
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"

