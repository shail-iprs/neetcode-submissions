class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        vis=[False]*n
        res=[]

        def dfs(curr,vis):
            if len(curr)==n:
                res.append(curr[:])
                return
            
            for ind in range(n):
                if ind+1<=n-1 and nums[ind]==nums[ind+1] and not vis[ind+1]:
                    continue
                if not vis[ind]:
                    vis[ind]=True
                    curr.append(nums[ind])
                    dfs(curr,vis)
                    curr.pop()
                    vis[ind]=False

        dfs([],vis)
        return res