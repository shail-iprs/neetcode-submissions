class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        n=len(nums)
        def dfs(start,curr_sum,curr):
            if curr_sum==target:
                self.res.append(list(curr))
                return 
            if curr_sum>target or start>=n:
                return
            
            curr.append(nums[start])
            dfs(start,curr_sum+nums[start],curr)
            curr.pop()
            dfs(start+1,curr_sum,curr)
        dfs(0,0,[])
        return self.res