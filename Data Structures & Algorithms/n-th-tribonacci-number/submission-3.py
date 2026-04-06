class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=1
        for ind in range(3,n+1):
            dp[ind]=dp[ind-1]+dp[ind-2]+dp[ind-3]
        return dp[n]