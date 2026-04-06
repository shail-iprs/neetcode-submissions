class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        n=len(nums)
        nums.sort()
        def dfs(ind,curr):
            if ind==n:
                self.res.append(curr[:])
                return 
            if ind>n:
                return 
            
            curr.append(nums[ind])
            dfs(ind+1,curr)
            curr.pop()
            while ind+1<n and nums[ind]==nums[ind+1]:
                ind+=1
            dfs(ind+1,curr)
        dfs(0,[])
        return self.res