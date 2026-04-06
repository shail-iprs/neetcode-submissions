class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*(n)
        dp[0]=nums[0]
        dp[1]=max(dp[0],nums[1])

        for ind in range(2,n):
            dp[ind]=max(dp[ind-2]+nums[ind],dp[ind-1])
        print(dp)
        return dp[n-1]