class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)

        for ind in range(1,n+1):
            if ind%2==0:
                dp[ind]=dp[ind//2]
            else:
                dp[ind]=dp[ind//2]+1
        return dp