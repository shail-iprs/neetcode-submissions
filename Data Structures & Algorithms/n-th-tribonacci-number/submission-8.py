class Solution:
    def tribonacci(self, n: int) -> int:
        dp={}

        def get(ind):
            if ind<=0:
                return 0
            if ind==1 or ind==2:
                return 1
            if ind in dp:
                return dp[ind]
            res=get(ind-1)+get(ind-2)+get(ind-3)
            dp[ind]=res
            return dp[ind]
        return get(n)