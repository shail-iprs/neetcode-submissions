class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m=len(board)
        n=len(board[0])
        self.res=set()
        words=set(words)
        prefix=set()
        max_len=max([len(w) for w in words])
        path=set()
        for w in words:
            for ind in range(1,len(w)+1):
                prefix.add(w[:ind])

        
        def search(r,c,curr):
            
            if len(curr)==max_len:
                return

            
            if r<0 or r>=m or c<0 or c>=n or (r,c) in path:
                return 
            
            curr+=board[r][c]

            if curr not in prefix:
                return
            
            if curr in words:
                self.res.add(curr)
                #print(curr)
            
            path.add((r,c))
            search(r+1,c,curr)
            search(r-1,c,curr)
            search(r,c+1,curr)
            search(r,c-1,curr)
            path.remove((r,c))
            return
            
        ind=0
        for r in range(m):
            for c in range(n):
                search(r,c,"")
        return list(self.res)