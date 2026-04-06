class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[None]*(amount+1)
        def dfs(total):
            if total==0:
                return 0
            if dp[total]!=None:
                return dp[total]
            res=float('inf')
            for coin in coins:
                if total-coin>=0:
                    res=min(res,1+dfs(total-coin))
            dp[total]=res
            return dp[total]

        min_coins=dfs(amount)
        return min_coins if min_coins!=float('inf') else -1




