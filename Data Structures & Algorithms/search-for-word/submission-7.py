class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit=set()
        #inds=[[0,1],[0,-1],[-1,0],[1,0]]
        rows=len(board)
        cols=len(board[0])

        def check(r,c,ind):
            if ind==len(word):
                return True
            
            if r<0 or r>=rows or c<0 or c>=cols or word[ind]!=board[r][c] or (r,c) in visit:
                return False
            
            visit.add((r,c))
            res=check(r+1,c,ind+1) or check(r-1,c,ind+1) or check(r,c+1,ind+1) or check(r,c-1,ind+1) 
            visit.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if check(r,c,0):
                    return True
        return False
                    
        