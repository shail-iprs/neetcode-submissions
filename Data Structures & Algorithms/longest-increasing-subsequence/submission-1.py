class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)

        def dfs(ind):
            if ind ==len(nums):
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            best=1
            for j in range(ind+1,len(nums)):
                if nums[ind]<nums[j]:
                    best=max(best,1+dfs(j))
            dp[ind]=best
            return dp[ind]
        return max(dfs(ind) for ind in range(len(nums)))