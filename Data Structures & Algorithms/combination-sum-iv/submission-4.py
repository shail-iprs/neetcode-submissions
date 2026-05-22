class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp={}
        def get(curr):
            if curr==target:
                return 1
            if curr>target:
                return 0
            if curr in dp:
                return dp[curr]
            ans=0
            for ind in range(n):
                ans+=get(curr+nums[ind])
            dp[curr]=ans
            return ans
        return get(0)