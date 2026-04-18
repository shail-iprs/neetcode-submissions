class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(ind,curr):
            if (ind,curr) in dp:
                return dp[(ind,curr)]
            if ind==len(nums):
                return 1 if curr==target else 0
            

            
            dp[(ind,curr)]=dfs(ind+1,curr+nums[ind])+dfs(ind+1,curr-1*(nums[ind]))
            return dp[(ind,curr)]
        return dfs(0,0)