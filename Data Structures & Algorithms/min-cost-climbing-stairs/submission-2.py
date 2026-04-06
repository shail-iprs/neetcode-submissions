class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]

        for ind in range(2,n):
            dp[ind]=cost[ind]+min(dp[ind-1],dp[ind-2])
        return min(dp[n-1],dp[n-2])