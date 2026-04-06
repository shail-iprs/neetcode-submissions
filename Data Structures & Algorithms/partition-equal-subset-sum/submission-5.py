class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        n=len(nums)
        dp=[[-1]*(target+1) for _ in range(n+1)]

        def dfs(ind,target):
            if target==0:
                return True
            if ind>=n or target<0:
                return False
            
            if dp[ind][target]!=-1:
                return dp[ind][target]
            dp[ind][target]=dfs(ind+1,target) or dfs(ind+1,target-nums[ind])
            return dp[ind][target]

        return dfs(0,target)