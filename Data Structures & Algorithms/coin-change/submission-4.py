class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        def dfs(ind,curr):
            if (ind,curr) in dp:
                return dp[(ind,curr)]
            if curr==amount:
                return 0
            if curr>amount or ind==len(coins):
                return float('inf')
            
            take=1+dfs(ind,curr+coins[ind])
            not_take=dfs(ind+1,curr)
            dp[(ind,curr)]=min(take,not_take)
            return dp[(ind,curr)]
        

        res=dfs(0,0)
        return res if res!=float('inf') else -1