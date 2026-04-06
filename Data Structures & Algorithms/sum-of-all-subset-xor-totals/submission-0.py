class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(start,curr_sum):
            if start==n:
                return curr_sum
            return dfs(start+1,curr_sum^nums[start])+dfs(start+1,curr_sum)

        return dfs(0,0)