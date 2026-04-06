class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*n
        def climb(ind):
            if ind>=n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=cost[ind]+min(climb(ind+1),climb(ind+2))
            return dp[ind]
        return min(climb(0),climb(1))