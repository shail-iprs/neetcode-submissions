class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(nums)
        def dfs(ind,curr_sum,curr):
            if curr_sum==target:
                res.append(curr[:])
                return
            if ind>=n or curr_sum>target:
                return
            curr.append(nums[ind])
            dfs(ind,curr_sum+nums[ind],curr)
            curr.pop()
            dfs(ind+1,curr_sum,curr)
        dfs(0,0,[])
        return res