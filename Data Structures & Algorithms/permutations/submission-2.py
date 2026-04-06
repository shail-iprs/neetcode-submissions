class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        vis=[False]*n
        res=[]
        def dfs(curr,vis):
            if len(curr)==n:
                res.append(curr[:])
                return
            for ind in range(n):
                if not vis[ind]:
                    vis[ind]=True
                    curr.append(nums[ind])
                    dfs(curr,vis)
                    curr.pop()
                    vis[ind]=False
        dfs([],vis)
        return res