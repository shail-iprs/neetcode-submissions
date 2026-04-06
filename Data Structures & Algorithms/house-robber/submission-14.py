class Solution:
    def rob(self, nums: List[int]) -> int: 
        n=len(nums)
        dp=[-1]*(n+1)

        def check(ind):
            if ind>=n:
                return 0
            
            if dp[ind]!=-1:
                return dp[ind]
            
            dp[ind]=max(nums[ind]+check(ind+2),check(ind+1))
            return dp[ind]
        check(0)
        return max(dp)