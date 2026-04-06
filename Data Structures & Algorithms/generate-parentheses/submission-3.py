class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def dfs(opened,closed,curr):
            if opened==closed==n:
                res.append("".join(curr[:]))
                return
            
            if opened<n:
                curr.append('(')
                dfs(opened+1,closed,curr)
                curr.pop()
            
            if closed<opened:
                curr.append(')')
                dfs(opened,closed+1,curr)
                curr.pop()
        dfs(0,0,[])
        return res