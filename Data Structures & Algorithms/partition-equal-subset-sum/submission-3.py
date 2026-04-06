class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        def dfs(ind,target):
            if ind>=len(nums):
                return target==0
            
            if target<0:
                return False

            return dfs(ind+1,target) or dfs(ind+1,target-nums[ind])
        return dfs(0,sum(nums)//2)