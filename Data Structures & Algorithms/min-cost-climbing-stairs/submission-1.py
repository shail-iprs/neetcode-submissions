class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*(len(cost)+1)
        def res(ind):
            if ind>=len(cost):
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=cost[ind]+min(res(ind+1),res(ind+2))
            return dp[ind]
        
        return min(res(0),res(1))