class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        
        def dfs(start,curr):
            if start==n:
                res.append(curr[:])
                return
            
            for end in range(start+1,n+1):
                prefix=s[start:end]
                if prefix==prefix[::-1]:
                    curr.append(prefix)
                    dfs(end,curr)
                    curr.pop()

        dfs(0,[])
        return res
