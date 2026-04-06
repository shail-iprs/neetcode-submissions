class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        def res(ind):
            if ind>=n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=max(nums[ind]+res(ind+2),res(ind+1))
            return dp[ind]
        return res(0)