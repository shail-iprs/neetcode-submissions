class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #arr=list(range(1,n+1))
        res=[]

        def dfs(start,curr):
            if len(curr)==k:
                res.append(curr[:])
                return
            if start>n or len(curr)>k:
                return
            curr.append(start)
            dfs(start+1,curr)
            curr.pop()
            dfs(start+1,curr)
        dfs(1,[])
        return res