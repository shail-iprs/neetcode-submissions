class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}

        def dfs(ind,curr):
            if (ind,curr) in dp:
                return dp[(ind,curr)]
            if curr==amount:
                return 1
            
            if curr>amount or ind==len(coins):
                return 0
            
            dp[(ind,curr)]=dfs(ind,curr+coins[ind])+dfs(ind+1,curr)
            return dp[(ind,curr)]
        return dfs(0,0)
