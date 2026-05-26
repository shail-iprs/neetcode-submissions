class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def get(ind):
            if ind<1:
                return 0
            if ind in dp:
                return dp[ind]

            if ind==1 or ind==2:
                return ind
            dp[ind]=get(ind-1)+get(ind-2)
            return dp[ind]
        
        return get(n)