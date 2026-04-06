class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        def dfs(start,curr):
            if start==n:
                res.append(curr[:])
                return
            
            for end in range(start+1,n+1):
                temp=s[start:end]
                if temp==temp[::-1]:
                    curr.append(temp)
                    dfs(end,curr)
                    curr.pop()

        dfs(0,[])
        return res