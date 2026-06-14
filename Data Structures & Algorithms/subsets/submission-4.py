class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        n=len(nums)
        def dfs(ind,curr):
            if ind==n:
                self.res.append(curr[:])
                return 
            if ind>n:
                return
            curr.append(nums[ind]) 
            dfs(ind+1,curr)
            curr.pop()
            dfs(ind+1,curr)
        if not nums:
            return self.res
        dfs(0,[])
        return self.res