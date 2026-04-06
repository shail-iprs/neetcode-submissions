class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(ind):
            if ind ==len(nums):
                return 0
            best=1
            for j in range(ind+1,len(nums)):
                if nums[ind]<nums[j]:
                    best=max(best,1+dfs(j))
            return best
        return max(dfs(ind) for ind in range(len(nums)))