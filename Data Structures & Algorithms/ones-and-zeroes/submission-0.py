class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=len(strs)
        arr=[[0]*2 for _ in range(l)]
        for ind in range(l):
            for c in range(len(strs[ind])):
                arr[ind][ord(strs[ind][c])-ord('0')]+=1
        dp={}
        def dfs(ind,m,n):
            if (ind,m,n) in dp:
                return dp[(ind,m,n)]

            if ind==l:
                return 0
            res=dfs(ind+1,m,n)
            if m>=arr[ind][0] and n>=arr[ind][1]:
                res=max(res,1+dfs(ind+1,m-arr[ind][0],n-arr[ind][1]))
            dp[(ind,m,n)]=res
            return dp[(ind,m,n)]
        return dfs(0,m,n)