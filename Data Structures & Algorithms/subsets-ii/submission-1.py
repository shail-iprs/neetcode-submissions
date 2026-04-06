class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]

        def dfs(ind,curr):
            if ind ==n:
                res.append(curr[:])
                return
            curr.append(nums[ind])
            dfs(ind+1,curr)
            curr.pop()

            while ind +1<=n-1 and nums[ind]==nums[ind+1]:
                ind+=1
            dfs(ind+1,curr)
        dfs(0,[])
        return res