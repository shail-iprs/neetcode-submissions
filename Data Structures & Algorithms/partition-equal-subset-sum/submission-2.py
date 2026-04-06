class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        total=sum(nums)
        def dfs(ind,curr_sum):
            if curr_sum*2==total:
                return True
            if ind>=len(nums):
                return False
            if curr_sum>total//2:
                return False
            return dfs(ind+1,curr_sum+nums[ind]) or dfs(ind+1,curr_sum)
        return dfs(0,0)