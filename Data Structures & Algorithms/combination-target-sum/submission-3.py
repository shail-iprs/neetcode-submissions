class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        n=len(nums)
        def dfs(ind,csum,curr):
            if ind==n-1 and csum==target:
                self.res.append(curr[:])
                return 
            
            if ind>=n or csum>target:
                return 
            curr.append(nums[ind])
            dfs(ind,csum+nums[ind],curr)
            curr.pop()
            dfs(ind+1,csum,curr)

        dfs(0,0,[])
        return self.res