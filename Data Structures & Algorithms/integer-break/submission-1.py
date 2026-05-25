class Solution:
    def integerBreak(self, n: int) -> int:
        dp={}
        def get(rem):
            if rem==0:
                return 1
            
            if rem in dp:
                return dp[rem]
            ans=0
            for ind in range(1,rem):
                first=ind
                second=rem-ind

                take=first*second

                nottake=first * get(rem-ind)   

                ans=max(ans,take,nottake)
            dp[rem]=ans
            return ans
        return get(n)

