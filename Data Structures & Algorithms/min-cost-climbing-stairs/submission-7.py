class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        n=len(cost)
        def get(ind):
            if ind>=n:
                return 0
            if ind in dp:
                return dp[ind]
            res=cost[ind]+min(get(ind+1),get(ind+2))
            dp[ind]=res
            return dp[ind]

        return min(get(0),get(1))