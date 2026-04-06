class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res=[]
        def dfs(c,curr):
            if len(curr)==k:
                self.res.append(curr[:])
                return
            if c>n:
                return 
            curr.append(c)
            dfs(c+1,curr)
            curr.pop()
            dfs(c+1,curr)
        dfs(1,[])
        return self.res