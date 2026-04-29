class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(ind,curr):
            if ind==n:
                return curr
            return dfs(ind+1,curr^nums[ind])+dfs(ind+1,curr)
        return dfs(0,0)